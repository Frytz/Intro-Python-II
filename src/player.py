# Write a class to hold player information, e.g. what room they are in
# currently.


#The Player
import textwrap
from items.item import Item

class Player(Item):
    def __init__(self, name, room, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}, {self.room}"

    def move(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room == None:
            print(
                f"That area is blocked, {self.name}. Please select a new direction.\n")
        else:
            self.room = next_room
            print(textwrap.fill(
                f"\n You walk into the {self.room}. \n ", 65))

    def add_inventory(self, Item):
        # super().__init__(self, name, description)
        self.inventory.append(Item)
        return f"you got a {self.inventory}"

    def remove_inventory(self, inventory):
        self.inventory.remove(inventory)
        return f"{self.inventory}"

    def get_inv(self):
        output=""
        
        for v in self.inventory:
            output += f"{v}"
        return output
