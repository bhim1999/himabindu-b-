1. What is Python?
Python is an interpreted scripting language that is known for its power, interactivity, and object-oriented nature. It utilizes English keywords extensively and has a simpler syntax compared to many other programming languages.
Python is designed to be highly readable and compatible with different platforms such as Mac, Windows, Linux, Raspberry Pi, etc.
2. Python is an interpreted language. Explain.
An interpreted programming language refers to any language that executes its instructions sequentially, one line at a time. In the case of Python, programs are executed directly from the source code without the need for any intermediate compilation process.

3. What distinguishes lists from tuples?
Lists	Tuples
Lists are mutable, i.e., they can be edited	Tuples possess immutability, denoting their incapability of being modified like lists.
Lists are usually slower than tuples	Tuples are faster than lists
Lists consume a lot of memory	Tuples consume less memory when compared to lists
Lists have a higher likelihood of experiencing unexpected changes, making them less reliable in terms of errors.	Tuples offer increased reliability due to their resistance to unexpected modifications.
Lists consist of many built-in functions.	Tuples do not consist of any built-in functions.
Syntax:
list_1 = [10, ‘Intellipaat’, 20]

Syntax:
tup_1 = (10, ‘Intellipaat’ , 20)

4. What is pep 8?
PEP in Python stands for Python Enhancement Proposal. It comprises a collection of guidelines that outline the optimal approach for crafting and structuring Python code to ensure the utmost clarity and legibility.

5. What are the Key features of Python?
The key features of Python are as follows:

Python Features
Python is an interpreted language, so it doesn’t need to be compiled before execution, unlike languages such as C.
Python is dynamically typed, so there is no need to declare a variable with the data type. Python Interpreter will identify the data type on the basis of the value of the variable.
For example, in Python, the following code line will run without any error:

a = 100
a = "Intellipaat"
Python follows an object-oriented programming paradigm with the exception of having access specifiers. Other than access specifiers (public and private keywords), Python has classes, inheritance, and all other usual OOPs concepts.
Python is a cross-platform language, i.e., a Python program written on a Windows system will also run on a Linux system with little or no modifications at all.
Python is literally a general-purpose language, i.e., Python finds its way in various domains such as web application development, automation, Data Science, Machine Learning, and more.
Go through the Python Course in London to get a clear understanding of Python and become a Python developer today!

6. How is Memory managed in Python?
Python makes use of automatic memory management through garbage collection.
The garbage collector keeps track of objects and frees memory when they are no longer in use.
Python uses reference counting to manage memory, incrementing and decrementing reference counts as needed.
A cyclic garbage collector handles objects with circular references.
Python also provides tools like context managers and the “with” statement to release resources automatically.
Python’s memory management simplifies coding by handling memory allocation and deallocation automatically.
To become a professional business analyst, check out Intellipaat’s Business Analyst Certification Course in Bangalore taught by industry experts.

7. What is PYTHONPATH?
PYTHONPATH serves as an environment variable within the Python programming language, empowering users to define supplementary directories for Python to search when seeking modules and packages. This variable serves as a search path and helps Python locate the necessary files to import when executing code. By setting the PYTHONPATH variable, users can extend the default search path and customize the module search behavior according to their needs. This feature enables developers to organize and structure their Python projects efficiently, facilitating easier module importation and enhancing code reusability.

8. What are Python Modules?
Files containing Python codes are referred to as Python modules. This code can  be of different types like classes, functions, or variables. This saves the programmer’s time by providing predefined functionalities when needed. It is a file with “.py” extension containing an executable code.

Commonly used built modules are listed below:

os
sys
data time
math
random
JSON
9. What are python namespaces?
A Python namespace ensures that the names assigned to objects within a program are unique and can be used without conflict. In Python, namespaces are implemented as dictionaries where the object’s name serves as the key and the object itself serves as the value.

Let’s examine some examples of namespaces:

The Local Namespace is specific to a function and contains the names defined within that function. It is created temporarily when the function is called and is cleared once the function finishes executing.
The Global Namespace includes names from imported modules or packages that are used in the current project. It is created when the package is imported into the script and remains accessible throughout the script’s execution.
The Built-in Namespace comprises the built-in functions provided by Python’s core, as well as specific names dedicated to various types of exceptions.
Want to become a master in Python programming? Check out this Python Training for Data Science and excel in your Python career!

10. Explain Inheritance in Python with an example?
Python embraces the principles of object-oriented programming and allows classes to acquire the characteristics of another class, a concept known as inheritance. This facilitates code reuse, promoting efficiency. The original class from which properties are inherited is referred to as the superclass or parent class, while the class inheriting those properties is known as the derived or child class. Python supports various types of inheritance, including the following:

Inheritance in Python
Multiple Inheritance: Python supports multiple inheritance, enabling a derived class to inherit attributes and methods from multiple parent classes, facilitating code reuse and enhancing flexibility.
Multilevel Inheritance: With multilevel inheritance, a derived class inherits properties and methods from a parent class, which in turn inherits from another parent class, establishing a hierarchical relationship between classes.
Hierarchical Inheritance: In hierarchical inheritance, multiple classes inherit properties and methods from a common superclass, resulting in a tree-like structure where each derived class has its own specialized functionality.
Single Inheritance: In Python, single inheritance allows a derived class to inherit properties and methods from a single superclass, promoting code reuse and organizational structure.
Hybrid Inheritance: Hybrid inheritance combines different types of inheritance, such as single, multiple, or multilevel inheritance, to create complex class hierarchies that fulfill specific programming requirements, ensuring maximum code reuse and flexibility.
Career Transition

11. What is scope resolution?
In Python, a scope defines the region of code where an object remains valid and accessible. Every object in Python operates within its designated scope. Namespaces are used to uniquely identify objects within a program, and each namespace is associated with a specific scope where objects can be used without any prefix. The scope of a variable determines its accessibility and lifespan.

Let’s explore the different scopes created during code execution:

Local scope: This refers to the objects that are defined within the current function and are accessible only within that function.
Global scope: Objects in the global scope are available throughout the execution of the code. 
Module-level scope: This scope encompasses global objects that are associated with the current module in the program. These objects are accessible within the module.
Outermost scope: This refers to all the built-in names that can be called from anywhere in the program.
Interested in learning React JS? Click here to learn more about this React JS Certification!

12. What is a dictionary in Python?
Python supports various data types, including dictionaries. A dictionary in Python is a collection of elements that are stored as key-value pairs. It is an unordered data structure, and the indexing is done based on the keys assigned to each element. Let’s consider an example: we have a dictionary named ‘dict’ with two keys, ‘Country’ and ‘Capital’, which have corresponding values ‘India’ and ‘New Delhi’, respectively.

Syntax:

dict={‘Country’:’India’,’Capital’:’New Delhi’, }
Output: Country: India, Capital: New Delhi

13. What are functions in Python?
A function is a segment of code that runs only when it is called. The “def” keyword is utilized to define a specific function, as exemplified below:

def my_function():
    print("Hi, Welcome to Intellipaat")
my_function()  # call to the function
Output:
Hi, Welcome to Intellipaat

14. What is __init__ in Python?
In Python classes, the reserved method init serves a similar purpose as constructors in object-oriented programming (OOP) terminology. When a new object is created, the init method is automatically called, initializing the object and allocating memory for it. This method can also be utilized to set initial values for variables.

Below is an example:

class Human:
    def __init__(self, age):
        self.age = age
    def say(self):
        print('Hello, my age is', self.age)
h = Human(22)
h.say()
Output:

Hello, my age is 22

15. What are the common built-in data types in Python?
Python supports the below-mentioned built-in data types:

Immutable data types:

Number
String
Tuple
Mutable data types:

List
Dictionary
set
Watch this Video on Python for Data Science Tutorial

Youtube subscribe
16. What are local variables and global variables in Python?
A local variable is a variable that is defined within a specific function and is only accessible within that function. It cannot be accessed by other functions within the program.

In contrast, a global variable is a variable that is declared outside of any function, allowing it to be accessed by all functions in the program

g=4 #global variable
def func_multiply():
l=5 #local variable
m=g*l
return m
func_multiply()
Output: 20

If you attempt to access the local variable outside the func_multiply function, you will encounter an error.

Become a Data Science engineer with expertise in Python. Enroll in Data Science with Python training in Philippines

17. What is type conversion in Python?
Python offers a valuable feature that allows for the conversion of data types as needed. This process is referred to as type conversion in Python.

Type conversion can be divided into two types:

Implicit Type Conversion: This type of conversion is automatically performed by the Python interpreter without requiring any user intervention.

Explicit Type Conversion: This type of conversion involves the user explicitly changing the data type to the desired type.

Below are several functions for explicit type conversion:

int(): This function converts any data type to an integer.

float(): This function converts any data type to a float.

ord(): This function returns an integer representing the Unicode character.

hex(): This function converts integers to hexadecimal strings.

oct(): This function converts integers to octal strings.

tuple(): This function converts a value to a tuple.

set(): This function returns the type after converting to a set.

list(): This function converts any data type to a list.

dict(): This function is used to convert a tuple of key-value pairs into a dictionary.

str(): This function is used to convert an integer into a string.

complex(real, imag): This function is used to convert real numbers to complex numbers in the form of complex(real, imag).

18. How to install Python on Windows and set a path variable?
To install Python on Windows and set a path variable, follow the steps below:

 

Download Python:

 

Visit the official Python website at www.python.org.
Click on the “Downloads” tab.
Choose the latest version of Python for Windows.
Select the appropriate installer based on your system (32-bit or 64-bit).
 

Run the Installer:

 

Double-click the downloaded installer.
Check the box stating “Add Python to PATH” during the installation process.
Click on the “Customize installation” option if you want to customize the installation location or components.
 

Set the Path Variable:

 

After opening the Start menu, search “Environment Variables” or “Edit the system environment variables.”
Click on the “Environment Variables” button.
Find the “Path” variable in “System Variables” and click “Edit.”
Select “New” and then provide the path to your Python installation directory. It is typically found at “C:PythonXX” (XX represents the Python version number).
Click “OK” to save the changes.
 

Verify the Installation:

 

Open a new Command Prompt window.
Type “python” and press Enter.
If Python is installed correctly, you will see the Python interpreter prompt with the version information.
Here’s the code to check the Python version using Command Prompt:

python –version

19. What is the difference between Python Arrays and lists?
Criteria	Python Arrays 	Python Lists
Definition	Arrays are data structures that hold fixed-size elements of the same type.	Lists are versatile data structures that can hold elements of different types and sizes.
Mutable	Arrays are mutable, meaning their elements can be modified once created.	Lists are mutable, allowing for modification of elements after creation.
Size	Array size is fixed upon creation and cannot be changed.	Lists can dynamically resize to accommodate new elements or remove existing elements.
Homogeneous	Arrays store elements of the same data type, ensuring homogeneity.	Lists can store elements of different data types, allowing heterogeneity.
Access	Elements in an array can be accessed using indexing.	Elements in a list can be accessed using indexing.
Operations	Arrays support mathematical and logical operations on their elements efficiently.	Lists provide a wide range of built-in methods and operations for manipulation and data handling.
Memory	Arrays consume less memory compared to lists.	Lists consume more memory due to their flexibility and dynamic resizing.
20. Is python case sensitive?
Yes, Python is a case sensitive language. In Python, it is important to note that “Function” and “function” are distinct entities, similar to how SQL and Pascal handle them differently.

Courses you may like
