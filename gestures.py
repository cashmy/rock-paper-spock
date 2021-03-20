class Gestures:
    def __init__(self, gesture_name, list_index, gesture_array, winning_actions):
        self.gesture_name = gesture_name
        self.list_index = list_index
        # index 0 and 1 will loose against this instance,
        # 2 and 3 will win against this instance
        self.gesture_oppose = gesture_array
        # An array of 4 (e.g. for Scissors: "cuts" paper and "decapitates" lizard'
        self.winning_actions = winning_actions

    def rtv_gesture_battle_result(self, opposing_gesture):
        pass
