import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    attempts = 0

    #player has 5 attempts maximum to guess the number
    while guess != random_number and attempts < 5:
        attempts += 1
        guess = int(input(f'Guess an number between 1 and {x} : '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

if guess == random_number:
        print(f'Yay, congrats. You have guessed the number {random_number} correctly in {attempts} attempts!')
else:
        print(f'Sorry, you have used all your attempts. The number was {random_number}. Better luck next time!')

#Ask to play again
play_again = input('Do you want to play again? (y/n): ')
if play_again.lower() == 'y':
    guess(x)

guess(10)


    
    
