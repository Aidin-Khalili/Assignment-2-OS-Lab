import random
from os import system

n = abs(int(input("Please enter the max number(upper than zero) : ")))
while n == 0 :
    n = abs(int(input("Please enter the max number(upper than zero) again : ")))
situation = ["Forside","Backside"]
players = ["user","computer-1","computer-2"]
choice_player = [0,0,0]
scoures = [0,0,0]
while n not in scoures:
    system('clear')
    print('')
    print('1. Your scoure : ',scoures[0],'\n2. computer-1 scoure : ',scoures[1],'\n3. computer-2 scoure : ',scoures[2],'\n')

    choice_player[0] = int(input("palam polom pilich (say \'0\' for Forside or \'1\' for Backside):"))
    while choice_player[0] != 0 and choice_player[0] != 1:
        choice_player[0] = int(input("palam polom pilich (Enter \'0\' for Forside or \'1\' for Backside) again : "))
    choice_player[1] = random.choice([0,1])
    choice_player[2] = random.choice([0,1])
    print(situation[choice_player[0]],situation[choice_player[1]],situation[choice_player[2]])
    sum = choice_player[0] + choice_player[1] + choice_player[2]
    if(sum == 0 or sum == 3):
        print("Draw")
    elif(sum == 1):
        for i in range(len(choice_player)):
            if(choice_player[i] == 1):
                print("Player",players[i]," wins !")
                scoures[i] += 1
                break
    elif(sum == 2):
        for i in range(len(choice_player)):
            if(choice_player[i] == 0):
                print("Player",players[i]," wins !")
                scoures[i] += 1
                break
print("So the final scoures are : \n")
for i in range(len(choice_player)):
    print("Player",players[i]," is : ",scoures[i],"\n")
print("So player",players[scoures.index(max(scoures))],'win')
