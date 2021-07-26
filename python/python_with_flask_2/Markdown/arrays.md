## Arrays

<link rel="stylesheet" href="../../style.css">

### Objectives

1. Students will understand what an array is and the attributes of an array
1. Students will be exposed to (briefly) to other data types in order to contrast them with arrays
1. Students will be exposed to some of the many built-in functions that go along with arrays

### Goals

- What is an array? examples
- Attributes of an array
- Built in function that comes with arrays
- Looping through arrays with a for loop

### Overview

- [What is an array](#what-is-an-array)
- [Attributes](#attributes)
- [Functions](#functions)
- [Loops](#loops)

<hr>

## What is an array

### group work - 3 minutes

```
With out thinking about coding or code, What is a real life example of an array?

In 3 minutes I want you and your group to come up with as many examples of arrays as you can, we will share with the class some of our examples and how they are or are not good examples.
```

**Define**: an array is a list of items.

- Grocery list
  - food
  - drinks
  - kitchen stuff
- shopping list
- to do list
- repair list

## Attributes

- index
- can hold many different data types
  - can hold arrays inside of arrays
- calling data out of an array

```
When we think about a shopping list, is the order of the items on the list important? What about when we think of a to do list?
```

### <u>**Index Base**</u>

Arrays are indexed, and they are indexed starting at 0

- Easy concept to grasp, when counting instead of starting at 1 you start at 0 so that the first item in the list is the 0 item.
- an array with 10 items will have the last index be the **\_** ? 9th...always one less than the total number of items.

### <u>**Data Types**</u>

Arrays can hold all sorts of data types

```
Take a minute and write down (on a piece of paper or notepad) as many data types that you know? There are 4 really common data types.
```

**\*\***\*\***\*\*\*\*** **Discuss** **\*\*\*\***\*\*\*\***\*\*\*\***

| Data Types | Indicators          |
| ---------- | ------------------- |
| strings    | " "                 |
| numbers    | 1,2,3,4,5,6,7,8,9,0 |
| arrays     | [ ]                 |
| objects    | { }                 |

- arrays can store arrays inside arrays

### Manipulating Data

- storing data is only good if we can access the data we store

- Get data
- Change data

```
Does anybody know how we would access data which is stored in an array?
```

var someArr = ["this", "that", "the other"]

- someArr[0]
- someArr[2] = "someVal"

## Functions

- push
- pop

- join

### Push

```
by the name alone can you guess what this built-in function does with the array?
```

- pushing data into the array

- broken up into 3 parts

1. the array
1. the command
1. the value

```js
someArr.push("someVal");
```

### Pop

```
if push, pushes data into an array, what do you think pop does?

Go to the internet to make sure, I will call on a random person in 2 minutes
```

- pops data out of an array from the back and returns that data to you

```
Then the question is how do we remove data from the front? what about from the middle?

In groups, you have 5 minutes to find all the ways you can to remove data from an array. Go look through the internet to find what you need?
```

- pop - from back
- shift - from front
- slice - from anywhere -> must have parameters

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* **Discuss** \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Loops
