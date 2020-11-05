def is_leap(year):
    leap = False
    Leap = True
    if (year%400 == 0):
        return Leap
    elif (year%100 == 0):
        return leap
    elif (year%4 == 0):
        return Leap
    else:
        return leap
a = int(input("enter the year : "))
print(is_leap(a))
