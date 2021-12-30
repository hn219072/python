#exist or not
a=["mango","cherry","melon","apple"]
n= input("enter your item which you want to check:")
if n in a:
   print("exist")
else:
 print("not exist")
#indexing method
a[0]=a[2]
#changing an item with other
a[3]="grapes"
print(a)
#removing an item
b=input()
a.remove(b)
print(a)
