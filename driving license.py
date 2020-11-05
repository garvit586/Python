print("enter your age")
age = int(input())
if age > 7 and age < 100:
    if age < 18:
        print("you can't drive")
    elif age == 18:
        print("we will think about you")
    else :
        print("you can drive")
else:
    print(" you enter invalid number")
