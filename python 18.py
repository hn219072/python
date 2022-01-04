#find sum and average
list=[1,30,20,10]
count=0
for i in list:
    count=i+count
print(count)
average=(count/len(list))                         
print(average)

#find smallest no. in list
list1=[1,10,20,30]
a=list1[0]
for i in list1:
    if i<a:
        a=i
print("smallest no.in list",a)
#find largest no.
list1=[1,10,20,30]
max1=list1[0]
a=list1.index(list1)
for i in list1:
    if i > list1:
        max1=list1[i]
        a=i
print("largest value is",max1)
print(a+1)
     
