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
    # player_one_wins = 0
    # player_two_wins = 0
    max_counter = 5
    while counter <= max_counter and not winner_exists:
        print(f'===== Turn {counter} =====')
        player_one_choice = player_one.method_of_play(game_gestures.gesture_name_list)
        # player_one_choice = select_option(game_gestures.gesture_name_list, 1)
        player_two_choice = player_two.method_of_play(game_gestures.gesture_name_list)
        # if opponent_type == '1':  # Human vs Human
        #     player_two_choice = select_option(game_gestures.gesture_name_list, 2)
        #     print(f'Player 2, your choice was {player_two_choice} \n')
        # else:
        #     player_two_choice = random_selection(game_gestures.gesture_name_list)
        #     print(f'The computer chose: {player_two_choice}')

        # track user wins and conditionally set winner_exists
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


# def select_option(gestures, player_number):
#     gesture_choice = ''
#     valid_entry = False
#     print(f'The Gesture list is: {gestures}')
#     while not valid_entry:
#         gesture_choice = input(f'Player {player_number}, which gesture do you choose? ')
#         try:
#             gestures.index(gesture_choice)
#             valid_entry = True
#         except ValueError:
#             print('That is not a valid option. Please try again.')
#     return gesture_choice
#
#
# def random_selection(gestures):
#     index = random.randint(0, 4)
#     gesture_choice = (gestures[index])
#     return gesture_choice


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
