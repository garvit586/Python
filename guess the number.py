n = 18
numberofguesses = 5
for x in range(numberofguesses):
    x = x + 1
    m = int(input("enter the number : \n"))
    if m > n:
        print("you entered greater number")
    elif m < n:
        print("you entered smaller number")
    else:
        print("congrats!, you guess the right number")
        break
    if x == 5:
        print("!!!!!GAME OVER!!!!!")
        break
    print("only", numberofguesses - x, "chances are left")