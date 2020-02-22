# Creating graphs with PyPlot - Homework

## Task 1
```.py
import matplotlib.pyplot as plt

x = [-2 + 0.004 * i for i in range(1001)]

y = [(i+1)**2 - 1 for i in x]

plt.plot(x,y)

plt.xlabel("x")
plt.ylabel("$f(x)=(x+1)^2-1$")

plt.show()
```
#### Graf:
![graf1](HWgraph1.png)

## HL Task
```.py
import matplotlib.pyplot as plt
from math import sin

x = [0.05 * i for i in range(601)]

m = [i**2 for i in x]

g = [0.1*sin(0.1*i) for i in m]

plt.plot(x,g)

plt.xlabel("x")
plt.ylabel("$g(x)=0.1 * sin(0.1 * m(x))$")

plt.show()
```
#### Graf:
![graf2](HWgraphHL.png)



