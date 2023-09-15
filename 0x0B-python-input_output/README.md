
# 0x0B. Python - Input/Output

Welcome to the "0x0B. Python - Input/Output" project, where you will learn about handling input and output in Python. This project covers various aspects of reading and writing data in Python, including working with files, standard input/output, and more.


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


## Mandatory Tasks

- [x] 0. Read file : 
	
	Write a function that reads a text file (`UTF8`) and prints it to stdout:

	-   Prototype:  `def read_file(filename=""):`
	-   You must use the  `with`  statement
	-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
	-   You are not allowed to import any module

- [x] 1. Write to a file : 

	Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

	-   Prototype:  `def write_file(filename="", text=""):`
	-   You must use the  `with`  statement
	-   You don’t need to manage file permission exceptions.
	-   Your function should create the file if doesn’t exist.
	-   Your function should overwrite the content of the file if it already exists.
	-   You are not allowed to import any module

- [x] 2. Append to a file : 
	
	Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

	-   Prototype:  `def append_write(filename="", text=""):`
	-   If the file doesn’t exist, it should be created
	-   You must use the  `with`  statement
	-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
	-   You are not allowed to import any module

- [x] 3. To JSON string : 

	Write a function that returns the JSON representation of an object (string):

	-   Prototype:  `def to_json_string(my_obj):`
	-   You don’t need to manage exceptions if the object can’t be serialized.

- [x] 4. From JSON string to Object :

	Write a function that returns an object (Python data structure) represented by a JSON string:

	-   Prototype:  `def from_json_string(my_str):`
	-   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	
- [x] 5. Save Object to a file : 
	
	Write a function that writes an Object to a text file, using a JSON representation:

	-   Prototype:  `def save_to_json_file(my_obj, filename):`
	-   You must use the  `with`  statement
	-   You don’t need to manage exceptions if the object can’t be serialized.
	-   You don’t need to manage file permission exceptions.
	
- [x] 6. Create object from a JSON file :

	Write a function that creates an Object from a “JSON file”:

	-   Prototype:  `def load_from_json_file(filename):`
	-   You must use the  `with`  statement
	-   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	-   You don’t need to manage file permissions / exceptions.

- [x] 7. Load, add, save :
	Write a script that adds all arguments to a Python list, and then save them to a file:

	-   You must use your function  `save_to_json_file`  from  `5-save_to_json_file.py`
	-   You must use your function  `load_from_json_file`  from  `6-load_from_json_file.py`
	-   The list must be saved as a JSON representation in a file named  `add_item.json`
	-   If the file doesn’t exist, it should be created
	-   You don’t need to manage file permissions / exceptions.
	
- [x] 8. Class to JSON :

	Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

	-   Prototype:  `def class_to_json(obj):`
	-   `obj`  is an instance of a Class
	-   All attributes of the  `obj`  Class are serializable: list, dictionary, string, integer and boolean
	-   You are not allowed to import any module

- [x] 9. Student to JSON :

	Write a class  `Student`  that defines a student by:

	-   Public instance attributes:
	    -   `first_name`
	    -   `last_name`
	    -   `age`
	-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
	-   Public method  `def to_json(self):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`)
	-   You are not allowed to import any module

- [x] 10. Student to JSON with filter :

	Write a class  `Student`  that defines a student by: (based on  `9-student.py`)

	-   Public instance attributes:
	    -   `first_name`
	    -   `last_name`
	    -   `age`
	-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
	-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
	    -   If  `attrs`  is a list of strings, only attribute names contained in this list must be retrieved.
	    -   Otherwise, all attributes must be retrieved
	-   You are not allowed to import any module

- [x] 11. Student to disk and reload :
	
	Write a class  `Student`  that defines a student by: (based on  `10-student.py`)

	-   Public instance attributes:
	    -   `first_name`
	    -   `last_name`
	    -   `age`
	-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
	-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
	    -   If  `attrs`  is a list of strings, only attributes name contain in this list must be retrieved.
	    -   Otherwise, all attributes must be retrieved
	-   Public method  `def reload_from_json(self, json):`  that replaces all attributes of the  `Student`  instance:
	    -   You can assume  `json`  will always be a dictionary
	    -   A dictionary key will be the public attribute name
	    -   A dictionary value will be the value of the public attribute
	-   You are not allowed to import any module

	Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

- [x] 12. Pascal's Triangle :
	**Technical interview preparation**:

	-   You are not allowed to google anything
	-   Whiteboard first

	Create a function  `def pascal_triangle(n):`  that returns a list of lists of integers representing the Pascal’s triangle of  `n`:

	-   Returns an empty list if  `n <= 0`
	-   You can assume  `n`  will be always an integer
	-   You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x0B$ cat 12-main.py
	#!/usr/bin/python3
	"""
	12-main
	"""
	pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

	def print_triangle(triangle):
	    """
	    Print the triangle
	    """
	    for row in triangle:
	        print("[{}]".format(",".join([str(x) for x in row])))


	if __name__ == "__main__":
	    print_triangle(pascal_triangle(5))

	guillaume@ubuntu:~/0x0B$ 
	guillaume@ubuntu:~/0x0B$ ./12-main.py
	[1]
	[1,1]
	[1,2,1]
	[1,3,3,1]
	[1,4,6,4,1]
	guillaume@ubuntu:~/0x0B$ 
	```

## Advanced Tasks

- [x] 13. Search and update :

	Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

	-   Prototype:  `def append_after(filename="", search_string="", new_string=""):`
	-   You must use the  `with`  statement
	-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
	-   You are not allowed to import any module

	```
	guillaume@ubuntu:~/0x0B$ cat 100-main.py
	#!/usr/bin/python3
	append_after = __import__('100-append_after').append_after

	append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At Holberton School,
	Python is really important,
	But it can be very hard if:
	- You don't get all Pythonic tricks
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ ./100-main.py
	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At School,
	Python is really important,
	"C is fun!"
	But it can be very hard if:
	- You don't get all Pythonic tricks
	"C is fun!"
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ ./100-main.py
	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At School,
	Python is really important,
	"C is fun!"
	"C is fun!"
	But it can be very hard if:
	- You don't get all Pythonic tricks
	"C is fun!"
	"C is fun!"
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ 
	```
- [x] 14. Log parsing :

	Write a script that reads  `stdin`  line by line and computes metrics:

	-   Input format:  `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
	-   Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
	    -   Total file size:  `File size: <total size>`
	    -   where  is the sum of all previous  (see input format above)
	    -   Number of lines by status code:
	        -   possible status code:  `200`,  `301`,  `400`,  `401`,  `403`,  `404`,  `405`  and  `500`
	        -   if a status code doesn’t appear, don’t print anything for this status code
	        -   format:  `<status code>: <number>`
	        -   status codes should be printed in ascending order

	```
	guillaume@ubuntu:~/0x0B$ cat 101-generator.py
	#!/usr/bin/python3
	import random
	import sys
	from time import sleep
	import datetime

	for i in range(10000):
	    sleep(random.random())
	    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
	        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
	        datetime.datetime.now(),
	        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
	        random.randint(1, 1024)
	    ))
	    sys.stdout.flush()

	guillaume@ubuntu:~/0x0B$ ./101-generator.py | ./101-stats.py 
	File size: 5213
	200: 2
	401: 1
	403: 2
	404: 1
	405: 1
	500: 3
	File size: 11320
	200: 3
	301: 2
	400: 1
	401: 2
	403: 3
	404: 4
	405: 2
	500: 3
	File size: 16305
	200: 3
	301: 3
	400: 4
	401: 2
	403: 5
	404: 5
	405: 4
	500: 4
	^CFile size: 17146
	200: 4
	301: 3
	400: 4
	401: 2
	403: 6
	404: 6
	405: 4
	500: 4
	Traceback (most recent call last):
	  File "./101-stats.py", line 15, in <module>
	Traceback (most recent call last):
	  File "./101-generator.py", line 8, in <module>
	    for line in sys.stdin:
	KeyboardInterrupt
	    sleep(random.random())
	KeyboardInterrupt
	guillaume@ubuntu:~/0x0B$ 
	```

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.

