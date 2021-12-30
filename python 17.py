#for loop
list1=[1,2,3,4,5]
for i in range(len(list1)):
    print(list1[i])
    
#while lopp
list2=[1,2,3,4,5]
i=0
while i<len(list2):
    print(list1[i])
    i=i+1
#creating list for items containing a specific alphabet
list1=["apple","banana","kiwi","mango"]
a=[]
for i in list1:
    if "a" in i:
        a.append(i)
        print(a)
#crerating list ......specific item method 2
list1=["apple","banana","kiwi","mango"]      
new=[x for x in list1 if "a" in x ]
print(new)

        
