import pandas as pd

#Importing dictionary table.

dic = pd.read_csv("C:\\Users\\jeanp\\Documents\\GitHub\\SSC\\Structure Calc - Dictionary.csv")

dic = dic.dropna()

dic = pd.DataFrame(dic)

print(dic.to_string())

dic_group = dic['Megastructure']

dic_group = dic['Megastructure'].drop_duplicates()

print(dic_group)
