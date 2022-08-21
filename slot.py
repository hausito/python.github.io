import random
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

current_balance = 10000

bet = 100

key = True

key_spin = True

list_1 = []


container = {
    '  7  ': 1,
    '  8  ': 2,
    '  9  ': 3,
    '  10 ': 4,
    '  J  ': 5,
    '  Q  ': 10,
    '  K  ': 20,
    '  A  ': 50,
    'BONUS': 100

}

container2 = {
    '  7  ': Fore.GREEN + Fore.CYAN,
    '  8  ': Fore.BLUE,
    '  9  ': Fore.RED,
    '  10 ': Fore.YELLOW,
    '  J  ': Fore.GREEN,
    '  Q  ': Fore.CYAN,
    '  K  ': Fore.WHITE,
    '  A  ': Fore.MAGENTA,
    'BONUS': Back.CYAN,

}





def random_slot():
    new_list = list(container.keys())
    new_list_2 = []
    bonus_number = 0
    for i in range(9):
        new_item = random.choice(new_list)
        new_list_2.append(new_item)
        if new_item == "BONUS":
            bonus_number += 1
            if bonus_number == 3:
                del new_list[-1]
                bonus_number = 0
    return new_list_2
        


def print_dates():
    print(Fore.BLUE + "\nCurrent Ballance: ",current_balance,"$")
    print("\nBet: ",bet,"$")
    if key_spin:
        print("Normal Spin\n")
    else:
        print("Turbo Spin\n")
    print(Fore.RED + '''
    Click Enter for SPIN
    Print B for changing bet
    Print I for Info
    Print T for changing Spin Mode
    ''')


  





def show_image():
    global current_balance
    global list_1
    list_1 = random_slot()
    if key_spin:
        print("-----------------")
        print(container2[list_1[0]] + list_1[0], end = " ")
        time.sleep(0.1)
        print(container2[list_1[1]] + list_1[1], end = " ")
        time.sleep(0.1)
        print(container2[list_1[2]] + list_1[2])
        time.sleep(0.1)
        print(container2[list_1[3]] + list_1[3], end = " ")
        time.sleep(0.1)
        print(container2[list_1[4]] + list_1[4], end = " ")
        time.sleep(0.1)
        print(container2[list_1[5]] + list_1[5])
        time.sleep(0.1)
        print(container2[list_1[6]] + list_1[6], end = " ")
        time.sleep(0.1)
        print(container2[list_1[7]] + list_1[7], end = " ")
        time.sleep(0.1)
        print(container2[list_1[8]] + list_1[8])
        print("-----------------")
    else:
        print("-----------------")
        print(container2[list_1[0]] + list_1[0], container2[list_1[1]] + list_1[1], container2[list_1[2]] + list_1[2])
        print(container2[list_1[3]] + list_1[3], container2[list_1[4]] + list_1[4], container2[list_1[5]] + list_1[5])
        print(container2[list_1[6]] + list_1[6], container2[list_1[7]] + list_1[7], container2[list_1[8]] + list_1[8])
        print("-----------------")

    current_balance = current_balance - bet

def change_bet():
    global bet
    print("Input your Bet: ")
    new_bet = int(input())
    if new_bet <= current_balance:
        bet = new_bet
        
    else:
        print("Error")

def info():
    print("\nWelcome to a demo version of Casino Slot made by hausito ))")
    print("The symbols plays only on lines and diagonals.")
    print("**the results are based on your bet**")
    print("    Lines                  Diagonals    ")
    print("3x   7   =", bet * 1 * 0.5,"$","          ", "3x   7   =",bet * 1 * 0.25,"$")
    print("3x   8   =", bet * 2 * 0.5,"$","          ", "3x   8   =",bet * 2 * 0.25,"$")
    print("3x   9   =", bet * 3 * 0.5,"$","         ", "3x   9   =",bet * 3 * 0.25,"$")
    print("3x   10  =", bet * 4 * 0.5,"$","         ","3x  10   =",bet * 4 * 0.25,"$")
    print("3x   J   =", bet * 5 * 0.5,"$","          ", "3x   J   =",bet * 5 * 0.25,"$")
    print("3x   Q   =", bet * 10 * 0.5,"$","          ", "3x   Q   =",bet * 10 * 0.25,"$")
    print("3x   K   =", bet * 20 * 0.5,"$","         ", "3x   K   =",bet * 20 * 0.25,"$")
    print("3x   A   =", bet * 50 * 0.5,"$","         ", "3x   A   =",bet * 50 * 0.25,"$")
    print("3x Bonus =", bet * 100 * 0.5,"$","         ", "3x Bonus =",bet * 100 * 0.25,"$")
    
def turbo_spin():
    global key_spin
    key_spin = not(key_spin)    

def option():
    answer = input()
    if answer == "":
        show_image()
        win()
    elif answer == "B":
        change_bet()
    elif answer == 'I':
        info()
    elif answer == 'T':
        turbo_spin()
    else:
        print("Error")

def verify_bal():
    if current_balance < 0:
        exit() 

def win():
    global current_balance
    sum = 0
    if list_1[0] == list_1[1] and list_1[1] == list_1[2]:
            sum += container[list_1[0]] * bet * 0.5
    if list_1[3] == list_1[4] and list_1[4] == list_1[5]:
            sum += container[list_1[3]] * bet * 0.5
    if list_1[6] == list_1[7] and list_1[7] == list_1[8]:
            sum += container[list_1[6]] * bet * 0.5
    if list_1[0] == list_1[4] and list_1[4] == list_1[8]:
            sum += container[list_1[0]] * bet * 0.25
    if list_1[2] == list_1[4] and list_1[4] == list_1[6]:
            sum += container[list_1[2]] * bet * 0.25
    print("You won: ",sum,"$")
    current_balance += sum

while key:
    print_dates()
    option()
    verify_bal()

print("Thanks for playing ))")
print("Recharge your balance !")
    
    
    
    

