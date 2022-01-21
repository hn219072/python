#square and square root in tupples
tup=(1,2,3,4)
for i in tup:
    print("the square of the element",i,"is",i*i)
    print("the square root of element",i,"is",(i)**1/2)





    
#modulus function in tupples
t=(2,4,6,8,10)
t2=(1,3,5,7,9)
for i in range(len(t)):
        print("modulous of element of tuple with tuple 2 is",t[i]%t2[i])
