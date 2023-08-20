
# 0x02. Python - Import & Modules

Welcome to the "0x02. Python - Import & Modules" repository! In this module, we will explore the concepts of importing modules and working with them in Python. Understanding how to effectively organize and use modules is essential for writing modular and maintainable code.

## Getting Started

Before starting this module, it is recommended that you have a basic understanding of computer programming concepts, including basic syntax, data types, and control flow statements. Additionally, you should have some familiarity with C and Python programming concepts, including variable types, functions, and the use of the gcc compiler.

## Project Requirements

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file at the root of the repo, containing a description of the repository
-   A `README.md` file, at the root of the folder of _this_ project, is mandatory
-   Your code should use the pycodestyle (version `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using `wc`

### Shell Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`wc -l file` should print 2)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/bin/bash`
-   All your files must be executable

### C Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
-   All your files should end with a new line
-   Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl "betty-style.pl") and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl "betty-doc.pl")
-   You are not allowed to use global variables
-   No more than 5 functions per file
-   In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
-   The prototypes of all your functions should be included in your header file called `lists.h`
-   Don’t forget to push your header file
-   All your header files should be include guarded
    

## Mandatory Tasks

- [x] 0. Import a simple function from a simple file : 
	
	Write a program that imports the function  `def add(a, b):`  from the file  `add_0.py`  and prints the result of the addition  `1 + 2 = 3`

	-   You have to use  `print`  function with string format to display integers
	-   You have to assign:
	    -   the value  `1`  to a variable called  `a`
	    -   the value  `2`  to a variable called  `b`
	    -   and use those two variables as arguments when calling the functions  `add`  and  `print`
	-   `a`  and  `b`  must be defined in 2 different lines:  `a = 1`  and another  `b = 2`
	-   Your program should print:  `<a value> + <b value> = <add(a, b) value>`  followed with a new line
	-   You can only use the word  `add_0`  once in your code
	-   You are not allowed to use  `*`  for importing or  `__import__`
	-   Your code should not be executed when imported - by using  `__import__`, like the example below

- [x] 1. My first toolbox! : 

	Write a program that imports functions from the file  `calculator_1.py`, does some Maths, and prints the result.

	-   Do not use the function  `print`  (with string format to display integers) more than 4 times
	-   You have to define:
	    -   the value  `10`  to a variable  `a`
	    -   the value  `5`  to a variable  `b`
	    -   and use those two variables only, as arguments when calling functions (including  `print`)
	-   `a`  and  `b`  must be defined in 2 different lines:  `a = 10`  and another  `b = 5`
	-   Your program should call each of the imported functions. See example below for format
	-   the word  `calculator_1`  should be used only once in your file
	-   You are not allowed to use  `*`  for importing or  `__import__`
	-   Your code should not be executed when imported

- [x] 2. How to make a script dynamic! : 

	Write a program that prints the number of and the list of its arguments.

	-   The output should be:
	    -   Number of argument(s) followed by  `argument`  (if number is one) or  `arguments`  (otherwise), followed by
	    -   `:`  (or  `.`  if no arguments were passed) followed by
	    -   a new line, followed by (if at least one argument),
	    -   one line per argument:
	        -   the position of the argument (starting at  `1`) followed by  `:`, followed by the argument value and a new line
	-   Your code should not be executed when imported
	-   The number of elements of  `argv`  can be retrieved by using:  `len(argv)`
	-   You do not have to fully understand lists yet, but imagine that  `argv`  can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

- [x] 3. Infinite addition : 

	Write a program that prints the result of the addition of all arguments

	-   The output should be the result of the addition of all arguments, followed by a new line
	-   You can cast arguments into integers by using  `int()`  (you can assume that all arguments can be casted into integers)
	-   Your code should not be executed when imported

- [x] 4. Who are you? :

	Write a program that prints all the names defined by the compiled module  [hidden_4.pyc](https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc "hidden_4.pyc")  (please download it locally).

	-   You should print one name per line, in alpha order
	-   You should print only names that do  **not**  start with  `__`
	-   Your code should not be executed when imported
	-   Make sure you are running your code in Python3.8.x (`hidden_4.pyc`  has been compiled with this version)

- [x] 5. Everything can be imported : 

	Write a program that imports the variable  `a`  from the file  `variable_load_5.py`  and prints its value.

	-   You are not allowed to use  `*`  for importing or  `__import__`
	-   Your code should not be executed when imported


## Advanced Tasks

- [x] 6. Build my own calculator! : 

	Write a program that imports all functions from the file  `calculator_1.py`  and handles basic operations.

	-   Usage:  `./100-my_calculator.py a operator b`
	    -   If the number of arguments is not 3, your program has to:
	        -   print  `Usage: ./100-my_calculator.py <a> <operator> <b>`  followed with a new line
	        -   exit with the value  `1`
	    -   `operator`  can be:
	        -   `+`  for addition
	        -   `-`  for subtraction
	        -   `*`  for multiplication
	        -   `/`  for division
	    -   If the operator is not one of the above:
	        -   print  `Unknown operator. Available operators: +, -, * and /`  followed with a new line
	        -   exit with the value  `1`
	    -   You can cast  `a`  and  `b`  into integers by using  `int()`  (you can assume that all arguments will be castable into integers)
	    -   The result should be printed like this:  `<a> <operator> <b> = <result>`, followed by a new line
	-   You are not allowed to use  `*`  for importing or  `__import__`
	-   Your code should not be executed when imported

- [x] 7. Easy print :

	Write a program that prints  `#pythoniscool`, followed by a new line, in the standard output.

	-   Your program should be maximum 2 lines long
	-   You are not allowed to use  `print`  or  `eval`  or  `open`  or  `import sys`  in your file  `101-easy_print.py`

- [x] 8. ByteCode -> Python #3 :

	Write the Python function  `def magic_calculation(a, b):`  that does exactly the same as the following Python bytecode:

	```
	  3           0 LOAD_CONST               1 (0)
	              3 LOAD_CONST               2 (('add', 'sub'))
	              6 IMPORT_NAME              0 (magic_calculation_102)
	              9 IMPORT_FROM              1 (add)
	             12 STORE_FAST               2 (add)
	             15 IMPORT_FROM              2 (sub)
	             18 STORE_FAST               3 (sub)
	             21 POP_TOP

	  4          22 LOAD_FAST                0 (a)
	             25 LOAD_FAST                1 (b)
	             28 COMPARE_OP               0 (<)
	             31 POP_JUMP_IF_FALSE       94

	  5          34 LOAD_FAST                2 (add)
	             37 LOAD_FAST                0 (a)
	             40 LOAD_FAST                1 (b)
	             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             46 STORE_FAST               4 (c)

	  6          49 SETUP_LOOP              38 (to 90)
	             52 LOAD_GLOBAL              3 (range)
	             55 LOAD_CONST               3 (4)
	             58 LOAD_CONST               4 (6)
	             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             64 GET_ITER
	        >>   65 FOR_ITER                21 (to 89)
	             68 STORE_FAST               5 (i)

	  7          71 LOAD_FAST                2 (add)
	             74 LOAD_FAST                4 (c)
	             77 LOAD_FAST                5 (i)
	             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             83 STORE_FAST               4 (c)
	             86 JUMP_ABSOLUTE           65
	        >>   89 POP_BLOCK

	  8     >>   90 LOAD_FAST                4 (c)
	             93 RETURN_VALUE

	 10     >>   94 LOAD_FAST                3 (sub)
	             97 LOAD_FAST                0 (a)
	            100 LOAD_FAST                1 (b)
	            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	            106 RETURN_VALUE
	            107 LOAD_CONST               0 (None)
	            110 RETURN_VALUE

	```

	-   Tip:  [Python bytecode](https://intranet.alxswe.com/rltoken/FMdg7W8NKJZKRuFGG8mzmg "Python bytecode")

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
