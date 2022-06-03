_key = True
number = 1

x = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


print("-------------")
print(x[0])
print(x[1])
print(x[2])
print("-------------")

while _key:

    if number > 9:
        print("Nobody wins")
        exit()
    _str = input("input coordinates: ")
    list2 = [g for g in _str.split(" ")]
    if list2[0] == "" or list2[1] == "":
        print("not inserted coordinates !")
        exit()

    a = int(list2[0])
    b = int(list2[1])

    number = number + 1

    if a == 1:
        if b == 1 and x[0][0] != "O" and x[0][0] != "X":
            x[0][0] = 'X'
        elif b == 2 and x[0][1] != "O" and x[0][1] != "X":
            x[0][1] = 'X'
        elif b == 3 and x[0][2] != "O" and x[0][2] != "X":
            x[0][2] = 'X'
        else:
            print("You can't ! X lose the game ")
            exit()
    elif a == 2:
        if b == 1 and x[1][0] != "O" and x[1][0] != "X":
            x[1][0] = 'X'
        elif b == 2 and x[1][1] != "O" and x[1][1] != "X":
            x[1][1] = 'X'
        elif b == 3 and x[1][2] != "O" and x[1][2] != "X":
            x[1][2] = 'X'
        else:
            print("You can't ! X lose the game ")
            exit()
    elif a == 3:
        if b == 1 and x[2][0] != "O" and x[2][0] != "X":
            x[2][0] = 'X'
        elif b == 2 and x[2][1] != "O" and x[2][1] != "X":
            x[2][1] = 'X'
        elif b == 3 and x[2][2] != "O" and x[2][2] != "X":
            x[2][2] = 'X'
        else:
            print("You can't ! X lose the game ")
            exit()
    else:
        print("You can't ! Input right coordinates")
        exit()

    print("-------------")
    print(x[0])
    print(x[1])
    print(x[2])
    print("-------------")

    if (x[0][0] == x[0][1] == x[0][2] and x[0][0] != '-') or (x[1][0] == x[1][1] == x[1][2] and x[1][1] != '-') or (x[2][0] == x[2][1] == x[2][2] and x[2][2] != '-') or (x[0][0] == x[1][0] == x[2][0] and x[0][0] != '-') or (x[0][1] == x[1][1] == x[
    2][1] and x[2][1] != '-') or (x[0][2] == x[1][2] == x[2][2] and x[2][2] != '-') or (x[0][0] == x[1][1] == x[2][2] and x[0][0] != '-') or (x[0][2] == x[1][1] == x[2][0] and x[1][1] != '-'):
        print("X win ))")
        quit()

    if number > 9:
        print("Nobody wins")
        exit()
    list3 = input("input coordinates: ")
    list4 = [h for h in list3.split(" ")]
    if list4[0] == "" or list4[1] == "":
        print("not inserted coordinates !")
        exit()
    a = int(list4[0])
    b = int(list4[1])
    if a == 1:
        if b == 1 and x[0][0] != "O" and x[0][0] != "X":
            x[0][0] = 'O'
        elif b == 2 and x[0][1] != "O" and x[0][1] != "X":
            x[0][1] = 'O'
        elif b == 3 and x[0][2] != "O" and x[0][2] != "X":
            x[0][2] = 'O'
        else:
            print("You can't ! O lose the game ")
            exit()
    elif a == 2:
        if b == 1 and x[1][0] != "O" and x[1][0] != "X":
            x[1][0] = 'O'
        elif b == 2 and x[1][1] != "O" and x[1][1] != "X":
            x[1][1] = 'O'
        elif b == 3 and x[1][2] != "O" and x[1][2] != "X":
            x[1][2] = 'O'
        else:
            print("You can't ! O lose the game ")
            exit()
    elif a == 3:
        if b == 1 and x[2][0] != "O" and x[2][0] != "X":
            x[2][0] = 'O'
        elif b == 2 and x[2][1] != "O" and x[2][1] != "X":
            x[2][1] = 'O'
        elif b == 3 and x[2][2] != "O" and x[2][2] != "X":
            x[2][2] = 'O'
        else:
            print("You can't ! O lose the game ")
            exit()
    else:
        print("You can't ! Input right coordinates")
        exit()
    print("-------------")
    print(x[0])
    print(x[1])
    print(x[2])
    print("-------------")
    if (x[0][0] == x[0][1] == x[0][2] and x[0][0] != '-') or (x[1][0] == x[1][1] == x[1][2] and x[1][1] != '-') or (x[2][0] == x[2][1] == x[2][2] and x[2][2] != '-') or (x[0][0] == x[1][0] == x[2][0] and x[0][0] != '-') or (x[0][1] == x[1][1] == x[
    2][1] and x[2][1] != '-') or (x[0][2] == x[1][2] == x[2][2] and x[2][2] != '-') or (x[0][0] == x[1][1] == x[2][2] and x[0][0] != '-') or (x[0][2] == x[1][1] == x[2][0] and x[1][1] != '-'):
        print("O win ))")
        quit()
    number = number + 1

