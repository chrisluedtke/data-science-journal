from time import sleep

class Player:
    """A class to hold player information, e.g. what room they are in 
    currently."""
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        if direction == 'n' and self.current_room.n_to:
            self.current_room = self.current_room.n_to
        elif direction == 'e' and self.current_room.e_to:
            self.current_room = self.current_room.e_to
        elif direction == 's' and self.current_room.s_to:
            self.current_room = self.current_room.s_to
        elif direction == 'w' and self.current_room.w_to:
            self.current_room = self.current_room.w_to
        else:
            print('Nothing there . . .')
