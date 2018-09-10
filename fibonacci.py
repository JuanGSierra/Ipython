import time
import matplotlib.pyplot as plt
import numpy as np

t0 = time.clock()
lista = np.array([])
def fibonacci(n):
    if n==1 or n==2:
        return 1
        np.hstack((lista,time.clock()))
    return fibonacci(n-1)+fibonacci(n-2)

print (fibonacci(int(input("Fibonacci: "))))
print (time.clock()-t0)
plt.plot(lista)
plt.show()