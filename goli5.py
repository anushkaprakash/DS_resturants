import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bill = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Customer Bill Detail.csv")
bill.head()

bill.drop(labels = ['Type','Date','Bill Number','Discount','Subtotal','Delivery Amt','Channel','Customer ID'], axis=1, inplace=True)
bill.head()

df = pd.DataFrame(columns = ['Dish Combo','Count','Cost'])
for i in bill.index:
    a = bill.loc[i,'Dish Details']
    a = a.split(',')
    a = [i.split(' (')[0] for i in a]
    a = set(a)
    a = list(a)
    if len(a)>1:
        flag = 0
        j = 0
        tt = 0
        for j in df.index:
            flag = 0
            temp = df.loc[j,'Dish Combo']
            if len(a) == len(temp):
                for k in range(len(a)):
                    if a[k]!=temp[k]:
                        flag = 1
                if flag == 0:
                    tt = j
                    break
            else:
                flag = 1
        if flag == 1 or i==0:
            df = df.append({'Dish Combo':a,'Count':1,'Cost':bill.loc[i,'Total Bill']}, ignore_index=True)
        else:
            df.loc[tt,'Count'] +=1

df.sort_values('Count',inplace=True,ascending=False)
df['Cost'] = df['Cost']-0.05*df['Cost']
print(df.head())