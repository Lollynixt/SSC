import pandas as pd

#Importing dictionary table.

dic = pd.read_csv("C:\\Users\\jeanp\\Documents\\GitHub\\SSC\\Structure Calc - Dictionary.csv")

dic = dic.dropna()

dic = pd.DataFrame(dic)

#print(dic.to_string()) test to see table import

dic_group = dic['Megastructure'] #selecting only megastructures for menu

menu = dic_group = dic['Megastructure'].drop_duplicates().reset_index(drop=True) #removing dupes

print(pd.DataFrame(menu.columns))

#print(menu['Megastructure'].to_list())

menu_choice = input('Which structure 0\\1\\2\\3: ')




