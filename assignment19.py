import numpy as np
import math

#Q1
a=np.random.random((1,10))
print (a)
print(np.mean(a))

#Q2
b=np.random.random((20,1))
print(b)
print(np.var(a))
print(np.std(a))

#Q3
a=np.random.random((10,20))
b=np.random.random((20,25))
c=np.matmul(a,b)
print(c)
d=np.sum(c)
print(c.shape)
print(d)

#Q4
a=np.random.random((10,1))
print(a)
i=0
l=[]
for i in range(0,10):
    b=1/(1+math.exp(-(x[i,0])))
    l.append(b)
print("f(x) ->")
print(l)