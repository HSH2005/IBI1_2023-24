import numpy as np
import matplotlib . pyplot as plt
#get some data for next step
beta = 0.3
gamma = 0.05
n = []
b = []
g = []
aa = 1
cc = 0
ccc = 0
aaa = 1
N = 10000
t = 0
#get the data 
while t < 1000:
    n.append(N)
    b.append(aaa)
    g.append(ccc)
    beta1 = beta * aaa / 10000
    Z = np.random.choice(range(2),N,p=[beta1,1-beta1])#affected
    a = list(Z)
    aa = a.count(0)
    Y = np.random.choice(range(2),aaa,p=[gamma,1-gamma])#recover
    c = list(Y)
    cc = c.count(0)
    N = N - aa
    aa = aa - cc
    aaa = aaa + aa
    ccc = ccc + cc
    t = t+1
print(n)
print(b)
print(g)
#draw pictures
line1 =plt.plot(n,label = 'susceptitble')
line2 =plt.plot(b,label = 'infected')
line3 =plt.plot(g,label = 'recovered')
plt.xlabel('time')
plt.ylabel('number')
plt.title("SIR model")
plt.legend()
plt.show()