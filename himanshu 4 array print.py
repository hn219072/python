#import array
arr=[ [1, 2, 3 ] , [4, 5, 6 ] , [1, 2, 3] ]
for i in arr:
    for j in i:
        print(j,end=" ")
    print()


    import array as a
arr=a.array("i")
n=9
for i in range(0,n):
    arr.append(int(input()))


print(arr)

n_row=2
#display in row and column
for i in range(0,len(arr)):
  if i%((len(arr))/n_row)==0:
               print()
               print(arr[i], end=" ")
