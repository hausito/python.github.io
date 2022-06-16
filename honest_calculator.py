msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"



msg_ = ["Are you sure? It is only one digit! (y / n)","Don't be silly! It's just one number! Add to the memory? (y / n)","Last chance! Do you really want to embarrass yourself? (y / n)"]
key = True
key_1 = True
key_2 = True


def is_one_digit(v):
    if v > -10 and v < 10 and (float(v) == int(v)):
        return True
    else:
        return False


def option():
    print(msg_5)
    answer = input()
    global key_3
   
    if answer == 'y':
        print(msg_0)
        key_3 = False
    if answer == 'n':
        exit()
def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '+' or v3 == '-' or v3 == '*'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
def memory_func():
    global msg_index
    global memory
    if is_one_digit(result):
        key_5 = True      
        while key_5:    
            if msg_index < 3:

                print(msg_[msg_index])
                answer4 = input()
            else:
                answer4 = 'y'
            if answer4 == 'y':
                
                if msg_index < 3:
                    msg_index += 1    
                else:
                    memory = float(result)
                    option()
                    key_5 = False
            elif answer4 == 'n':
                option()
                key_5 = False
            else:
                memory_func()
    else:
        memory = float(result)
        key_5 = False
        option()

    
    




memory = 0
print(msg_0)

while key:
    msg_index = 0
    mains = input()
    _list = [g for g in mains.split()]
    
    
    if _list[0] == 'M':
        x = memory
    else:
        try:
            x = int(_list[0])
       
        
        except ValueError:
            if key_1:
                for i in range(len(_list[0])):
                    if _list[0][i] == '.':
                        x = float(_list[0])
                        key_1 = False
                        break
            if key_1:
                print(msg_1)
                print(msg_0)
                continue
    
        
    if _list[2] == 'M':
        y = memory
    else:
        try:
       
            y = int(_list[2])
        
        except ValueError:
            if key_2:
         
        
                for i in range(len(_list[2])):
                    if _list[2][i] == '.':
                        y = float(_list[2])
                        key_2 = False
                        break
                    
                
            
            if key_2:
                print(msg_1)
                print(msg_0)
                continue
    
    if _list[1] == '+':
        oper = '+'
        
    elif _list[1] == '-':
        oper = '-'
        
    elif _list[1] == '*':
        oper = '*'
     
    elif _list[1] == '/':
        oper = '/'
       
    else:
        print(msg_2)
        print(msg_0)
        continue
    check(x,y,oper)
    if oper == "+":
        result = x + y
       
    elif oper == "-":
        result = x - y
       
    elif oper == "*":
        result = x * y
        
    elif oper == "/" and y != 0:
        result = x / y
        
    else:
        print(msg_3)
        print(msg_0)
        continue
    print(float(result))
  
    
    print(msg_4)
    answer1 = input()
    key_3 = True
    while key_3:
        if answer1 == 'y':
            memory_func()
            
               
            
        elif answer1 == 'n':
            option()
            
   

