a=input("do you want to play this game:yes or no:")
if(a=="yes"): 
    print("enter the quiz")
    print("choose any of the following topics:")
    print("1.sports")
    print("2. video game")
    enter_topic=int(input("choose one option"))
    if(enter_topic==1):
     print("question. how many maximum in field players are allowed in cricket")
     print("1. 10")
     print("2. 9")
     print("3. 11")
    b=int(input("choose your answer"))
    if (b==3):
        point1=10
        print("correct",point1)
    else:
        point1=-10
        print("incorrect",point1)
    print("question. most popular game among youth") 
    print("1. free fire")
    print("2.bgmi")
    print("3.cod")
    c=int(input("choose answer"))
    if (c==2):
        point2=10
        print("correct",point2)
    else:
        point2=-10
        print("incorrect",point2)
    print("question. colour of indian cricket jersey")
    print("1.blue")
    print("2.black")
    print("3. pink")
    d=int(input("choose answer"))
    if (d==1):
          point3=10
          print("correct",point3)
    else:
        point3=-10
        print("incorrect",point3)
    total=point1+point2+point3
    print("=====you score",total,"out of 30====")
        
else:
    print("good bye") 
