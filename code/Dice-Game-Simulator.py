#!/usr/bin/env python3
"""Original source: seraph★776, email: seraph776@gmail.com, github: https://github.com/seraph776

from random import randint
import sys


def main():
    d: dict[int, int] = {k:0 for k in range(3, 12)}
    d.setdefault('snakeEyes', 0)
    d.setdefault('doubles', 0)

    dice_roll = int(input('How my dice roll simulations?\n> '))

    for i in range(dice_roll):
        d1 = randint(1, 6)
        d2 = randint(1, 6)

        if d1 + d2 == 2:
            d['snakeEyes'] += 1
        elif d1 == d2:
            d['doubles'] += 1
        else:
            d[d1+d2] += 1

    print(f'--- Results of {dice_roll} rolls --- ')
    for k, v in d.items():
         print(f"You rolled {k}, {v} times at {100 * (v/dice_roll):.2f}%")

    play_again()

def play_again():
    """Handles play again option"""
    while True:
        option = input('\nWould you like to play again?! (yes or no): ')
        if option not in ['yes', 'no']:
            print('invalid option!')
            continue
        else:
            break
    if option == 'yes':
        return main()
    else:
        print('Thanks for playing - Goodbye!')
        sys.exit()


if __name__ == '__main__':
     main()
