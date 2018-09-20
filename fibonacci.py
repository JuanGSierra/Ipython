import time
import matplotlib.pyplot as plt

fibonacci=[]
x=0
y=1
xarray=[]
yarray=[]
num = int(input("Numero de elementos:"))

start_time = time.time()
for n in range(num):
    yarray.append(x+y)
    xarray.append(time.time() - start_time)
    fibonacci.append(x+y)
    aux = x + y
    x = y
    y = aux
print(fibonacci)
fig = plt.figure()
print(xarray)
print(yarray)
plt.plot(xarray,yarray)
fig.savefig("grafico.png")



