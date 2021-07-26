# W1D1 Morning

## OBJECTIVES, OUTCOMES, AND OVERVIEW

## Objectives

1. Students will understand the difference between js and python syntax
1. Students will understand python data type

## Outcomes

## Overview

- [Python Syntax](#Python-Syntax)
- [Data Type](#Data-Types)
- [Conditionals](#Conditionals)
- [Loops](#Loops)

# Python Syntax

- Python is an indend based language
- Python variable convention VS JavaScript

```
What construct or thing that you know of that is indend based?
```

**_ANSWER_**

- paragraphs
- Lists

## Code Block

```
What is a code block?
```

**_ANSWER_**

A set of lines of code that belong together

```
So thinking back to JS, can you think of code that belongs together?
Looking at the code below can you see how many code blocks there are?
```

```js
function someFunction(){
    var listOfNames = ['Tyler','Joe','Curtis']
    listOfNames.forEach(name => {
        console.log(name)
        if (name === 'Tyler' {
            console.log('that is my name')
        })
    })
}
```

Code Block examples

| js                | python       |
| ----------------- | ------------ |
| functions         | def          |
| if, else if, else | if elif else |
| for, while        | for, while   |
| class             | class        |

```py
def some_function():
    list_of_names = ['Tyler','Joe','Curtis']
    for name in list_of_names:
        print(name)
        if name == 'Tyler':
            print('that is my name')
```

```
what is the difference between the JS version and the python version?
```

**_ANSWER_**

Notice the

- ':' instead of '{}'
- print instead of 'console.log'
- the for loop is a little different

SIDE NOTE: if you want to prep a code block in python but don't actually want to put code into it just yet, you can use **PASS**

```py
def some_function():
    pass
```

# Data Types

```
What are some data types that you know of from JS?
```

1. Primitive data types
   - Booleans
   - Numbers
   - Strings
1. Composite Data Types
   - Tuples
   - Lists
   - Dictionaries

## Booleans

- True or False
- 0 or 1
- tinyInt

## Numbers

- pos and neg
- decimal and whole numbers
  - Int VS float

## Strings

```
What is a string?
```

**_ANSWER_**

Any character, number, special character that is put into quotes -> " "

examples1 = "tyler"
examples2 = "2"

### _String Interpolation_

```
What if we have some variable that we want to place (or insert) into a string?
```

example:

```py
first_name = 'tyler'
last_name = "tbo"
age = 32
print("my name is %s and my last name is %s. Also My age is %s" % (first_name, last_name, age))
print("my first name is {} and my last name is {}. Also My age is {}".format(first_name, last_name, age))
print(f"my name is {first_name} and my last name is {last_name}. Also my age is {age}")
```

### _String functions_

**Group Activity - 5 mintues**

```
In groups look at the given string functions and see if you can figure out what they mean? Then go to the INTERNET and look up what they actually mean.
```

<style>
    .flex {
        display: flex;
        justify-content: space-evenly;
    }
    .section {
        margin: 1em 0;
        padding: 1em;
        background: white;
        color: black;
        border: 1px solid black;
        border-radius: 10px;
    }
</style>

<div class="flex">

<div class="section">

# Group 1

- string.upper()
- string.find()
- string.istitle()
- string.lower()
- string.strip()
</div>

<div class="section">

# Group 2

- string.lower()
- string.join()
- string.isalpha()
- string.islower()
- string.count()
</div>

<div class="section">

# Group 3

- string.swapcase()
- string.isdigit()
- string.split()
- string.format()
- string.find()
</div>
</div>

SIDE NOTE: _Numbers have there own functions as well_

## Forcing something to be a specific data type = type casting

```
What is type casting?
Can you think of a reason where we would need to type cast?
```

**_ANSWER_**

- 2 + "2"
  - NOT GOOD in python
  - In JS it helps you out a little but not in python

## Lists

_Class Discussion_

```
What is a list, what are some examples you can think of in "real life"?
    - List vs Array
What would be a good definition for a list?
```

**Definition:** A construct that contains "items" that are indexed

- recognize them by their [ ] square brackets

Some functions of an array in javascript?

- push
- pop
- length

_Group activity_ - 3 minutes

```
What are the python correspondents to these three functions?
```

## Dictionaries

_Group activity_ - 5 minutes

```
When thinking about a dictionary (the book), answer the following questions?
- What is a dictionary?
- what makes it a dictionary?
- How would you use a dictionary in real life? - the process of using it, step by step
```

- recognized by their { } curley brackets
- key value pair

```py
some_dict = {
    'key1':'value1',
    'first_name':'Tyler'
}
```

- WARNING: When adding to a dict after its creation you will see [ ]
  - inside the [ ] will be a string with the key -> this is the differnce when looking at lists and dictionaries
  ```py
  some_dict['last_name'] = 'Tbo'
  some_dict['first_name'] = 'Joe'
  ```
- Lists are indexed...Dictionaries -> basically are NOT

  - best to think of them as not being indexed.

- create a dictionary
- add to a dictionary
- get info from a dictionary
  - some_dict.pop('key')
  - del some_dict['key']

## Tuples

tuples are a set of information but key take-a-way is that they are immutable, meaning they cannot be changed.
