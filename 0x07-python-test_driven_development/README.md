# 0x07 - Python Test-Driven Development (TDD)

The "0x07 - Python Test-Driven Development (TDD)" project is focused on learning and applying Test-Driven Development principles in Python programming. Test-Driven Development is a software development approach that emphasizes writing tests for code before implementing the code itself. This process helps ensure that the code functions correctly and meets the specified requirements.

## Getting Started

Before starting this module, it is recommended that you have a basic understanding of computer programming concepts, including basic syntax, data types, and control flow statements. Additionally, you should have some familiarity with C and Python programming concepts, including variable types, functions, and the use of the gcc compiler.

## Project Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
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
-   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!



## Mandatory Tasks

- [x] 0. Integers addition : 
	
	Write a function that adds 2 integers.

	-   Prototype:  `def add_integer(a, b=98):`
	-   `a`  and  `b`  must be integers or floats, otherwise raise a  `TypeError`  exception with the message  `a must be an integer`  or  `b must be an integer`
	-   `a`  and  `b`  must be first casted to integers if they are float
	-   Returns an integer: the addition of  `a`  and  `b`
	-   You are not allowed to import any module

- [x] 1. Divide a matrix : 

	Write a function that divides all elements of a matrix.

	-   Prototype:  `def matrix_divided(matrix, div):`
	-   `matrix`  must be a list of lists of integers or floats, otherwise raise a  `TypeError`  exception with the message  `matrix must be a matrix (list of lists) of integers/floats`
	-   Each row of the  `matrix`  must be of the same size, otherwise raise a  `TypeError`  exception with the message  `Each row of the matrix must have the same size`
	-   `div`  must be a number (integer or float), otherwise raise a  `TypeError`  exception with the message  `div must be a number`
	-   `div`  can’t be equal to  `0`, otherwise raise a  `ZeroDivisionError`  exception with the message  `division by zero`
	-   All elements of the matrix should be divided by  `div`, rounded to 2 decimal places
	-   Returns a new matrix
	-   You are not allowed to import any module

- [x] 2. Say my name : 

	Write a function that prints  `My name is <first name> <last name>`

	-   Prototype:  `def say_my_name(first_name, last_name=""):`
	-   `first_name`  and  `last_name`  must be strings otherwise, raise a  `TypeError`  exception with the message  `first_name must be a string`  or  `last_name must be a string`
	-   You are not allowed to import any module

- [x] 3. Print square : 

	Write a function that prints a square with the character  `#`.

	-   Prototype:  `def print_square(size):`
	-   `size`  is the size length of the square
	-   `size`  must be an integer, otherwise raise a  `TypeError`  exception with the message  `size must be an integer`
	-   if  `size`  is less than  `0`, raise a  `ValueError`  exception with the message  `size must be >= 0`
	-   if  `size`  is a float and is less than 0, raise a  `TypeError`  exception with the message  `size must be an integer`
	-   You are not allowed to import any module

- [x] 4. Text indentation :

	Write a function that prints a text with 2 new lines after each of these characters:  `.`,  `?`  and  `:`

	-   Prototype:  `def text_indentation(text):`
	-   `text`  must be a string, otherwise raise a  `TypeError`  exception with the message  `text must be a string`
	-   There should be no space at the beginning or at the end of each printed line
	-   You are not allowed to import any module

- [x] 5. Max integer - Unittest : 

	Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

	In this task, you will write unittests for the function  `def max_integer(list=[]):`.

	-   Your test file should be inside a folder  `tests`
	-   You have to use the  [unittest module](https://intranet.alxswe.com/rltoken/hX5a13o-1mXGTQASWBitFQ "unittest module")
	-   Your test file should be python files (extension:  `.py`)
	-   Your test file should be executed by using this command:  `python3 -m unittest tests.6-max_integer_test`
	-   All tests you make must be passable by the function below
	-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case


## Advanced Tasks

- [x] 6. Matrix multiplication :
	
	Write a function that multiplies 2 matrices:

	-   Read:  [Matrix multiplication - only Matrix product (two matrices)](https://intranet.alxswe.com/rltoken/Qw_rYR3lYYL5DHDH-iCWCA "Matrix multiplication - only Matrix product (two matrices)")
	    
	-   Prototype:  `def matrix_mul(m_a, m_b):`
	    
	-   `m_a`  and  `m_b`  must be validated with these requirements in this order
	    
	-   `m_a`  and  `m_b`  must be an list of lists of integers or floats:
	    
	    -   if  `m_a`  or  `m_b`  is not a list: raise a  `TypeError`  exception with the message  `m_a must be a list`  or  `m_b must be a list`
	    -   if  `m_a`  or  `m_b`  is not a list of lists: raise a  `TypeError`  exception with the message  `m_a must be a list of lists`  or  `m_b must be a list of lists`
	    -   if  `m_a`  or  `m_b`  is empty (it means:  `= []`  or  `= [[]]`): raise a  `ValueError`  exception with the message  `m_a can't be empty`  or  `m_b can't be empty`
	    -   if one element of those list of lists is not an integer or a float: raise a  `TypeError`  exception with the message  `m_a should contain only integers or floats`  or  `m_b should contain only integers or floats`
	    -   if  `m_a`  or  `m_b`  is not a rectangle (all ‘rows’ should be of the same size): raise a  `TypeError`  exception with the message  `each row of m_a must be of the same size`  or  `each row of m_b must be of the same size`
	-   If  `m_a`  and  `m_b`  can’t be multiplied: raise a  `ValueError`  exception with the message  `m_a and m_b can't be multiplied`
	    
	-   You are not allowed to import any module

- [x] 7. Lazy matrix multiplication :

	Write a function that multiplies 2 matrices by using the module  [NumPy](https://intranet.alxswe.com/rltoken/sXnBuOVSyhKEGt-biOyOWg "NumPy")

	To install it:  `pip3 install numpy==1.15.0`

	-   Prototype:  `def lazy_matrix_mul(m_a, m_b):`
	-   Test cases should be the same as  `100-matrix_mul`  but with new exception type/message

- [x] 8. CPython #3: Python Strings :

	Create a function that prints Python strings.

	-   Prototype:  `void print_python_string(PyObject *p);`
	-   Format: see example
	-   If  `p`  is not a valid string, print an error message (see example)
	-   Read:  [Unicode HOWTO](https://intranet.alxswe.com/rltoken/UkkHHaILiYf9d_a3nc4Bxw "Unicode HOWTO")

	About:

	-   Python version: 3.4
	-   You are allowed to use the C standard library
	-   Your shared library will be compiled with this command line:  `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

	```
	julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
	import ctypes

	lib = ctypes.CDLL('./libPython.so')
	lib.print_python_string.argtypes = [ctypes.py_object]
	s = "The spoon does not exist"
	lib.print_python_string(s)
	s = "ложка не существует"
	lib.print_python_string(s)
	s = "La cuillère n'existe pas"
	lib.print_python_string(s)
	s = "勺子不存在"
	lib.print_python_string(s)
	s = "숟가락은 존재하지 않는다."
	lib.print_python_string(s)
	s = "スプーンは存在しない"
	lib.print_python_string(s)
	s = b"The spoon does not exist"
	lib.print_python_string(s)
	julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
	julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
	[.] string object info
	  type: compact ascii
	  length: 24
	  value: The spoon does not exist
	[.] string object info
	  type: compact unicode object
	  length: 19
	  value: ложка не существует
	[.] string object info
	  type: compact unicode object
	  length: 24
	  value: La cuillère n'existe pas
	[.] string object info
	  type: compact unicode object
	  length: 5
	  value: 勺子不存在
	[.] string object info
	  type: compact unicode object
	  length: 14
	  value: 숟가락은 존재하지 않는다.
	[.] string object info
	  type: compact unicode object
	  length: 10
	  value: スプーンは存在しない
	[.] string object info
	  [ERROR] Invalid String Object
	julien@ubuntu:~/0x07. Pyhton Strings$ 
	```

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
