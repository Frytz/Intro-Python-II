import textwrap


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"\n{self.name}\n{self.description}"

    def on_get(self):
        return f"You have picked up {self.name}"

    def on_drop(self):
        return f"You have dropped {self.item}"
    
