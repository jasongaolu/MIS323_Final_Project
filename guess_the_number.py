
from random import randint

player_score = 0
comp_score = 0
total_score = player_score + comp_score
sample = 0
sample2 = 0
sample3 = 0

def choice(starting, ending):
    rand_num = randint(starting,ending)
    return rand_num

version = int(input('Hello, which version would you like to play? \nPress 1 for infinite amount of guesses and no score\nPress 2 for one guess per game\n'))

if version == 1:
    print(f'Okay you pressed {version}, for infinite amount of guesses per game and no score')
else:
    print(f'Okay you pressed {version}, for one guess per game')

games = input("Before we start\n If you would like to leave mid-game press 'q' during an input\nNow how many times do you want to play 'Guess the Number?': ")
try:
    val = float(games)
except ValueError as err:
    print("This is not a valid number, please re-run the program")
    quit()

print(f'Okay we will play it {games} times, lets start!')

while total_score != int(games):


    print(f'*****ROUND {total_score + 1} GO*****')
    a = input('what is the starting number?: ') 
    if a == 'q':
        break
    try:
        val = float(a)
    except ValueError as err:
        print("This is not a valid number, please re-run the program")
        quit()
    sample = float(a)

    b = input('what is the ending number?: ')
    if b == 'q':
        break
    try:
        val = float(b)
    except ValueError as err:
        print("This is not a valid number, please re-run the program")
        quit()
    sample2 = float(b)

    choice(sample,sample2)
    num = choice(sample,sample2)

    c = input('Okay, I generated a random number between those inputs, try to guess: ')
    if c == 'q':
        break
    try:
        val = float(c)
    except ValueError as err:
        print("This is not a valid number, please re-run the program")
        quit()
    sample3 = float(c)

    if version == 1:
        while sample3 != num:
            if sample3 > num:
                print('Thats too high')
                sample3 = float(input('Try again: '))
            elif sample3 < num:
                print('Thats too low')
                sample3 = float(input('Try again: '))
        if sample3 == num:
            print('Thats correct!')
        total_score += 1


    if version == 2:
        if sample3 > num:
            print(f'Oh too high! The number was {num} and you guess {c}')
            comp_score += 1
        elif sample3 < num:
            print(f'Oh dang too low, the number was {num} and you guessed {c}')
            comp_score += 1
        else:
            print('That number is correct! Yay')
            player_score += 1
        print(f'The current score is \n Player: {player_score} \n Computer: {comp_score}')
        total_score = player_score + comp_score

print("Thanks for playing 'Guess that Number', We hope to see you soon!")