import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os .chdir("/Users/heshenghao/Desktop")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.iloc[0:101:10,3]
A_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='Afganistan':
        A_index.append(True)
    else:
        A_index.append(False)
print(dalys_data.loc[A_index,"DALYs"])

CN_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='China':
        CN_index.append(True)
    else:
        CN_index.append(False)
china_data=dalys_data.loc[CN_index,:]
CN_mean_data=np.mean(china_data.loc[:,'DALYs'])
print(CN_mean_data)
#DALYs in China in 2019 (22270.51) was less than mean(30677.69)
plt.figure(1)
plt.plot(china_data.Year,china_data.DALYs,"b+")
plt.xticks(china_data.Year,rotation=-90)
UK_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='United Kingdom':
        UK_index.append(True)
    else:
        UK_index.append(False)
UK_data =dalys_data.loc[UK_index,:]
plt.figure(2)
plt.plot(UK_data.Year,UK_data.DALYs,"b+")
plt.xticks(UK_data.Year,rotation=-90)
plt.show()
plt.clf()