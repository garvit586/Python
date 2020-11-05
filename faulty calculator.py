print("enter the following operator")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
a = input()
print("enter the first digit")
b = int(input())
print("enter the second digit")
c = int(input())
if a == "+" :
    if b== 56 and c==9:
        print(77)
    else:
        print("sum =",b+c)
elif a == "-":
    print("substraction =",b-c)
elif a == "*":
    if b==45 and c==3:
        print(555)
    else:
        print("muliplicatrion =",b*c)
else:
    if b==56 and c==6:
        print(4)
    else:
        print("division =",b/c)