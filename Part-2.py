from random import randint
scoures = [0,0]
n = abs(int(input("Please enter the max score(upper than zero) : ")))
while n == 0 :
    n = abs(int(input("Please enter the max score(upper than zero) again : ")))
while n not in scoures:
    print('1. Your scoure : ',scoures[0],'\n2. computer scoure : ',scoures[1])
    user_choice = int(input('Enter your Choice:\n1. Rock \t 2. Paper \t 3. Scissor \t'))
    computer_choice = randint(1,3)
    if user_choice == computer_choice:
        print('Tie!')
    elif user_choice == 1:
        if computer_choice == 2:
            print('Computer Wins!')
            scoures[1] += 1
        else:
            print('You Win!')
            scoures[0] += 1
    elif user_choice == 2:
        if computer_choice == 3:
            print('Computer Wins!')
            scoures[1] += 1
        else:
            print('You Win!')
            scoures[0] += 1
    elif user_choice == 3:
        if computer_choice == 1:
            print('Computer Wins!')
            scoures[1] += 1
        else:
            print('You Win!')
            scoures[0] += 1
print('The final score is : you are : ' ,scoures[0] ,' computer scoure : ',scoures[1] )
if(scoures[0] > scoures[1]):
    print('You wiiiiin !')
else: print('You lose !')