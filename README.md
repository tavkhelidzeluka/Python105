# Python105

## Lectures 
---
<details>
    <summary>Lecture 1</summary>

- Basic Output
    - print builtin function
    - multiple arguments **print(1, 2, 3, 4)**

- Variables
    - Naming Convention
    - snake_case
    - Case Sensitivity

- Basic Data Types in python
    - int (integer)         **(-∞, ..., -2, -1, 0, 1, 2, ..., +∞)**
    - float (fractions)     **(-∞, ..., -1.1, -1, 0, 1.1, 2, ..., +∞)**
    - str (string)          **"hello", 'hello', """Hello""", '''Hello'''**
    - bool (boolean)        **True, False**

- Basic String Operations
    - concatenation **"Hello" + " " + "World"**
    - fstrings **f"I am {20 + 1} years old"**

- Constants
    - just a convention
    - UPPER_CASE
</details>

<details>
    <summary>Lecture 2</summary>

- Type Casting
    - figuring out type of variable **type(variable_name)**
    - just use data type keyword to cast an object to another data type **str(1), int("125")**
    - Errors during type casting **int("hello 25"), float("nick")**

- Data Structures **list**
    - Initialization | **nums = [], nums = list()**
    - Indexing, Why 0?
    - Accessing elements | **nums[0]**
    - Changing elements | **nums[0] = 1**
    - builtin methods | **append, pop, len, sort**
    - Slicing lists | **nums[3:-1], nums[:], nums[::-1]**
    - Errors (Index Error) | **nums[Non existent Index]**

- Loops **for**
    - basic syntax **for element in my_list:**
    - Indentation **body, code block**
    - looping through lists
    - using range function | **range(10), range(5, 10), range(0, 10, 2)**

- F.Q.A.
    - What data types can be stored in list? **Every data type that is defined in python by user or by default is eligible to store in list**
    - How to get reverse order of a list? **list_name.reverse() or list_name[::-1], last one gives python the instruction to get list slice and start from the last element**
    - Why does list indexing start from 0? **since python stores the address of the first element in RAM, during accessing elements python starts counting from that first element's address**


</details>

<details>
    <summary>Lecture 3</summary>

- Boolean Operators **(==, !=, >, >=, <, <=)**
    - Equality **==**
    - Inequality **!=**
    - Greater **>**
    - Greater or Equal to **>=**
    - Less **<**
    - Less or Equal to **<=**

- Flow Control **if, else**
    - conditional statement **if | else**
    - Indentation  **block of code that is executed if statement is satisfied**

- Loops **while**
    - syntax **while something is True**
    - Indentation **Block of code that get executed in while loop**

- Data Structures **tuple**
    - how to define tuple with brackets or commas?

- Using knowledge **Guessing Game**
    - generating random number **random module**
    - Infinite Loops
    - getting user input on every iteration
    - checking input for correctness
    - adding new features (try count, automatic lose after specific amount of tries)

- Challenge **Reversed Guessing Game** 
    - User thinks of the number and computer should guess it!`


</details>

<details>
    <summary>Lecture 4</summary>

- Statement Chaining **if elif else**
    - Using Multiple elif Blocks
    - Omitting the else Block
    - Testing Multiple Conditions

- Data Structures **dict**
    - Accessing Values in a Dictionary 
    - Adding New Key-Value Pairs
    - Starting with an Empty Dictionary
    - Modifying Values in a Dictionary 
    - Removing Key-Value Pairs
    - Using get() to Access Values
    - A Dictionary of Similar Objects
    - Looping Through All Key-Value Pairs
    - Looping Through All the Keys in a Dictionary
    - Looping Through All Values in a Dictionary
    - A List of Dictionaries
    - A List in a Dictionary
    - A Dictionary in a Dictionary

- Type Hinting / Annotations
    - Differences within type hinting in python versions
    - type hinting for single values
    - type hinting for data structures
    - type hinting dictionary VS TypedDict
    - Any Type
    - None Type

</details>

<details>
    <summary>Lecture 5</summary>

- Functions **def**
    - Defining a Function
    - Calling a Function
    - Passing Information to a Function
    - Arguments vs Parameters
    - Passing Arguments
        - Positional Arguments
        - Keyword Arguments
    - Default Values
    - Equivalent Function Calls
    - Avoiding Argument Errors
    - Return Values
    - Making an Argument Optional
    - Passing an Arbitrary Number of Arguments **args**
        - Mixing Positional and Arbitrary Arguments
    - Using Arbitrary Keyword Arguments **kwargs**


</details>


<details>
    <summary>Lecture 6</summary>
- Scopes
    - Local Scope Variable
    - Global Scope Variable

- Modules
    - Storing Your Functions in Modules
    - Importing an Entire Module
    - Importing Specific Functions
    - Using as to Give a Function an Alias **as**
    - Using as to Give a Module an Alias
    - Importing All Functions in a Module

- List Comprehension
    - Syntax
    - Using conditional statement

- Introduction To OOP
    - Defining Class
        - init (constructor)
        - attributes
        - Custom Methods
    - Creating an object **Instantiate**
    - Using Defined Methods
    - Default values for attributes
    - Modifying attributes
    - Public, Private, Protected attributes
    - Encapsulation (Getter, Setter)



</details>

## Links
---

**Books**
- [Python Crash Course](https://en.sng1lib.org/book/4995914/5d84d3) - Python Basics
- [Django for Beginners](https://en.sng1lib.org/book/3594011/891d30) - Backend Web Development with Python


**Youtube Channels**
- [Tech With Tim](https://www.youtube.com/c/TechWithTim) - Python Related content
- [Computerphile](https://www.youtube.com/user/Computerphile) - Computer Science Related Content



**Quizes**
- [Quiz 1](https://forms.gle/iTXu5ZzvWKbgwdGs5)
- [Quiz 2](https://forms.gle/Z51QqGiVrXcHWiPj8)
- [Quiz 2.2](https://forms.gle/Pi7rqQHPvrQjMP6N7)
- [Quiz 3](https://forms.gle/1A3nzcqMYDZ5bt5t7)
