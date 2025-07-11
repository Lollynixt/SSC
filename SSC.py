import pandas as pd

#Importing dictionary table.

dic = pd.read_csv("C:\\Users\\jeanp\\Documents\\GitHub\\SSC\\Structure Calc - Dictionary.csv")

dic = dic.dropna()

print(dic.to_string())
