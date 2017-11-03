num1 = input("enter a number")
num1 = int(num1)


secret = 21


if(num1 > secret):
    print("too high")
    num1 =input ("enter a number")
    num1 = int(num1)
    if(num1 >secret):
        print("too high")
    elif(num1 < secret):
        print("too low")
    else:
        print("you got it")
elif(num1 < secret):
    print("too low")
else:
    print("you got it")
