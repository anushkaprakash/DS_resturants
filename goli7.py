import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pricing = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Market Pricing.csv")
pricing.head()

pricing.drop_duplicates(['What people love here'],inplace=True)
pricing.drop(labels = ['Restaurant','Menu Header','Menu Item','Rate'],axis=1,inplace=True)
pricing.dropna(inplace=True)
pricing.head()

dishes = []
for i in pricing.index:
    dishes += pricing.loc[i,'What people love here'].split(',')
dishes.sort()
dishes = [i.strip() for i in dishes]
unique_dishes = set(dishes)

dict1 = {}
for i in unique_dishes:
    dict1[i] = dishes.count(i)
dict1

plt.figure()
index = np.arange(len(dict1))
plt.bar(index,list(dict1.values()))
plt.xlabel('Dishes', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.xticks(index, dict1.keys(), fontsize=5,rotation=90)
plt.title('Popularity of dishes')
plt.show()

df = pd.DataFrame.from_dict(dict1, orient = 'index' )
df.columns = ['Count']
df.head()

df.sort_values('Count',inplace=True,ascending=False)
df[:20]