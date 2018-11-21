import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bill = pd.read_csv("/Users/anushka/Desktop/Decision Science - Intern/Customer Bill Detail.csv")
bill.head()

bill.drop(labels = ['Date','Bill Number','Discount','Subtotal','Delivery Amt', 'Channel'], axis=1, inplace=True)
bill.head()

p = bill['Total Bill'].values
print(len(p))
p.sort()
p

plt.figure()
def histedges_equalN(x, nbin):
    npt = len(x)
    return np.interp(np.linspace(0, npt, nbin + 1),
                     np.arange(npt),
                     np.sort(x))


n, bins, patches = plt.hist(p, histedges_equalN(p, 20))
plt.xlabel('Price range')
plt.ylabel('No. of customers')
plt.title('Distribution with equal no. of customers in each bin')

plt.figure()
plt.hist(p, bins=20)
plt.xlabel('Price range')
plt.ylabel('No. of customers')
plt.title('Distribution with equal sized bins (no. of bins=20)')