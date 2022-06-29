import random

print("H A N G M A N  animals\n")

container = ("dog","turtle","rabbit", "cat","goldfish","mouse", "hamster","parrot","cow", "duck","pig","goat", "deer","bee","sheep", "fish","turkey","chicken", "horse")
msg_0 = "No improvements.\n"
msg_1 = "That letter doesn\'t appear in the word."
msg_2 = "You guessed the word!"
msg_3 = "You survived!"
msg_4 = "You lost!"
answer = ""
answer_1 = ""
index = 0
list_1 = []


def choice():
    global answer
    answer = random.choice(container)

def reset():
    global list_1
    for i in range(len(answer)):
        list_1.append('-')
def Convert():
    global answer_1
    answer_1 = ''.join(list_1)
   
def change():
    global list_1
    for i in range(len(list_1)):
        if list_1[i] == "-":
            if answer[i] == user_answer:
                list_1[i] = user_answer
            else:
                list_1[i] = '-'
        elif list_1[i] == user_answer:
            print(msg_0)
def win_lose():
    if '-' not in answer_1:
        print(msg_2)
        print(msg_3)
        exit()
def level():
    print("Choose level: easy, medium, hard")
    _level_ = input()
    if _level_ == "easy":
        return 20
    elif _level_ == "medium":
        return 15
    elif _level_ == "hard":
        return 10
    else:
        print("choose right level !")
        level()
choice()
set_1 = set(answer)
reset()
Convert()
print(f'{answer_1}\n')
index = level()

while index > 0:
    
    win_lose()
    index -= 1
    
    user_answer = input("Input a letter:")
    print(f'{index} attempts left')
    
    if user_answer in set_1:
        change()
        
    else:
        print(msg_1)
    Convert()
    print(f'{answer_1}\n')
print(msg_4)
exit()
