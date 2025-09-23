import random
import 

def guess(x):

    print('Welcome to the Number Guessing Game!')
    print('Enter your name : ')
    print('Choose difficulty: easy, medium, hard :')
    difficulty = input.lower()
    if difficulty == 'easy':
         x = 1<=10
    elif difficulty == 'medium':
         x = 1<=50
    elif difficulty == 'hard':
            x = 1<=100
    random_number = random.randint(difficulty)
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
        elif guess == random_number % 2 ==0:
             print('Number is Even')
        elif guess == random_number % 2 !=0:
             print('Number is Odd')

       

if guess == random_number: # type: ignore
        print(f'Yay, congrats. You have guessed the number {random_number} correctly in {attempts} attempts!')
else:
        print(f'Sorry, you have used all your attempts. The number was {random_number}. Better luck next time!')

        Score = 100-(attempts*10)
        print(f'Your score is {Score}')

#Ask to play again
play_again = input('Do you want to play again? (y/n): ')
if play_again.lower() == 'y':
    guess(x)

guess(10)




    
    
