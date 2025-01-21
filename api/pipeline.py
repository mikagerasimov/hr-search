import database as dtb
from prefect import flow, task
import pandas as pd
from os import path
from database import from_bd


@task
def load_data_from_excel(excel):
    return dtb.to_csv(excel)


@task
def upload_data_to_bd():
    return dtb.df_tobd()

@task
def format(df):
    df[df.columns[0]].astype(str)
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


@task
def average(df):
    df['Срзнач'] = df.drop(columns=['Субъект']).mean(axis=1)
    cols = df.columns.tolist()
    cols.insert(1, cols.pop(-1))
    return df


@task
def names(df):
    df.columns = df.columns.str.replace(r"\s*\n\s*", " ", regex=True)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'20172\)', '2017', regex=True)
    return df


@task
def null(df):
    nan_cols = len(df) * (0.7)  # 70% пропусков довольно высоко для статистических методов, нам придется их удалить.
    nan_rows = df.shape[1] * 0.7
    df = df.dropna(axis=1, thresh=nan_cols).dropna(axis=0, thresh=nan_rows)
    df.drop_duplicates()

    # если остались другие значения, где пустые поля
    missing_values = df.isnull().sum().sort_values(
        ascending=False)  # Метод isnull() создаёт новый DataFrame того же размера, что и df, но с булевыми значениями: метод sum() применяется к результату isnull(), чтобы посчитать количество True (то есть пропущенных значений) в каждом столбце. Он работает по умолчанию по столбцам (оси 0) и суммирует количество True для каждого столбца.
    columns = missing_values[missing_values > 0].index.tolist()
    if columns:
        print("Количество пропущенных значений в каждом столбце:")
        for col, count in missing_values.items():
            if count > 0:
                print(f"{col}: {count} отсутствующих значений. Были заполены средним")
            for column_name in columns:
                row_mean = df[column_name].mean(axis=1)
                # Заполняем пропущенные значения в строках средним значением этой строки
                df[column_name] = df.apply(
                    lambda row: row[column_name] if pd.notna(row[column_name]) else row_mean[row.name], axis=1)
    return df


@task
def okrug(df):
    filtered = df[~df["Субъект"].str.lower().str.contains("федеральный округ", na=False)]

    return filtered


@flow
def working(excel_file):
    #Загружаем DF из БД
    df = load_data_from_excel(excel_file)

    #форматируем, на всякий случай
    df = format(df)

    df = average(df)

    #Чистим ошибки записи в строку
    df = names(df)

    #Удаляем лишние столбцы
    df = okrug(df)

    #Чистим от большого количества пропусков, если их мало, то заполняются средним
    df = null(df)

    return