# imports
from gesture_list import GestureList
import random


game_gestures = GestureList()
game_gestures.build_list()


def begin_game():

    opponent_type = determine_opponent()

    counter = 1  # 5 turns
    winner_exists = False
    player_one_wins = 0
    player_two_wins = 0
    while counter <= 5 and not winner_exists:
        print(f'===== Turn {counter} =====')
        player_one_choice = select_option(game_gestures.gesture_name_list, 1)
        print(f'Player 1, your choice was {player_one_choice} \n')
        if opponent_type == '1':  # Human vs Human
            player_two_choice = select_option(game_gestures.gesture_name_list, 2)
            print(f'Player 2, your choice was {player_two_choice} \n')
        else:
            player_two_choice = random_selection(game_gestures.gesture_name_list)
            print(f'The computer chose: {player_two_choice}')

        # track user wins and conditionally set winner_exists
        turn_winner = check_turn_winner(player_one_choice, player_two_choice)
        if turn_winner == 1:
            player_one_wins += 1
        else:
            player_two_wins += 1
        if player_one_wins == 3 or player_two_wins == 3:
            winner_exists = True

        counter += 1
    declare_winner(player_one_wins,player_two_wins,opponent_type)


def determine_opponent():
    valid_entry = False
    while not valid_entry:
        print(' 1) Human vs. Human  or  2) Human vs. AI')
        opponent_type = input("Who would you like to play against? ")
        if opponent_type == '1' or opponent_type == '2':
            valid_entry = True
        else:
            print('\nI did not understand your entry. Please try again.')
    return opponent_type


def select_option(gestures, player_number):
    valid_entry = False
    print(f'The Gesture list is: {gestures}')
    while not valid_entry:
        gesture_choice = input(f'Player {player_number}, which gesture do you choose? ')
        try:
            gestures.index(gesture_choice)
            valid_entry = True
        except ValueError:
            print('That is not a valid option. Please try again.')
    return gesture_choice


def random_selection(gestures):
    index = random.randint(1, 5)
    gesture_choice = (gestures[index])
    return gesture_choice


def check_turn_winner(player_one_choice, player_two_choice):
    turn_winner = game_gestures.compare_gesture(player_one_choice,player_two_choice)
    return turn_winner


def declare_winner(player_one_wins, player_two_wins, opponent_type):
    print('\n ============================ ')
    print('        The winner is :       ')
    if player_one_wins > player_two_wins:
        winner_string = 'Player One'
    elif opponent_type == '1':
        winner_string = 'Player Two'
    else:
        winner_string = 'Computer'
    winner_string = winner_string.center(30)
    print(f'{winner_string}')