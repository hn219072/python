#multiplication of elements in list
list1=[1,2,3,4,5,6,7,8]
count=1
for i in list1:
    count=count*i
print(count)


#reverse of a list
list1=[1,20,30,40,50]
newlist=list1[::-1]
print(newlist)



#positive elements of list
list1=[-1,20,30,40]
for i in list1:
    if i>0:
         print(i,end=" ")


         
#negetive elements of list
list1=[-1,-20,30,40,50]  
for i in list1:
    if i<0:
         print(i,end=" ")
    
    
 #both positve and negetive
    list1=[12,7,-9,-3,4,5]
mylist=[]
mylist1=[]

for num in list1:
  if num<0:
    mylist.append(num)
  else:
    mylist1.append(num)
print("positive numbers",mylist1)
print("negative numbers",mylist)     

    
