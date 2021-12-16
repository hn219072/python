print("welcome to bank")
print("1.withdraw money,2.update password")
a=int(input())
if (a==1):
    print("enter amount withdrawn")
    b=int(input())
    print("collect your money",b)
    print("do you want to check total balance")
    e=input("yes/no")
    if(e=="yes"):
        total_amt=340000
        balance=total_amt-b
        print(balance)
    if(e=="no"):
        print("bye bye")
if (a==2):
    print("enter your current password")
    c=2345
    d=int(input())
    if (c==d):
        print("password match")
    else:
        print("password does not match")
else:
    print("exit")
