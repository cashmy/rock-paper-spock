class Player:
    def __init__(self, name, player_number):
        self.name = self.validate_name(name, player_number)
        self.player_number = player_number
        self.wins = 0

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number}, what is your name?: ')
        return name

    def method_of_play(self, gestures):
        pass
