from player import Player


class HumanPlayer(Player):
    def __init__(self, name='', player_number=1):
        super().__init__(name, player_number)
        pass

    def method_of_play(self, gestures):
        gesture_choice = ''
        valid_entry = False
        print(f'The Gesture list is: {gestures}')
        while not valid_entry:
            gesture_choice = input(f'{self.name}, which gesture do you choose? ')
            try:
                gestures.index(gesture_choice)
                valid_entry = True
            except ValueError:
                print('That is not a valid option. Please try again.')
        else:
            print(f'{self.name} your choice was {gesture_choice} \n')
        return gesture_choice
