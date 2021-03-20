# Import Gestures
# this will allow us to use/"inherit" the attributes in gestures
# in order to build list of gesture objects
import gestures
from gestures import Gestures


class GestureList(Gestures):
    def __init__(self, gesture_name='', list_index=0, gesture_array=None, winning_actions=None):
        super().__init__(gesture_name, list_index, gesture_array, winning_actions)
        if gesture_array is None:
            gesture_array = []
        if winning_actions is None:
            winning_actions = []
        self.gesture_name_list = []
        self.gesture_obj_list = []

    def build_list(self):
        # Instantiate all gestures and their relationships to other gestures
        # Indexes 0 and 1 are wins against and 2 and 3 are losses against
        self.gesture_obj_list.append(Gestures('Rock', 0,
                                              ['Lizard', 'Scissors', 'Spock', 'Paper'],
                                              ['crushes', 'crushes']))

        self.gesture_obj_list.append(Gestures('Paper', 1,
                                              ['Rock', 'Spock', 'Lizard', 'Scissors'],
                                              ['covers', 'disproves']))

        self.gesture_obj_list.append(Gestures('Scissors', 2,
                                              ['Lizard', 'Paper', 'Rock', 'Spock'],
                                              ['decapitates', 'cuts']))

        self.gesture_obj_list.append(Gestures('Lizard', 3,
                                              ['Paper', 'Spock', 'Rock', 'Scissors'],
                                              ['eats', 'poisons']))

        self.gesture_obj_list.append(Gestures('Spock', 4,
                                              ['Rock', 'Scissors', 'Lizard', 'Paper'],
                                              ['vaporizes', 'smashes']))
        # Now build the name list
        for gesture in self.gesture_obj_list:
            self.gesture_name_list.append(gesture.gesture_name)
        return self

    def print_list(self):
        print(f'The Gesture list is: {self.gesture_name_list}')
        return self

    def find_gesture_index(self, a_gesture):
        print(self.gesture_obj_list[0].gesture_name)
        for gesture in self.gesture_obj_list:
            if a_gesture in gesture.gesture_name:
                print(f'The record for {a_gesture} was found with a tracked index of {gesture.list_index}')
        return self
