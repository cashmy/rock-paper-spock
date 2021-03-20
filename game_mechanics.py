# imports
from gesture_list import GestureList


def begin_game():
    game_gestures = GestureList()
    game_gestures.build_list()

    opponent_type = determine_opponent()

    counter = 1  # 5 turns
    winner_exists = False
    while counter <= 5 or winner_exists:
        print(f'===== Turn {counter} =====')
        player_one_choice = select_option(game_gestures.gesture_name_list, 1)
        print(f'Player 1, your choice was {player_one_choice} \n')
        if opponent_type == '1':  # Human vs Human
            player_two_choice = select_option(game_gestures.gesture_name_list, 2)
            print(f'Player 2, your choice was {player_two_choice} \n')
        else:
            # random selection
            print(f'The computer chose: Rock')
        # track user wins and conditionally set winner_exists
        counter += 1


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


def select_option(game_gestures, player_number):
    valid_entry = False
    print(f'The Gesture list is: {game_gestures}')
    while not valid_entry:
        gesture_choice = input(f'Player {player_number}, which gesture do you choose? ')
        try:
            game_gestures.index(gesture_choice)
            valid_entry = True
        except ValueError:
            print('That is not a valid option. Please try again.')
    return gesture_choice

