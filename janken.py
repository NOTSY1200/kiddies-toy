import random

win = 0
same = 0
lose = 0

message1 = "you win"
message2 = "you lose"
message3 = "same"

def myhands():
    print("please,input")
    my = input("rock, scissors, paper: ")
    
    if my == "rock":
        my = 0
    elif my == "scissors":
        my = 1
    elif my == "paper":
        my = 2
    else:
        print("error!")
        return 
    
    return int(my)

def enemyhands():
    Enemy = random.randint(0,2)
    return Enemy

def battle(My, Ene):
    if My ==0:
        if Ene ==0:
                print(message3)
                result = 1
                return result
            
        elif Ene == 1:
                print(message1)
                result = 0
                return result
            
        elif Ene == 2:
                print(message2)
                result = 2
                return result
            
    elif My == 1:
        if Ene == 0:
            print(message2)
            result = 2
            return result
        
        elif Ene == 1:
            print(message3)
            result = 1
            return result
        
        elif Ene == 2:
            print(message1)
            result = 0
            return result
            
    elif My == 2:
        if Ene ==0:
            print(message1)
            result = 0
            return result
        
        elif Ene == 1:
            print(message2)
            result = 2
            return result
        
        elif Ene == 2:
            print(message3)
            result = 1
            return result
        
    else:
        print("error?")
        return 
        
print("rock,scissors,paper")

while(1):
    My = myhands()
    Ene = enemyhands()
    result = battle(My, Ene)
    if int(result) == 1:
        same += 1
    elif int(result) == 0:
        win += 1
    elif int(result) == 2:
        lose += 1
    
    print("win: ", win)
    print("same: ", same)
    print("lose", lose)
    
    