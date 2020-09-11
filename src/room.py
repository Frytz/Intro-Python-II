# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = item

    def __str__(self):
        return f"{self.name}, {self.description}"

    def add_item(self, item):
        self.item.append(item)
# return f"{self.item}"

    def remove_item(self, item):
        self.item.remove(item)

    def see_room(self):
        return f"These items re available: {self.item}"