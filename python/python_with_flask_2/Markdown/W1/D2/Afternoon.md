# W1D2 Morning - OOP

## OBJECTIVES AND OVERVIEW

### Objectives

1. Students will understand the big picture of OOP
1. Students will be exposed to the parts of a class

### Oberview

- [classes](#classes)
- [Instances](#Instances)
- [Self](#Self)
- [constructor](#constructor)
- [attributes and methods](#attributes-and-methods)
- [Inheritance](#Inheritance)
- [Chaining](#Chaining)

<hr>

# Classes

- what are they?
  - Blueprints of a "thing"
  ```
  What do you think of when you think of a blueprint?
  ```
  - Outline that you can make "copies" (or instances) of
- Why do we want them?
  - Creates structure
  - Contains related code together
- Syntax of a class
  - Every word the is caps
  - no spaces
  - pascal case

# Instances

- What is an Instance
  - "In this specific instance, it is okay to get in a fight"
  ```
  What is the above question an instance of?
  ```
- Why do we want an instance?
  - Blueprint of a house
    - Many homes
  - Think about STAR WARS
    - Jedi
    - Sith
    - Storm trooper
- How do we create an instance?

  ```py
  class Jedi:
      pass

  John = Jedi(...)
  Frank = Jedi(...)
  ```

# Self

- What is self?

  - refers to the specific instance
  - the specific home or jedi

- When would we use self?

  - When we want to refer to an attribute of the specific instance
  - the jedi -> john has health that is different from Frank's health

- How do we use self

  - include it in the function inside the class

  ```py
  class Jedi:
      pass

      def take_damage(self):
          self.health - 10
  ```

# Constructor

- What is a constructor?

  - It builds the blueprint
  - creates the instance
  - is the first thing that runs when you create a new instance of a class

- Why do we need this?

  - Creates the instance of the class

- When do we use this?

  - Almost always you will have this as the first thing you create after defining the class name itself

- How do we start?
  - dunder init function
  - magic method
  ```py
  class Jedi:
      def __init__(self, first_name, last_name):
          self.first_name = first_name
          self.last_name = last_name
  ```
  - self.first_name IS NOT first_name
  - always takes in self as the first parameter

# Attributes and Methods

- What are attributes?
  - Things that make up that object
  - for a person
    - first name
    - last name
    - number of arms
    - gender
    - attractivness scale
  - for a song
    - name
    - band
    - Artist
    - length of song
    - happiness level
    - genre
- How to use attributes?

  - by targeting the "self" or the instance of that class and their attributes

- what are methods?
  - Actions that the class can do
- How do we use them

  ```py
  class Jedi:
      def __init__(self, first_name, last_name, health=100):
          self.first_name = first_name
          self.last_name = last_name
          self.health = ealth

      # Normal Method
      def take_damage(self, amount):
          self.health -= amount
  ```

- What types of methods are there
  - "normal mode"
    - act on the instance of the class
  - classmethod
    - target the whole class and not a specific instance
  - static
    - Doesn't really do anything, however it is good to keep code together

# Inheritance

- What is Inheritance?

  - if a class has a bigger class that it is attached to
  - Employees
    - Instructor
    - Head Instructor
    - CEO

- How does it help us?

  - It allows us not to have to dup our code
  - keeps it DRY

- When would we use it?

  - when a class has a "parent" class

- How do we do this?

```py
cclass Person:
    def __init__(self, first_name, last_name, health=100):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def printInfo(self):
        print("******* ")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Full name: {self.get_full_name()}")
        print(f"{self.get_full_name()} has {self.health}")
        print("******* ")


    def get_health(self):
        print(f"{self.get_full_name()} has {self.health}")
        return self


class ForceUser(Person):
    def __init__(self, first_name, last_name, alignment, midichlorian_count, health=100):
        super().__init__(first_name, last_name, health)
        self.alignment = alignment
        self. midichlorian_count = midichlorian_count


John = ForceUser("john", "romine", 75, 10000)
John.printInfo().get_health()
# John.get_health()
```

# Chaining

- What is chaining? what is it doing?
  - returns the instance of the class
  - **show that if you don't have RETURN SELF that it will return a _"noneType"_**
  - Remeber that a function is what it returns
  - lets us connect one command to another
- How do we make it happen?
  - return self at the end of every method
