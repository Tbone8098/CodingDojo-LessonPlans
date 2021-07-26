import random

class Person:
    def __init__(self, first_name, last_name, health=100):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def printInfo(self):
        print()
        print(f"******* {self.full_name}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Health: {self.health}")
        return self
    
    def get_health(self):
        print(f"{self.full_name} has {self.health}")
        return self

    def take_damage(self, amount, attacker, round):
        defence_roll = random.randint(0, 20)
        print(f"{self.full_name} rolled a {defence_roll} for defence agains {amount} damage")

        if defence_roll < 10:
            print(f"{self.full_name} took {amount} damage")
            self.health -= amount

        elif defence_roll == 20:
            print(f"{self.full_name} rolled a crit!")
            self.give_damage(amount, attacker, round)

        else:
            print(f"{self.full_name} blocked")
            attack_reduction = random.random()
            print(f"attack reduction: {attack_reduction}")
            self.give_damage((amount*attack_reduction), attacker, round)
        return self
    
    def give_damage(self, amount, person_attacked, round=1):
        # print(f"{self.full_name} is attacking {person_attacked.full_name}")
        person_attacked.take_damage(amount, self, round)
        return self

class ForceUser(Person):
    def __init__(self, first_name, last_name, alignment, midichlorian_count, health=100):
        super().__init__(first_name, last_name, health)
        self.alignment = alignment
        self. midichlorian_count = midichlorian_count

    @property
    def force_side(self):
        if self.alignment < 0:
            return "Dark Side"
        elif self.alignment > 0:
            return "List Side"
        else:
            return "Confussed"

    def give_damage(self, amount, person_attacked, round=1):
        print(f"ROUND: {round}")
        print(f"{self.full_name} is attacking {person_attacked.full_name}")
        if self.force_side == person_attacked.force_side and round == 1:
            user_input = input("Are you sure you want to attack?")
            if user_input.lower() == 'y' or user_input.lower() == 'yes':
                round += 1
                self.alignment -= 50
                return super().give_damage(amount, person_attacked, round)
        else:
            round += 1
            return super().give_damage(amount, person_attacked, round)


    def printInfo(self):
        super().printInfo()
        print(f"force side: {self.force_side}")
        print(f"alignment: {self.alignment}")
        return self


John = ForceUser("john", "romine", 75, 10000)
Tyler = ForceUser("tyler", "tbo", -75, 15000)
Joe = ForceUser("joe", "tbo", 0, 15000)
Curtis = ForceUser("curtis", "tbo", 80, 15000)

John.give_damage(25, Curtis)
Curtis.printInfo()
John.printInfo()
