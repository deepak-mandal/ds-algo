--SQL:- (4)
--Data Defination language: create, alter, truncate, drop
--Data Manipulation language: insert, uodate, delete, select
--transation control language: commit, rollback
--Data control language: grant revoke


--DDL
--Create
create table customer(
cId number(10),
cName varchar2(25),
phoneno number(10),
email varchar2(25),
address varchar(35)
);



--Constraint (5): constraints are the rules enforced on data columns on the table. these are used to limit the type of data that can go into the table - accuracy & reliability puropse
--type of constraint - primary key, foreign key, unique, not null, check
--UNIQUE:- no dublicate are allowed but null values are allowed
create table customer(
cId number(10) PRIMARY KEY,
cName varchar2(25) NOT NULL,
phone number(10),
email varchar2(25) UNIQUE
);

--CHECK: Use check constraints to ensure the attribute has only a positive value
create table policy(
pId varchar2(10) PRIMARY KEY,
pName varchar2(25),
pPeriodInYears varchar2(25) NOT NULL,
MinAmount number(10) CHECK(MinAmount>0)
);


--FOREIGN KEY:- it is used to enforce the link between tables. the referenced table is called the parent table while the table with the foregin key is called the child table. the primary or unique column of the parent table can be created as foregin key column in the child table
create table policyEnrollement(
enrollementId number(5) primary key,
cId number(10) REFERENCES customer(cId),
pId varchar(10),
dueDate date,
paidDate date,
penalty number(10)
);

--User can override the default constraint name with the user defined constraint name
create table policy(
pId varchar2(10) CONSTRAINT pk_pid primary key,
pname varchar2(25),
pPeriodInYears varchar2(25) not null ,
minAmount number(10) constraint ck_minamount check(minAmount>0)
);



--ALTER: alter command is used to change the structure of the table
--ADD, MODIFY, RENAME, DROP

--to add a column age to customer table
ALTER table customer ADD age number(2);

--to increase the column size of email to 30;
alter table customer MODIFY email varchar2(30);

--to change the column name from email to emailId
alter table customer RENAME COLUMN email TO emailId;

--rename table name
alter table saleInfo RENAME to dale_Information;

--to change the datatype of a particular column
alter table tablename MODIFY columnname newdatatype;

--to remove a column from the table
alter table tablename DROP COLUMN columnname;

--to remove a constraint
alter table tablename DROP CONSTRAINT constriantname;

--to enable/disable a constraint
alter table tablename ENABLE/DISABLE CONSTRAINT constraintname;



--TRUNCATE: remove all rows from the table
--(Restriction:- you cannot truncate the table if it id linked with anither table)
TRUNCATE TABLE table_name;


--DROP: drops the entire table structure
DROP TABLE table_name;

--in truncste only the data is removed, whereas, In drop the entire structure is removed.




--DML:- defines the data of table

--INSERT
insert into customer values (1, 'tom', 'tom@gmail.com', 'mumbai');
insert into customer 
(id, cname, phoneno, address) 
values 
(2, 'mini', 741258963, 'chennai');



--UPDATE
update customer set email='tiny15@gamil.com'
where cname='tiny';
--all rows in the table are modify if we omit the WHERE clause


--DELETE
--remove existing rows from the table by using the delete statement
DELETE from customer where cId=2
--to delete all rows from the table
delete from customer;


--deletion is not posible if the row to be deleted is referred in the child table
--deletion of the parent records is made possible by using a foreign key reference options
--CASCADE, SET NULL, RESTRICT
--Syntax: REFERENCE table_name(index_col_name, ...) [ON DELETE SET NULL/ RESTRICT/ CASCADE]

--CASCADE:- delete the row from the parent table and automatically deletes the matching rows in the child table
create table ploicyEnrollment(
enrollmentId number (15) primary key,
cid number(10) references customer(cid) ON DELETE CASCADE,
pid varchar2(10),
dueDate date,
paidDate date,
penalty number(10)
);




--SET NULL: delete the row from the parent table and sets the foreign key column in the child table is null
create table policyEnrollment(
enrollmentId number(15) primary key,
cid number(10) references customer(cid) on DELETE SET NULL,
pid varchar2(10),
dueDate date,
paidDate date,
penalty number(10)
);






--RESTRICT: rejects the delete or update operations for the parent table. THIS iS default option





SELECT



--ALIASES
select emp_id, department_id as depart
from employees
order by depart


--GROUP  BY
select exp1, exp2, aggregate_function(aggregate_exp)
from tables
where conditions
group by exp1, exp2;

--Contains 5 character LENGTH
select ename 
from emp
where LENGTH(ename)=5;

--list the employees whose name starts withs with 's' and ends with 's'
select ename
from emp
where ename LIKE('s%') and ename LIKE('%s');

