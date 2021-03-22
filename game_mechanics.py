# imports
from gesture_list import GestureList
from human_player import HumanPlayer
from computer_player import ComputerPlayer

game_gestures = GestureList()
game_gestures.build_list()


def begin_game():
    opponent_type = determine_opponent()

    player_one = HumanPlayer()

    if opponent_type == '1':
        player_two = HumanPlayer('', 2)
    else:
        player_two = ComputerPlayer()

    counter = 1  # 5 turns
    winner_exists = False

    max_counter = 5
    while counter <= max_counter and not winner_exists:
        print(f'===== Turn {counter} =====')
        player_one_choice = player_one.method_of_play(game_gestures.gesture_name_list)
        player_two_choice = player_two.method_of_play(game_gestures.gesture_name_list)
        turn_winner = check_turn_winner(player_one_choice, player_two_choice)
        if turn_winner == 1:
            player_one.wins += 1
        elif turn_winner == 2:
            player_two.wins += 1
        else:
            # increment max counter to accommodate for tie rounds
            max_counter += 1

        if player_one.wins == 3 or player_two.wins == 3:
            winner_exists = True

        counter += 1
    declare_winner(player_one, player_two, opponent_type)


# noinspection PyGlobalUndefined
def determine_opponent():

    opponent_type = ''
    valid_entry = False
    while not valid_entry:
        print(' 1) Human vs. Human  or  2) Human vs. AI')
        opponent_type = input("Who would you like to play against? ")
        if opponent_type == '1' or opponent_type == '2':
            valid_entry = True
        else:
            print('\nI did not understand your entry. Please try again.')
    return opponent_type


def check_turn_winner(player_one_choice, player_two_choice):
    turn_winner = game_gestures.compare_gesture(player_one_choice, player_two_choice)
    return turn_winner


def declare_winner(player_one, player_two, opponent_type):
    print('\n ============================ ')
    print('        The winner is :       ')
    if player_one.wins > player_two.wins:
        winner_string = 'Player One ' + player_one.name
    elif opponent_type == '1':
        winner_string = 'Player Two ' + player_two.name
    else:
        winner_string = 'Computer ' + player_two.name
    winner_string = winner_string.center(30)
    print(f'{winner_string}')
