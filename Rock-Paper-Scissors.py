from random import choice


def rock_paper_scissors():
    """This function Handles the main operation of Rock, Paper, Scissors.
    The User will input their choice against computer and win."""

    player_points = 0
    comp_points = 0
    while player_points < 3 or comp_points < 3:

        lst = ['rock', 'paper', 'scissors']
        computer = choice(lst)

        while player := input('HEY! what is your choice: '):

            if player == computer:
                print(f'{computer} \nDraw!\n')
                break

            elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
                print(f'{computer} \nYou Win!\n')
                player_points += 1
                break

            else:
                print(f'{computer} \nYou Lose!\n')
                comp_points += 1
                break

        print(f'You: {player_points}')
        print(f'Comp: {comp_points}')

        if player_points == 3:
            print('Congrats! You Won the Game')
            break

        elif comp_points == 3:
            print('Sorry, You Lost the Game')
            break


rock_paper_scissors()
