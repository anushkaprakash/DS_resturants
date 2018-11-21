import numpy as np
import pandas as pd

order = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Customer Order Item Details.csv")
dish = order['Dish Name'].unique()
dish.sort()
order.head()

dict1 = {}
for i in order.index:
    if order.loc[i,'Dish Name'] not in dict1.keys():
        dict1[order.loc[i,'Dish Name']] = order.loc[i,'Quantity']
    else:
        dict1[order.loc[i,'Dish Name']] += order.loc[i,'Quantity']

df = pd.DataFrame.from_dict(dict1, orient = 'index' )
df.columns = ['Count']
df.head()

df.sort_values('Count',inplace=True,ascending=False)
df.head()

print("DISHES TO PROMOTE")
for i in df.index:
    if df.loc[i,'Count']>=200:
        print(i)
        
print("\nDISHES TO REMOVE")
for i in df.index:
    if df.loc[i,'Count']<=10:
        print(i)