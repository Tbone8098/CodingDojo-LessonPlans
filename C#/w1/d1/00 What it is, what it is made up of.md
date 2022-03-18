<link rel="stylesheet" href="../../style.css">

# What are we actually learning? C# / .net / ASP.NET 
<div class="overview">
Overview

<input type="checkbox"> [About C#](#About-C#)           
<input type="checkbox"> What is dot Net      
<input type="checkbox"> What is ASP.NET      
<input type="checkbox"> What are C# strengths

</div>

## C#
- the language 
- c# got it's name from being one better than c++
  - c++++ then it became c# because a # sign looks like 4 plus signs
  
## NET
- a framework to build applications
- but is focused on the console
- Use .net 3.1

## ASP.NET
- a framework for building WEB applications
- an extensions of .NET

## About C#
- object oriented programming
  - almost EVERYTHING we make will be a class. 
  - classes built on classes built on classes
  - other than interfaces
- a compiled and strickly typed language
  - strickly typed
    - must declare the type of the variable
    - rules are always the same
  - compiled
    - <span class="highlight">two types of friends analogy</span>
    - Falsey and Truethy -> 0 being falsey and 1 being truethy

<div class="overview">

# QUESTIONS

- what is .net
  - a framework that allows us to build an application on the fly and use c# to write our code and we don't have to worry about forcing it to compile
- ASP is built on top of .net 
  - to listen for http requests

</div>

# Getting Started With DotNet
- We can't just take a file and say `run it`
  - C# is a little more complex
  - because it is a compiled language

__It is going to look for things__
- a file name "main"

<span class="highlight">Starting a new Project</span> In the terminal:
  ```
  dotnet new console
  ```
  - this will create files in the current location
    - filename.csproj 
    - obj/
    - Program.cs
  ```
  dotnet new console -o project_name
  ```
  - When you see missing things for the debugger __add them__

<span class="highlight">In OBJ folder there is a bunch of information, this info links directly to file paths on your computer</span>
- if you are having problems: 
  - delete the obj folder 
  - run in the terminal
    ```
    dotnet build
    ```

# Where do we come in as developers?
Go into `Program.cs`

## What are namespaces?
- remember how we had to import things in python?
  - reletive path "from ____ import ____"
- We just have to give it the same namespace

somethingElse.cs
```cs
  namespace something1
  {
    public class SomeClass
    {}
  }
```

program.cs
```cs
  using System;

  namespace something1
  {
    class Program
    {
      static void Main(string[] args)
      {
        Console.WriteLine("Hello World")
        // New line here
        SomeClass myClass = new SomeClass();
      }
    }
  }
```

- as long as everything is in the same `namespace` then it is accessble between files

<span class="highlight">Naming convention</span>
- BEST PRACTICE
- each class is in its own file
- each file is going to be named the samething as the class


`static` and `void`

<span class="highlight">Static</span> means that it does not need an instance of the object to be called on. `remember back to python where we had @staticmethods`

<span class="highlight">Void</span> means that it is going to return nothing. `remember that a function becomes what it returns` we are saying here that this is going to return nothing

- In python we could create a function anywhere but in C# because everything is in classes we need to create a function inside a class

# How to run your program 
- in your terminal 
  - navigate to your project dir
  ```
  dotnet run
  ```

`notice` how it took a minute for it to run....this is the compiling process

