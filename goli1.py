import numpy as np
import pandas as pd

bill = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Customer Bill Detail.csv")
order = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Customer Order Item Details.csv")
pricing = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Market Pricing.csv")
pricing1 = pricing.copy()

print(pricing.shape)
pricing = pricing[pd.notnull(pricing['Rate'])]  #don't consider rows where price is not mentioned
pricing.shape

goli_menu_df = pd.DataFrame(columns = ['Menu Item','Rate'])  #new df to store only the given Goli items
for i in pricing.index:
    if pricing.loc[i,'Restaurant'] == 'Goli':
        goli_menu_df = goli_menu_df.append({'Menu Item':pricing.loc[i,'Menu Item'].strip(),'Rate':pricing.loc[i,'Rate']},ignore_index=True)

for i in goli_menu_df.index:    #correct inconsistencies
    if goli_menu_df.loc[i,'Menu Item'] == 'hicken Palak Full':
        goli_menu_df.loc[i,'Menu Item'] = 'Chicken Palak Full'
    elif goli_menu_df.loc[i,'Menu Item'] == 'Bread Omlatte':
        goli_menu_df.loc[i,'Menu Item'] = 'Bread Omlette'
    elif goli_menu_df.loc[i,'Menu Item'] == 'Omlatte':
        goli_menu_df.loc[i,'Menu Item'] = 'Omlette'
    goli_menu_df.loc[i,'Menu Item'] = goli_menu_df.loc[i,'Menu Item'].lower()

goli_menu = goli_menu_df['Menu Item'].unique()  #set of all Goli dishes
goli_menu_df.shape

goli_menu.sort()
print(len(goli_menu))
goli_menu_lower = [i.lower() for i in goli_menu]
#goli_menu

pricing1 = pd.DataFrame(columns = ['Restaurant','Menu Header','Menu Item','Rate','What people love here'])  #new df containg all restaurent dishes except Goli 
for i in pricing.index:
    if pricing.loc[i,'Restaurant']!='Goli' and pricing.loc[i,'Menu Item'].lower() in goli_menu_lower:
        pricing1 = pricing1.append(pricing.loc[i])
for i in pricing1.index:
    pricing1.loc[i,'Menu Item'] = pricing1.loc[i,'Menu Item'].lower()

print(pricing1.shape)
pricing1.head()

temp = pd.DataFrame(columns = ['Dish','Sum of Prices','Comp_count','Goli Rate'])
temp['Dish'] = goli_menu_lower
temp.fillna(0,inplace = True)
temp.set_index('Dish',inplace=True)
temp.head()

for i in pricing1.index:
    cost = int(pricing1.loc[i,'Rate'])
    temp.loc[pricing1.loc[i,'Menu Item'],'Sum of Prices'] += cost
    temp.loc[pricing1.loc[i,'Menu Item'],'Comp_count'] += 1

temp['Goli Rate'] = temp['Sum of Prices']/temp['Comp_count']
for i in temp.index:
    if temp.loc[i,'Sum of Prices'] == 0:
        for j in goli_menu_df.index:
            if goli_menu_df.loc[j,'Menu Item'] == i:
                temp.loc[i,'Goli Rate'] = goli_menu_df.loc[j,'Rate']
goli_final_menu = temp.drop(labels = ['Sum of Prices','Comp_count'],axis=1)
print(goli_final_menu)