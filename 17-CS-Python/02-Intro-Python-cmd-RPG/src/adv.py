from textwrap import wrap
from time import sleep

from item import Item
from player import Player
from room import Room

# Declare the rooms
room = {
    'outside': Room(
        name="Outside Cave Entrance",
        desc="North of you, the cave mouth beckons",
        items=[
            Item("Rock", "It's just a rock."),
        ]
    ),
    'foyer': Room(
        name="Foyer", 
        desc="""Dim light filters in from the south. Dusty passages run north 
and east.""",
        items=[]
    ),
    'overlook': Room(
        name="Grand Overlook", 
        desc="""A steep cliff appears before you, falling into the darkness. 
Ahead to the north, a light flickers in the distance, but there is no way 
across the chasm.""",
        items=[]
    ),
    'narrow': Room(
        name="Narrow Passage", 
        desc="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        items=[]
    ),
    'treasure': Room(
        name="Treasure Chamber", 
        desc="""You've found the long-lost treasure chamber! Sadly, it has 
already been completely emptied by earlier adventurers. The only exit is to the 
south.""",
        items=[]
    ),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if __name__=="__main__":
    name = input("Input your name > ")
    player = Player(name, room['outside'])
    for i in range(3):
        print('.')
        sleep(0.25)

    while True:
        print('', '---', '', sep='\n')
        print(player.current_room.name.upper())
        for l in wrap(player.current_room.desc, 80):
            print(l)

        if player.current_room.items:
            print('\nItems in view:')
            for item in player.current_room.items:
                print(f"   {item.name}: {item.desc}")

        cmd = input('> ').lower().split(' ')
        verb = cmd[0]

        if verb in ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
            player.move(verb[0])
            continue

        elif verb in ['get', 'take', 'drop']:
            if len(cmd) < 2:
                print(f'Enter an object to {verb}.')
                input('\n<< enter any key to continue >>')
                continue

            obj = cmd[1]

            if verb == 'drop':
                drop_item, drop_idx = None, None
                for idx, item in enumerate(player.items):
                    if obj == item.name.lower():
                        drop_idx = idx
                        drop_item = item

                if not drop_item:
                    print("You don't have that item.")
                else:
                    player.current_room.items.append(
                        player.items.pop(idx)
                    )
                    drop_item.on_drop()

            elif verb in ['get', 'take']:
                take_item, take_idx = None, None
                for idx, item in enumerate(player.current_room.items):
                     if obj == item.name.lower():
                        take_idx = idx
                        take_item = item

                if not take_item:
                    print("Item not in room.")
                else:
                    player.items.append(
                        player.current_room.items.pop(idx)
                    )
                    take_item.on_take()

        elif verb == 'inventory':
            if player.items:
                for item in player.items:
                    print(f"   {item.name}: {item.desc}")
            else:
                print("You have no items.")

        elif verb == 'q':
            break

        else:
            print('Enter a direction (n/e/s/w) or action (take/drop/inventory)')
        
        input('\n<< enter any key to continue >>')
        continue
