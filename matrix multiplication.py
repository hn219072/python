#matrix multiplication
n=int(input())
m=int(input())

import numpy as np

arr1=np.array([n,m], dtype=int)
arr2=np.array([n,m ],dtype=int)
c=np.empty([n,m],dtype=int)

for i in range(n):
    for j in range(m):
        arr1[i][j]=int(input())

for i in range(n):
    for j in range(m):
        arr2[i][j]=int(input())

for i in range(n):
    for j in range(m):
        c[i][j]=0
        for k in range(n):
            c[i][j]=c[i][j]+arr1[i][j]*arr2[k][j]


print(c)
