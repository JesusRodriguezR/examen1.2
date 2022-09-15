import numpy as np
import math
from matplotlib import pyplot as plt
from scipy import stats
import statistics
data = np.loadtxt ("estatura.txt",dtype=float)
#print (data)
x = np.array(data[:])
clases =  28
rango = (50,190)
plt.figure(1)
plt.title("histograma")
plt.xlabel("clases")
plt.hist(x, range = rango, bins = clases, density = False)
(n,bins,patches)=plt.hist(x, range = rango, bins = clases, density = False)
res = stats.relfreq(x, numbins = clases,defaultreallimits = (50,190))
print(bins)
plt.figure(2)

bins = (bins[1:] + bins[:-1]) / 2
plt.title("Diagrama de frecuencias relativas")
plt.xlabel("Clases")
plt.bar(bins,res.frequency)
print(bins)

E=0
for i in range(0,clases):
	E += bins[i]*res.frequency[i]
print("E(x)",E)
print("Media aritmetica: ",sum(x)/len(x))
V = 0
for i in range(0,clases):
	V += (bins[i]-E)**2*res.frequency[i]
print("V(X)",V)
s = math.sqrt(V)
print ("s : ",s)
print("sp :", statistics.stdev(x))

x = np.linspace(E - 3*s, E + 3*s, 100)
plt.plot(x, stats.norm.pdf(x, E, s))

plt.show()

#estatura: media: 167.298 desviacion estandar: 13.082
#calzado: media: 25.75 desviacion estandar: 1.843