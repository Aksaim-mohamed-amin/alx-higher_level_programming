# 0x00. Python - Hello, World

This project is designed to help beginners get started with Python programming. It includes a series of simple Python scripts that demonstrate the classic "Hello, World" program and cover basic concepts such as variables, data types, and control structures.

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
    

## More Info

### Zen

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```


## Mandatory Tasks

- [x] 0. Run Python file : 
	
	Write a Shell script that runs a Python script.
	The Python file name will be saved in the environment variable `$PYFILE`

- [x] 1. Run inline : 

	Write a Shell script that runs Python code.

	The Python code will be saved in the environment variable `$PYCODE`

- [x] 2. Hello, print : 

	Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
	-   Use the function `print`

- [x] 3. Print integer : 

	Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py "here")
	-   The output of the script should be:
	    -   the number, followed by `Battery street`,
	    -   followed by a new line
	-   You are not allowed to cast the variable `number` into a string
	-   Your code must be 3 lines long
	-   You have to use f-strings [tips](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ "tips")

- [x] 4. Print float :

	Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py "here")
	-   The output of the program should be:
	    -   `Float:`, followed by the float with only 2 digits
	    -   followed by a new line
	-   You are not allowed to cast `number` to string
	-   You have to use f-strings

- [x] 5. Print string : 

	Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py "source code") in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py "here")
	-   The output of the program should be:
	    -   3 times the value of `str`
	    -   followed by a new line
	    -   followed by the 9 first characters of `str`
	    -   followed by a new line
	-   You are not allowed to use any loops or conditional statement
	-   Your program should be maximum 5 lines long

- [x] 6. Play with strings : 

	Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py "source code") to print `Welcome to Holberton School!`

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py "here")
	-   You are not allowed to use any loops or conditional statements.
	-   You have to use the variables `str1` and `str2` in your new line of code
	-   Your program should be exactly 5 lines long

- [x] 7. Copy - Cut - Paste : 

	Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py "source code")

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py "here")
	-   You are not allowed to use any loops or conditional statements
	-   Your program should be exactly 8 lines long
	-   `word_first_3` should contain the first 3 letters of the variable `word`
	-   `word_last_2` should contain the last 2 letters of the variable `word`
	-   `middle_word` should contain the value of the variable `word` without the first and last letters

- [x] 8. Create a new sentence : 

	Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py "source code") to print `object-oriented programming with Python`, followed by a new line.

	-   You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py "here")
	-   You are not allowed to use any loops or conditional statements
	-   Your program should be exactly 5 lines long
	-   You are not allowed to create new variables
	-   You are not allowed to use string literals

- [x] 9. Easter Egg : 

	Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

	-   Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

- [x] 10. Linked list cycle : 

	**Technical interview preparation**:

	-   You are not allowed to google anything
	-   Whiteboard first
	-   This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

	Write a function in C that checks if a singly linked list has a cycle in it.

	-   Prototype: `int check_cycle(listint_t *list);`
	-   Return: `0` if there is no cycle, `1` if there is a cycle

	Requirements:

	-   Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

```
carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
```
```
carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```
```
carrie@ubuntu:~/0x00$ cat 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
```
## Advanced Tasks

- [x] 11. Hello, write : 

	 Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

	-   Use the function `write` from the `sys` module
	-   You are not allowed to use `print`
	-   Your script should print to `stderr`
	-   Your script should exit with the status code `1`

- [x] 12. Compile :

	Write a script that compiles a Python script file.

	The Python file name will be stored in the environment variable `$PYFILE`

	The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)


- [x] 10. ByteCode -> Python #1:

	Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

	```
	  3           0 LOAD_CONST               1 (98)
	              3 LOAD_FAST                0 (a)
	              6 LOAD_FAST                1 (b)
	              9 BINARY_POWER
	             10 BINARY_ADD
	             11 RETURN_VALUE

	```

	-   Tip: [Python bytecode](https://intranet.alxswe.com/rltoken/B38QeZHREbvgq-wY7Ze3vQ "Python bytecode")

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.