# CMPE-207--Memcached
•	SQLite is used for creating the database.
•	Memcached is the caching layer. Running Memcached container on docker.
•	The client requests for the data, if the data is not available in the cache it will be a MISS. Then it will get the data from the database.
•	If the data is already present in t cache, it will be a HIT.
•	If the requested data is not present in database, the error message saying “data not in db” will be displayed.


Create sqlite3 database:
sqlite3 db.sql -header -column 
sqlite> create table my_table1( Name STRING(50), Description STRING(50)); 
sqlite> insert into my_table1 values ('Banana', 'Fruit'); 
sqlite> insert into my_table1 values ('Grasshopper', 'Insect'); 
sqlite> insert into my_table1 values ('Himalay', 'Mountain'); 
sqlite> insert into my_table1 values ('Python', 'Prog language');

Check the created database:
sqlite> select * from my_table1;

RUN A MEMCACHED CONTAINER ON DOCkER 
$ docker run -itd --name memcached -p 11211:11211 rbekker87/memcached:alpine

Run the hw4.py file
