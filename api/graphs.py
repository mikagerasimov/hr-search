#гистограма
def Po_regionam(df):
    category_data1 = df[df.columns[0]]
    print(category_data1)
    data1 = df[df.columns[1]]
    return category_data1, data1


#График с точками
def dots(df):
    data_dots = []
    for i in df.columns[1:]:
        tata = df[df["Субъект"].str.contains("Республика Татарстан", case=False, na=False)]
        xy = [i,tata.iloc[0][i]]
        data_dots.append(xy)
    print(data_dots)
    return data_dots