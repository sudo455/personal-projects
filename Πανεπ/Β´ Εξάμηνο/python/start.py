print("menu\n")
print("1. for")
print("2. if elif else")
print("3. while")
print("4. exit")


flagcontinue = True
while flagcontinue:
    flag = True

    while flag:
        ans = int(input("give me [1,3]"))
        if (ans >= 1) and (ans <= 3):
            flag = False

    if ans == 1:
        print("for loop [1-10]")
        for i in range(1,11):
            print("i = " + str(i))
    elif ans == 2:
        ans = int(input("give me a int number: "))
        if ans % 2 == 0:
            print("einai artios")
        else:
            print("einai peritos")
    elif ans == 3:
        print("while loop [1-10]")
        i = 1
        while i <= 10:
            print("i = " + str(i))
            i+=1
    else:
        flagcontinue = False
