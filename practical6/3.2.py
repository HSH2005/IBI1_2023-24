import numpy as np
import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7]
uk_cities.sort()
cn_cities=[0.58,8.4,22.2,29.9]
cn_cities.sort()
uk_list=['string','ediinburgh','glasgow','london']
cn_list=['haining','hangzhou','beijing','shanghai']
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.bar(uk_list,uk_cities,color=['b'],width=0.5,hatch='\\')
for a,b,i in zip(cn_list,cn_cities,range(len(uk_list))):
    plt.text(a,b+0.03,"%.2f"%uk_cities[i],ha='center',fontsize=10)
plt.title('UK')
plt.ylabel('population/million')
plt.xlabel('cities')

plt.subplot(1,2,2)
plt.bar(cn_list,cn_cities,cplpr=['r'],width=0.5,hatch='/')
for a,b,i in zip(cn_list,cn_cities,range(len(cn_list))):
    plt.text(a,b+0.03,"%.2f"%uk_cities[i],ha='center',fontsize=10)
plt.title('China')
plt.ylabel('population/million')
plt.xlabel('cities')
plt.show
plt.clf
