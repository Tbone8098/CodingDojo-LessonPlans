import random

class ForceWielder(object):
    def __init__(self, name, side="light", health=100, force_standing=10 ):
        self.name = name
        self.side = side
        self.health = health
        self.force_standing = force_standing
    
    def print_info(self):
        print(f"name: {self.name}")
        print(f"side: {self.side}")
        print(f"health: {self.health}")
        print(f"force_standing: {self.force_standing}")
        return self

    def change_force_standing(self, amount):
        self.force_standing += amount
        if self.force_standing < 0:
            self.side = "dark"
        else:
            self.side = "light"
        return self
    
    def is_attacked(self, amount):
        isBlocked = random.randrange(1,100) % 2
        if isBlocked == 0:
            print("missed")
        else:
            self.

tyler = ForceWielder("tyler", "light")
tyler.print_info().change_force_standing(20).print_info()