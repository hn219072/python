n=int(input("no of rows"))
m=int(input("no. of columns"))
import numpy as np
arr=np.empty([n,m],dtype=int )
for i in range(n):
    for j in range(m):
        arr[i][j]=int(input())
print(arr[:,0])
print(arr[:,1])
print(arr[:,2])

