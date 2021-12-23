#first half
for i in range(3):
    for j in range(i+1):
        print("a",end=" ")
    print("\r")
#second half
for i in range(3,1,-1):
    for j in range(i-1):
        print("a",end=" ")
    print("\r")    
