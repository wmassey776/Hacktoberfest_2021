#!/usr/bin/env python3
"""project: Guess the Secret Number
created:2021-10-07, @author:wmassey, email:wmassey776@gmail.com, github:https://github.com/wmassey776"""

import sys
from random import randint


def guess_number() -> None:
    """Guess the secret number game. """     
    low = 1  # Low ow range of secret number
    high = 100  # High range of secret number 
    guesses = 7  # Number of guesses        
    secret_number = randint(low, high)
    

    print(f'''I'm thinking of a secret number between {low} and {high}. You have
{guesses} chances to guess the number. Good luck! ''')

    while True:
        if guesses == 0:
            break
        # Input validation loop
        while True:            
            user_guess = input('Guess the secret number:\n> ')
            if not user_guess.isdigit():
                print('Invalid input!')
                continue
            else:
                break
        # Cast user_guess to integer 
        user_guess = int(user_guess)

        # Determine the result of guess
        if user_guess == secret_number:
            print(f'Bingo! You guessed {secret_number} correctly!')
            break
        elif user_guess < secret_number:
            print('Too low!\n')
        elif user_guess > secret_number:
            print('Too high!\n')
        guesses -= 1
        
    print(f'Game Over! The secret number was {secret_number}!')
    play_again()


def play_again():
    while True:
        user_input = input('Play again? (yes or no):\n> ')
        if user_input.lower() not in ['yes', 'no']:
            print('Invalid Response!')
            continue
        elif user_input.lower() == 'yes':
            return main()
        elif user_input.lower() == 'no':
            print('Thanks for playing - Goodbye!')            
            return sys.exit()



def main():
    guess_number()

    

if __name__ == '__main__':
    main()
