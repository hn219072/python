#largest and second largest element
list1=[10,20,4,45,99]
largest=list1[0]
second_largest=list1[0]
for i in range(len(list1)):
    if list1[i]>largest:
        largest=list1[i]
for i in range(len(list1)):
    if (list1[i] > second_largest and list1[i]!=largest):
        second_largest = list1[i]
        print("largest value",largest)
        print("second largest value",second_largest)
#even/odd
a=[1,2,3,4,5,6,7]
even=0
odd=0
for i in a:
    if(i%2==0):
        even= even+1
    else:
        odd= odd+1
print(odd)
print(even)        
        
    
        
                    
