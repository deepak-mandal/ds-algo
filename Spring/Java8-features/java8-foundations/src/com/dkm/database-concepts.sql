MySQL

-- In ternimal
sudo mysql -u root -p (for linux)
mysql -u root -p (for window)


-- TO create database
create database <databaseName>
create database hr;

-- TO switch to database
USE databasename;


-- In ternimal
create database hr;


-- To view all the databases
show databases;

use hr;


-- to view all the tables in the database
show tables;


-- to create a table
create table course(id int, name varchar(20), duration int);



-- to view the structure of the table
describe tablename;


-- alter
-- to add new column
alter table course add column domain varchar(20);

-- to modify the existing column
alter table course modify name varchar(35);

-- change the name of the column
alter table cours change domain specialization varchar(20);


-- delete column
alter table course drop column specialization;


insert into course values (1, 'java', 2);



select * from course;


-- to delete the data from the table without deleting the structure
truncate course;


-- to delete the table including the structure
drop table course;


desc course;

-- DML
-- to modify the record
update dept set loc='bangalore' 
where deptno = 10;


-- to delete an existing record
delete from dept 
where deptno = 20;



-- TCL
-- to make it false : not auto commit
set autocommit =0;
select * from dept;
insert into dept (deptno, dname) 
values
(20, 'deepak');
select * from dept;
rollback;


-- commit:- to store permanently into database
-- rollback:- we can cancel the tranaction



-- foregin key
create table emp(empno int
ename varchar(20),
sal int,
deptno int references dept(deptno));






