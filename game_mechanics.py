# imports
from gesture_list import GestureList


def begin_game():
    game_gestures = GestureList()
    game_gestures.build_list().print_list()

    counter = 5
    winner_exists = False
    while counter >= 0 or winner_exists:
        counter -= 1

    game_gestures.find_gesture_index('Lizard')


