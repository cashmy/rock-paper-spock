# imports
from gesture_list import GestureList


def begin_game():
    game_gestures = GestureList()
    game_gestures.build_list().print_list()

    game_gestures.find_gesture_index('Lizard')


