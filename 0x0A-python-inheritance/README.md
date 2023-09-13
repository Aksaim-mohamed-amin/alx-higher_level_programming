
# 0x0A. Python - Inheritance

Welcome to the **0x0A. Python - Inheritance** project! This project is designed to help you understand the concept of inheritance in Python, a fundamental aspect of object-oriented programming (OOP). Inheritance allows you to create new classes that inherit properties and behaviors from existing classes. This README will guide you through the basics of inheritance and provide examples to reinforce your understanding.


## Getting Started

Before starting this module, it is recommended that you have a basic understanding of computer programming concepts, including basic syntax, data types, and control flow statements. Additionally, you should have some familiarity with C and Python programming concepts, including variable types, functions, and the use of the gcc compiler.

## Project Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a newline character
-   The first line of all your script files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version  `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`


### Python Test Cases

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   All your test files should be text files (extension:  `.txt`)
-   All your tests should be executed by using this command:  `python3 -m doctest ./tests/*`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Documentation

-   Do not use the words  `import`  or  `from`  inside your comments, the checker will think you try to import some modules


## Mandatory Tasks

- [x] 0. Lookup : 
	
	Write a function that returns the list of available attributes and methods of an object:

	-   Prototype:  `def lookup(obj):`
	-   Returns a  `list`  object
	-   You are not allowed to import any module

- [x] 1. My list : 

	Write a class  `MyList`  that inherits from  `list`:

	-   Public instance method:  `def print_sorted(self):`  that prints the list, but sorted (ascending sort)
	-   You can assume that all the elements of the list will be of type  `int`
	-   You are not allowed to import any module

- [x] 2. Exact same object : 
	
	Write a function that returns  `True`  if the object is  _exactly_  an instance of the specified class ; otherwise  `False`.

	-   Prototype:  `def is_same_class(obj, a_class):`
	-   You are not allowed to import any module
	
- [x] 3. Same class or inherit from : 

	Write a function that returns  `True`  if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise  `False`.

	-   Prototype:  `def is_kind_of_class(obj, a_class):`
	-   You are not allowed to import any module

- [x] 4. Only sub class of :

	Write a function that returns  `True`  if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise  `False`.

	-   Prototype:  `def inherits_from(obj, a_class):`
	-   You are not allowed to import any module
	
- [x] 5. Geometry module : 
	
	Write an empty class  `BaseGeometry`.

	-   You are not allowed to import any module
	
- [x] 6. Improve Geometry :

	Write a class  `BaseGeometry`  (based on  `5-base_geometry.py`).

	-   Public instance method:  `def area(self):`  that raises an  `Exception`  with the message  `area() is not implemented`
	-   You are not allowed to import any module
	
- [x] 7. Integer validator :

	Write a class  `BaseGeometry`  (based on  `6-base_geometry.py`).

	-   Public instance method:  `def area(self):`  that raises an  `Exception`  with the message  `area() is not implemented`
	-   Public instance method:  `def integer_validator(self, name, value):`  that validates  `value`:
	    -   you can assume  `name`  is always a string
	    -   if  `value`  is not an integer: raise a  `TypeError`  exception, with the message  `<name> must be an integer`
	    -   if  `value`  is less or equal to 0: raise a  `ValueError`  exception with the message  `<name> must be greater than 0`
	-   You are not allowed to import any module
	
- [x] 8. Rectangle :

	Write a class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`).

	-   Instantiation with  `width`  and  `height`:  `def __init__(self, width, height):`
	    -   `width`  and  `height`  must be private. No getter or setter
	    -   `width`  and  `height`  must be positive integers, validated by  `integer_validator`

- [x] 9. Full rectangle :

	Write a class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`). (task based on  `8-rectangle.py`)

	-   Instantiation with  `width`  and  `height`:  `def __init__(self, width, height):`:
	    -   `width`  and  `height`  must be private. No getter or setter
	    -   `width`  and  `height`  must be positive integers validated by  `integer_validator`
	-   the  `area()`  method must be implemented
	-   `print()`  should print, and  `str()`  should return, the following rectangle description:  `[Rectangle] <width>/<height>`

- [x] 10. Square #1 :

	Write a class  `Square`  that inherits from  `Rectangle`  (`9-rectangle.py`):

	-   Instantiation with  `size`:  `def __init__(self, size):`:
	    -   `size`  must be private. No getter or setter
	    -   `size`  must be a positive integer, validated by  `integer_validator`
	-   the  `area()`  method must be implemented

- [x] 11. Square #2 :

	Write a class  `Square`  that inherits from  `Rectangle`  (`9-rectangle.py`). (task based on  `10-square.py`).

	-   Instantiation with  `size`:  `def __init__(self, size):`:
	    -   `size`  must be private. No getter or setter
	    -   `size`  must be a positive integer, validated by  `integer_validator`
	-   the  `area()`  method must be implemented
	-   `print()`  should print, and  `str()`  should return, the square description:  `[Square] <width>/<height>`


## Advanced Tasks

- [x] 12. My integer :

	Write a class  `MyInt`  that inherits from  `int`:

	-   `MyInt`  is a rebel.  `MyInt`  has  `==`  and  `!=`  operators inverted
	-   You are not allowed to import any module		

- [x] 13. Can I? :

	Write a function that adds a new attribute to an object if it’s possible:

	-   Raise a  `TypeError`  exception, with the message  `can't add new attribute`  if the object can’t have new attribute
	-   You are not allowed to use  `try/except`
	-   You are not allowed to import any module


## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.

