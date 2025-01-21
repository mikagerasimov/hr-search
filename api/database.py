import pandas as pd
# import psycopg2
from sqlalchemy import create_engine
from os import path

# Параметры подключения
db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "mydb",
    "user": "admin",
    "password": "secret"
}


def to_csv(excel_file):
    # Переводит нужный лист и строки в цсв
    df = pd.read_excel(excel_file, sheet_name='3', header=4, engine='openpyxl')
    df.rename(columns={df.columns[0]: 'Субъект'}, inplace=True)
    df.to_csv('csv_file', index=False)
    return df

def df_tobd(df):

    # Шаг 2: Сформировать SQL для создания таблицы
    table_name = "trud"
    columns = ", ".join([f"{col} TEXT" for col in df.columns])  # Все колонки как TEXT для универсальности
    create_table_query = f"CREATE TABLE {table_name} ({columns});"

    # Шаг 3: Подключиться к PostgreSQL и выполнить запрос
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")  # Удалить старую таблицу, если она существует
        cursor.execute(create_table_query)  # Создать таблицу
        connection.commit()
        print(f"Таблица {table_name} создана.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cursor.close()
        connection.close()

    # Шаг 4: Загрузить данные
    engine = create_engine(
        f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print("Данные успешно загружены!")



    #Получение из БД. Перевод в формат ДФ
def from_bd():
    # Создание строки подключения
    connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    engine = create_engine(connection_string)

    # Загрузка данных из базы данных
    df = pd.read_sql("SELECT * FROM trud;", engine)
    return df
