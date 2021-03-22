from player import Player
import random


class ComputerPlayer(Player):
    def __init__(self, name='', player_number=2):
        super().__init__(name, player_number)
        pass

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number}/Computer, what is your name?: ')
        return name

    def method_of_play(self, gestures):
        index = random.randint(0, 4)
        gesture_choice = (gestures[index])
        print(f'The computer {self.name}\'s choice was {gesture_choice} \n')
        return gesture_choice
