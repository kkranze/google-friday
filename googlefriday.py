import random

print ("1 is wide reciever, 2 is tackle, 3 is guard, 4 is guard, 5 is tackle, 6 is tight end, 7 is wr, 8 is qb, 9 is fb, 10 is hb, 11 center")
min = 1
max = 11

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("choosing positions...")
    print ("The psitions are....")
    number1 = random.randint(min, max)
    number2 = random.randint(min,number1, max)
    print (number1)
    print (number2)
    roll_again = input("choose new positions?")
