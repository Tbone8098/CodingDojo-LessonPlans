# W1D1 Afternoon

## OBJECTIVES, OUTCOMES, AND OVERVIEW

## Objectives

1. Students will understand the difference between js and python syntax
1. Students will understand python data type

## Outcomes

## Overview

- [Conditionals](#Python-Syntax)
- [Loops](#Loops)
- [Python Functions](#Python-Functions)
- [Parameters VS Arguments](#Parameters-vs-arguments)
- [Default Parameters](#default-parameters)

# Conditionals

```
What is a conditional?
Pulling from the morning session, can someone tell me how to write a conditional?
```

if, elif, else

**NOTE:** else if BECOMES elif

conditionals see if something equates to being True or False

- is this true? if it is than do something

```py
name = "tyler"
if name != "Tyler":
    print("noooooooooooooo!")
```

## Logical operators

- ==
- !=
- '>'
- '<'
- '<='
- '>='
- and
- or
- not

# Loops

**Note** loops have aspects that are sometimes hard for people to grasp right away.

1. for loops
   - have a set amount of runs through the loop
   - for 10 times
1. while loops
   - keep running until a condition is no longer True

python automatically will extract the item at the index in a for loop

```py
names = ['tyler','joe','curtis']
for name in names:
    print(name)
```

- pull out tyler, joe, curtis

If you want to use the index then you will need to use the "RANGE" function

```py
for index in range(len(names)):
    print(index)
```

Some common things you can loop through:

- Strings
- Loops
- Dictionaries

### ^^^^^^^^^^^^^^^^^^^^Pop Quiz^^^^^^^^^^^^^^^^

1. How many ways can you see (at this moment) where python is different than JavaScript in it's syntax?
2. What dataTypes did we cover and what are their indicators (what tells you that they are that dataType)?
3. What is the difference between a float and an int?
4. What is an f-string (what does it allow us to do)? and what is it's indicator?
5. Name one thing that is unique to a list?
6. Explain why getting data from a list could be slower than getting data from a dictionary?
7. What is a conditional? How to use them?
8. Explain how
   ```python
   for key in all_keys:
       print(key)
   ```
   is different from
   ```python
   for key in range(len(all_keys)):
       print(key)
   ```

# Inputs and Outputs

A way to get input from the user using the terminal

```py
user_input = input("favorite color: ")
print(f"your favorite color is {user_input}")
```

# Python Functions

_Group activity_ - 3 to 5 minutes

```
What is a function and what is their purpose?
What are some attributes (things that define) of a function?
Write some examples of some basic functions
```

## **Attributes**

- name
- can takes in parameters
- performs a set of instructions
- returns something
  - implicit or explicit

Think of a function like a factory

- factories have trucks that bring it stuff -> parameters
- factories do something with the stuff -> set of instructions
- factories produce some kind of product -> the return

## **Advantages of useing a function**

- Help to create DRY code
- Breaks down complex problems into simpler ones
- Improves readability or clairity for people reading the code.

"Any body can create code that a computer can read, a good programmer will write code that people can read"

**Remember** You are what you return

# Parameters VS Arguments

- parameters = what the function takes in
- arguments = what you pass to the function

# Default Parameters

def some_funct(some_param="tyler" ):
print(some_param)
