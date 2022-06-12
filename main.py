
x = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def grid():
    print("---------")
    print(f"| {x[0][0]} {x[0][1]} {x[0][2]} |")
    print(f"| {x[1][0]} {x[1][1]} {x[1][2]} |")
    print(f"| {x[2][0]} {x[2][1]} {x[2][2]} |")
    print("---------")
grid()
key = True
index = 0
while index < 9:

    if key:
        text = input("Enter the coordinates: ")
        n = [x for x in text.split() if x.isalpha()]
        if len(n) > 0:
            print("You should enter numbers!")
            continue
        else:
            coord1,coord2 = text.split()
            coord1,coord2 = int(coord1),int(coord2) 
      
        
            if coord1 > 3 or coord2 > 3 or coord1 <= 0 or coord2 <= 0:
                print("Coordinates should be from 1 to 3!")
                continue
            elif x[coord1 - 1][coord2 - 1] == " ":
                x[coord1 - 1][coord2 - 1] = "X"
                grid()
                index += 1
        
            else:
                print("This cell is occupied! Choose another one!")
                continue
    key = True   
     

    if (x[0][0] == x[0][1] == x[0][2] and x[0][0] != ' ') or (x[1][0] == x[1][1] == x[1][2] and x[1][1] != ' ') or (x[2][0] == x[2][1] == x[2][2] and x[2][2] != ' ') or (x[0][0] == x[1][0] == x[2][0] and x[0][0] != ' ') or (x[0][1] == x[1][1] == x[2][1] and x[2][1] != ' ') or (x[0][2] == x[1][2] == x[2][2] and x[2][2] != ' ') or (x[0][0] == x[1][1] == x[2][2] and x[0][0] != ' ') or (x[0][2] == x[1][1] == x[2][0] and x[1][1] != ' '):
        print("X wins")
        quit()
    if index == 9:
        continue
    
    text = input("Enter the coordinates: ")
    n = [x for x in text.split() if x.isalpha()]
    if len(n) > 0:
        print("You should enter numbers!")
        key = False
    else:
        coord1,coord2 = text.split()
        coord1,coord2 = int(coord1),int(coord2) 
    
        
        if coord1 > 3 or coord2 > 3 or coord1 <= 0 or coord2 <= 0:
            print("Coordinates should be from 1 to 3!")
            key = False
        elif x[coord1 - 1][coord2 - 1] == " ":
            x[coord1 - 1][coord2 - 1] = "O"
            grid()
            index += 1
        else:
            print("This cell is occupied! Choose another one!")
            key = False
    if (x[0][0] == x[0][1] == x[0][2] and x[0][0] != ' ') or (x[1][0] == x[1][1] == x[1][2] and x[1][1] != ' ') or (x[2][0] == x[2][1] == x[2][2] and x[2][2] != ' ') or (x[0][0] == x[1][0] == x[2][0] and x[0][0] != ' ') or (x[0][1] == x[1][1] == x[2][1] and x[2][1] != ' ') or (x[0][2] == x[1][2] == x[2][2] and x[2][2] != ' ') or (x[0][0] == x[1][1] == x[2][2] and x[0][0] != ' ') or (x[0][2] == x[1][1] == x[2][0] and x[1][1] != ' '):
        print("O wins")
        quit()
print("Draw")