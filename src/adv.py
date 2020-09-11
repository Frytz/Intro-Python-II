from room import Room
from player import Player
from items.weapon import Weapon
from items.armor import Armor
from items.item import Item


# Declare all the rooms
sword = Weapon("A sword", "This sword is rusty", 10)
helmet = Armor("a helmet", "this is a wortless helmet", -5)
# item = {
#     'a_key': Item("key", "A small key"),
#     'ball_of_light': Item('Ball of Light', "It may or may not work"),
#     'something': Item('something', 'something'),
# }

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [sword]), 
                

    'foyer':    Room("Foyer", 
                     "Dim light filters in from the south. Dusty passages run north and east.",[helmet]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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




# Addings Items to rooms
# room['outside'].add_item(sword)
# room['foyer'].add_item('ball_of_light')

# room['foyer'].it=.append(
#     Item("Clay tablet", "Large clay tablet with some runes but you can't read them"))
# room['overlook'].item.extend(
#     [Item("helmet", "A helmet that could save your life, but its too small for you to wear"), Item("broad sword", "A powerful broad sword, broken at the hilt and the blade is missing")])
# room['narrow'].item.append(
#     Item("spoon", "A dirty sppon with dried food stuck to it"))
# room['treasure'].item.append(
#     Item("small paper", "A small piece of paper with something written on it: Indiana Jones was here!"))

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
current_player = Player(input("How may I refer to you? "),
                        room['outside'])


print(
    f"\nThat is a lovely name, {current_player.name}. Welcome to the world!\n")
# print(
    # f"As you enter the world, you are currently standing in the {current_player.room} {current_player.inventory}\n")
print("You have several options to pick from:\n")
print("'n' - To move North\n")
print("'s' - To move South\n")
print("'e' - To move East\n")
print("'w' - To move West\n")
print("'l' - To look at the room your in\n")
print("'get [item name]' - To add an item to your inventory\n")
print("'drop [item name]' - To drop the item in the current room\n")
print("'leave' - To leave the item in the room\n")
print("'i' - To check your current inventory\n")
print("------------------------")
print("'q' - To leave the world\n\n")
print(
    f"As you enter the world, you are currently standing in the {current_player.room}\n")

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
while True:
    cur_play = current_player
    for item in cur_play.room.item:
        print(item)
    # print("\n")
    # Allowing for user input
    user_input = input("~~~~> ")

    # User selects direction
    
    if user_input in ["n", "s", "e", "w"]:
        cur_play.move(user_input)
        # break
    elif user_input in ["get"]:
        cur_play.add_inventory(Item)
        cur_play.room.remove_item(item)
    elif user_input in ["inv"]:
        print(cur_play.get_inv())

    elif user_input == "q":
        print(f"\nHave fun exploring the outside world, {cur_play.name}.\n")
        break
    # User selnected something outside of given commands
    else:
        print(
            f"\n Oof, that should not have happened. \n This is embarrassing. \n You tried moving to a location that does not exist! \n")
