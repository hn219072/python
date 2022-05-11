def find(a,x,i):
    if x==a[i]:
        return i
    elif i<len(a)-1:
        return find(a,x,i+1)
    else:
        print("element not found")
        return-1

n=int(input("enter the size of array"))

arr=[]
print("enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))

print("enter the element whose index to be found:")
x=int(input())

count=0
y=find(arr,x,count)

print(y)
