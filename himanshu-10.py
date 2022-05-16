def towerofhanoi(n,s_pole,d_pole,i_pole):
    if n==1:
        print("move disc 1 from pole ",s_pole,"to pole",d_pole)
        return
    towerofhanoi(n-1,s_pole,i_pole,d_pole)
    print("move disc", n," from pole ",s_pole,"to pole",d_pole)
    towerofhanoi(n-1,s_pole,i_pole,d_pole) 
n=3
print(towerofhanoi(n,'A','C','B'))  
    #A,B,C are the names of poles
