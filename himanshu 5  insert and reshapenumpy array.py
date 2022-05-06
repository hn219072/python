#insert and reshape numpy array
import numpy as np
arr=np.full((3,2),1)
print(arr)
print(arr.shape)
print("enter the values")
for i in range(0,arr.shape[0]):
    for j in range(0,arr.shape[1]):
        arr[i][j]= int(input())


print(arr)
#for reshape
a=arr.reshape(2,3)
print(a)
