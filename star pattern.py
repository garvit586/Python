n = 5
print("enter the value")
b = int(input())
c = bool(b)
if c == 1:
    for x in range(n):
        for y in range(x + 1):
            print("*", end=" ")
        print(" ")
else:
    for x in range(n+1,0,-1):
        for y in range(0,x-1):
            print("*", end=" ")
        print("\r")
