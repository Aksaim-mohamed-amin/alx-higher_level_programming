
# 0x0E. SQL - More queries

Welcome to the "0x0E. SQL - More queries" project! In this project, I did embark on an exciting journey into the world of Structured Query Language (SQL). SQL is a powerful language used for managing and manipulating relational databases, making it an essential skill for anyone interested in data management and analysis.

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

- [x] 0. My privileges! : 

	Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

	- [x] 1. Root user : 

	Write a script that creates the MySQL server user  `user_0d_1`.

	-   `user_0d_1`  should have all privileges on your MySQL server
	-   The  `user_0d_1`  password should be set to  `user_0d_1_pwd`
	-   If the user  `user_0d_1`  already exists, your script should not fail
	
- [x] 2. Read user : 

	Write a script that creates the database  `hbtn_0d_2`  and the user  `user_0d_2`.

	-   `user_0d_2`  should have only SELECT privilege in the database  `hbtn_0d_2`
	-   The  `user_0d_2`  password should be set to  `user_0d_2_pwd`
	-   If the database  `hbtn_0d_2`  already exists, your script should not fail
	-   If the user  `user_0d_2`  already exists, your script should not fail

- [x] 3. Always a name : 

	Write a script that creates the table  `force_name`  on your MySQL server.

	-   `force_name`  description:
	    -   `id`  INT
	    -   `name`  VARCHAR(256) can’t be null
	-   The database name will be passed as an argument of the  `mysql`  command
	-   If the table  `force_name`  already exists, your script should not fail

- [x] 4. ID can't be null :

	Write a script that creates the table  `id_not_null`  on your MySQL server.

	-   `id_not_null`  description:
	    -   `id`  INT with the default value  `1`
	    -   `name`  VARCHAR(256)
	-   The database name will be passed as an argument of the  `mysql`  command
	-   If the table  `id_not_null`  already exists, your script should not fail

- [x] 5. Unique ID : 

	Write a script that creates the table  `unique_id`  on your MySQL server.

	-   `unique_id`  description:
	    -   `id`  INT with the default value  `1`  and must be unique
	    -   `name`  VARCHAR(256)
	-   The database name will be passed as an argument of the  `mysql`  command
	-   If the table  `unique_id`  already exists, your script should not fail

- [x] 6. States table :

	Write a script that creates the database  `hbtn_0d_usa`  and the table  `states`  (in the database  `hbtn_0d_usa`) on your MySQL server.

	-   `states`  description:
	    -   `id`  INT unique, auto generated, can’t be null and is a primary key
	    -   `name`  VARCHAR(256) can’t be null
	-   If the database  `hbtn_0d_usa`  already exists, your script should not fail
	-   If the table  `states`  already exists, your script should not fail

- [x] 7. Cities table :
	Write a script that creates the database  `hbtn_0d_usa`  and the table  `cities`  (in the database  `hbtn_0d_usa`) on your MySQL server.

	-   `cities`  description:
	    -   `id`  INT unique, auto generated, can’t be null and is a primary key
	    -   `state_id`  INT, can’t be null and must be a  `FOREIGN KEY`  that references to  `id`  of the  `states`  table
	    -   `name`  VARCHAR(256) can’t be null
	-   If the database  `hbtn_0d_usa`  already exists, your script should not fail
	-   If the table  `cities`  already exists, your script should not fail

- [x] 8. Cities of California :

	Write a script that lists all the cities of California that can be found in the database  `hbtn_0d_usa`.

	-   The  `states`  table contains only one record where  `name`  =  `California`  (but the  `id`  can be different, as per the example)
	-   Results must be sorted in ascending order by  `cities.id`
	-   You are not allowed to use the  `JOIN`  keyword
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 9. Cities by States :

	Write a script that lists all cities contained in the database  `hbtn_0d_usa`.

	-   Each record should display:  `cities.id`  -  `cities.name`  -  `states.name`
	-   Results must be sorted in ascending order by  `cities.id`
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 10. Genre ID by show :

	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")

	Write a script that lists all shows contained in  `hbtn_0d_tvshows`  that have at least one genre linked.

	-   Each record should display:  `tv_shows.title`  -  `tv_show_genres.genre_id`
	-   Results must be sorted in ascending order by  `tv_shows.title`  and  `tv_show_genres.genre_id`
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 11. Genre ID for all shows :

	Import the database dump of  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `10-genre_id_by_show.sql`)

	Write a script that lists all shows contained in the database  `hbtn_0d_tvshows`.

	-   Each record should display:  `tv_shows.title`  -  `tv_show_genres.genre_id`
	-   Results must be sorted in ascending order by  `tv_shows.title`  and  `tv_show_genres.genre_id`
	-   If a show doesn’t have a genre, display  `NULL`
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 12. No genre :
	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `11-genre_id_all_shows.sql`)

	Write a script that lists all shows contained in  `hbtn_0d_tvshows`  without a genre linked.

	-   Each record should display:  `tv_shows.title`  -  `tv_show_genres.genre_id`
	-   Results must be sorted in ascending order by  `tv_shows.title`  and  `tv_show_genres.genre_id`
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 13. Number of shows by genre :

	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `12-no_genre.sql`)

	Write a script that lists all genres from  `hbtn_0d_tvshows`  and displays the number of shows linked to each.

	-   Each record should display:  `<TV Show genre>`  -  `<Number of shows linked to this genre>`
	-   First column must be called  `genre`
	-   Second column must be called  `number_of_shows`
	-   Don’t display a genre that doesn’t have any shows linked
	-   Results must be sorted in descending order by the number of shows linked
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 14. My genres :

	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `13-count_shows_by_genre.sql`)

	Write a script that uses the  `hbtn_0d_tvshows`  database to lists all genres of the show  `Dexter`.

	-   The  `tv_shows`  table contains only one record where  `title`  =  `Dexter`  (but the  `id`  can be different)
	-   Each record should display:  `tv_genres.name`
	-   Results must be sorted in ascending order by the genre name
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 15. Only Comedy :
	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `14-my_genres.sql`)

	Write a script that lists all Comedy shows in the database  `hbtn_0d_tvshows`.

	-   The  `tv_genres`  table contains only one record where  `name`  =  `Comedy`  (but the  `id`  can be different)
	-   Each record should display:  `tv_shows.title`
	-   Results must be sorted in ascending order by the show title
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 16. List shows and genres :
	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `15-comedy_only.sql`)

	Write a script that lists all shows, and all genres linked to that show, from the database  `hbtn_0d_tvshows`.

	-   If a show doesn’t have a genre, display  `NULL`  in the genre column
	-   Each record should display:  `tv_shows.title`  -  `tv_genres.name`
	-   Results must be sorted in ascending order by the show title and genre name
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

## Advanced Tasks

- [x] 17. Not my genre :
	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `16-shows_by_genre.sql`)

	Write a script that uses the  `hbtn_0d_tvshows`  database to list all genres not linked to the show  `Dexter`

	-   The  `tv_shows`  table contains only one record where  `title`  =  `Dexter`  (but the  `id`  can be different)
	-   Each record should display:  `tv_genres.name`
	-   Results must be sorted in ascending order by the genre name
	-   You can use a maximum of two  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 18. No Comedy tonight! :
	Import the database dump from  `hbtn_0d_tvshows`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")  (same as  `100-not_my_genres.sql`)

	Write a script that lists all shows without the genre  `Comedy`  in the database  `hbtn_0d_tvshows`.

	-   The  `tv_genres`  table contains only one record where  `name`  =  `Comedy`  (but the  `id`  can be different)
	-   Each record should display:  `tv_shows.title`
	-   Results must be sorted in ascending order by the show title
	-   You can use a maximum of two  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 19. Rotten tomatoes :
	Import the database  `hbtn_0d_tvshows_rate`  dump to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql "download")

	Write a script that lists all shows from  `hbtn_0d_tvshows_rate`  by their rating.

	-   Each record should display:  `tv_shows.title`  -  `rating sum`
	-   Results must be sorted in descending order by the rating
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

- [x] 20. Best genre :
	Import the database dump from  `hbtn_0d_tvshows_rate`  to your MySQL server:  [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql "download")  (same as  `102-rating_shows.sql`)

	Write a script that lists all genres in the database  `hbtn_0d_tvshows_rate`  by their rating.

	-   Each record should display:  `tv_genres.name`  -  `rating sum`
	-   Results must be sorted in descending order by their rating
	-   You can use only one  `SELECT`  statement
	-   The database name will be passed as an argument of the  `mysql`  command

## Contributing

If you have any suggestions or improvements for the tasks or exercises, please feel free to contribute. You can do this by forking the repository, making your changes, and submitting a pull request. All contributions are welcome and appreciated.
