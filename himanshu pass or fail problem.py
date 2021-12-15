name=input("enter your name")
maths=float(input("enter maths marks"))
english=float(input("enter english marks"))
science=float(input("enter science marks"))
IT=float(input("enter IT marks"))
a=(maths+science+english+IT)/200*100
print(a)
if a>65:
    print('pass')
else:
    print('fail')
