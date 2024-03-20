
# 0x0D. SQL - Introduction

Welcome to the "0x0D. SQL - Introduction" project! In this project, I did embark on an exciting journey into the world of Structured Query Language (SQL). SQL is a powerful language used for managing and manipulating relational databases, making it an essential skill for anyone interested in data management and analysis.

## Introduction

In this project, I explored the fundamentals of SQL, including:

-   Understanding the concept of databases and their importance in storing and organizing data.
-   Exploring relational databases and their role in establishing relationships between different sets of data.
-   Discovering the significance of SQL, which stands for Structured Query Language, as the standard language for managing relational databases.
-   Getting familiar with MySQL, a popular open-source relational database management system widely used in web development and other applications.
-   Learning how to create and manage databases in MySQL, including creating tables, altering their structure, and defining relationships between them.

## Project Requirements
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 20.04 LTS using  `MySQL 8.0`  (version 8.0.25)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`


## Mandatory Tasks

- [x] 0. List databases : 

		Write a script that lists all databases of your MySQL server.

	- [x] 1. Create a database : 

	Write a script that creates the database  `hbtn_0c_0`  in your MySQL server.

	-   If the database  `hbtn_0c_0`  already exists, your script should not fail
	-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements
	
- [x] 2. Delete a database : 

	Write a script that deletes the database  `hbtn_0c_0`  in your MySQL server.

	-   If the database  `hbtn_0c_0`  doesn’t exist, your script should not fail
	-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

- [x] 3. List tables : 

	Write a script that lists all the tables of a database in your MySQL server.

	-   The database name will be passed as argument of  `mysql`  command (in the following example:  `mysql`  is the name of the database)

- [x] 4. First table :

	Write a script that creates a table called  `first_table`  in the current database in your MySQL server.

	-   `first_table`  description:
	    -   `id`  INT
	    -   `name`  VARCHAR(256)
	-   The database name will be passed as an argument of the  `mysql`  command
	-   If the table  `first_table`  already exists, your script should not fail
	-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

- [x] 5. Full description : 

	Write a script that prints the full description of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

	-   The database name will be passed as an argument of the  `mysql`  command
	-   You are not allowed to use the  `DESCRIBE`  or  `EXPLAIN`  statements

- [x] 6. List all in table :

	Write a script that lists all rows of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

	-   All fields should be printed
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 7. First add :
	Write a script that inserts a new row in the table  `first_table`  (database  `hbtn_0c_0`) in your MySQL server.

	-   New row:
	    -   `id`  =  `89`
	    -   `name`  =  `Best School`
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 8. Count 89 :

	Write a script that displays the number of records with  `id = 89`  in the table  `first_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 9. Full creation :

	Write a script that creates a table  `second_table`  in the database  `hbtn_0c_0`  in your MySQL server and add multiples rows.

	-   `second_table`  description:
	    -   `id`  INT
	    -   `name`  VARCHAR(256)
	    -   `score`  INT
	-   The database name will be passed as an argument to the  `mysql`  command
	-   If the table  `second_table`  already exists, your script should not fail
	-   You are not allowed to use the  `SELECT`  and  `SHOW`  statements
	-   Your script should create these records:
	    -   `id`  = 1,  `name`  = “John”,  `score`  = 10
	    -   `id`  = 2,  `name`  = “Alex”,  `score`  = 3
	    -   `id`  = 3,  `name`  = “Bob”,  `score`  = 14
	    -   `id`  = 4,  `name`  = “George”,  `score`  = 8

- [x] 10. List by best :

	Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   Results should display both the score and the name (in this order)
	-   Records should be ordered by score (top first)
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 11. Select the best :

	Write a script that lists all records with a  `score >= 10`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   Results should display both the score and the name (in this order)
	-   Records should be ordered by score (top first)
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 12. Cheating is bad :
	Write a script that updates the score of Bob to  `10`  in the table  `second_table`.

	-   You are not allowed to use Bob’s id value, only the  `name`  field
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 13. Score too low :

	Write a script that removes all records with a  `score <= 5`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 14. Average :

	Write a script that computes the score average of all records in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   The result column name should be  `average`
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 15. Number by score:
	Write a script that lists the number of records with the same score in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   The result should display:
	    -   the  `score`
	    -   the number of records for this  `score`  with the label  `number`
	-   The list should be sorted by the number of records (descending)
	-   The database name will be passed as an argument to the  `mysql`  command

- [x] 16. Say my name :
	Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

	-   Don’t list rows without a  `name`  value
	-   Results should display the score and the name (in this order)
	-   Records should be listed by descending score
	-   The database name will be passed as an argument to the  `mysql`  command

	In this example, new data have been added to the table  `second_table`.

## Advanced Tasks

- [x] 17. Go to UTF8 :
	Write a script that converts  `hbtn_0c_0`  database to UTF8 (`utf8mb4`, collate  `utf8mb4_unicode_ci`) in your MySQL server.

	You need to convert all of the following to  `UTF8`:

	-   Database  `hbtn_0c_0`
	-   Table  `first_table`
	-   Field  `name`  in  `first_table`

- [x] 18. Temperatures #0 :
	Import in  `hbtn_0c_0`  database this table dump:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql "download")

	Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- [x] 19. Temperatures #1 :
	Import in  `hbtn_0c_0`  database this table dump:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql "download")  (same as  `Temperatures #0`)

	Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)


- [x] 20. Temperatures #2 :
	Import in  `hbtn_0c_0`  database this table dump:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql "download")  (same as  `Temperatures #0`)

	Write a script that displays the max temperature of each state (ordered by State name).

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
