import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# start = play()

print('\nNew Game\n')

PlayerChoice = input('Enter: \n1 for Rock \n2 for Paper\n3 for Scissors\n\n')

Player =int(PlayerChoice)

if Player < 1 or Player > 3: 
    sys.exit('enter a value of 1, 2, or 3 ONLY.')

Computer = random.choice('123')

ComputerInt = int(Computer)
# print('')
# print('You Chose ' + PlayerChoice + '.')
# print('Computer Chose ' + Computer + '.')
# print('')

if Player == 1:
    PlayerPick = 'Rock'
if Player == 2:
    PlayerPick = 'Paper'
if Player == 3:
    PlayerPick = 'Scissors'

if ComputerInt == 1:
    ComputerPick = 'Rock'
if ComputerInt == 2:
    ComputerPick = 'Paper'
if ComputerInt == 3:
    ComputerPick = 'Scissors'

print('')
print('You Chose ' + str(RPS(Player)) + '.')
print('Computer Chose ' + str(RPS(ComputerInt)) + '.')
print('')

if Player == 1 and ComputerInt ==3:
    print('You Win!')
elif Player == 2 and ComputerInt ==1:
     print('You Win!')
elif Player == 3 and ComputerInt ==2:
     print('You Win!')
elif Player == ComputerInt:
    print('You Tied')
else:
    print('You Lose :(')


#Loop Attempt

# replay = input('Play Again? \nYES to Play Again\nNO to Quit')
# trimplay = replay.strip().upper

# if trimplay == 'YES':
#     start
# else:
#     print('Thanks for Playing!')

# #Rock Scenarios
# if Player == 1 and ComputerInt == 1:
#     print('Tie! Play Again!')
# if Player == 1 and ComputerInt == 2:
#     print('You Lose! Paper Beats Rock!')
# if Player == 1 and ComputerInt == 3:
#     print('You Win! Rock Beats Paper!')               MY CODING COMMENTED OUT

# #Paper Scenarios
# if Player == 2 and ComputerInt == 1:
#     print('You Win! Paper Beats Rock!')
# if Player == 2 and ComputerInt == 2:
#     print('Tie! Play Again!')
# if Player == 2 and ComputerInt == 3:
#     print('You Lose! Scissors Beats Paper!')

# #Scissors Scenarios
# if Player == 3 and ComputerInt == 1:
#     print('You Lose! Rock Beats Scissors!')
# if Player == 3 and ComputerInt == 2:
#     print('You Win! Scissors Beats Paper!')
# if Player == 3 and ComputerInt == 3:
#     print('Tie! Play Again!')

# print('\n\n')

