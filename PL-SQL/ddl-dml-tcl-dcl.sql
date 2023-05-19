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





--SELECT
SELECT [distinct][column_name1, col_nam2] | *
FROM table_name [alias] [, table_name [alias]] ..
[WHERE condition]
[GROUP BY group [HAVING group_condition]]
[ORDER BY sort_columns [ASC | DESC]];






--ALIASES
select emp_id, department_id as depart
from employees
order by depart


--GROUP  BY
select exp1, exp2, aggregate_function(aggregate_exp)
from tables
where conditions
group by exp1, exp2;












--MERGE:- provides the ability to conditionally update or insert data into a database table
MERGE INTO table_name table_alias
USING (table|view|sub_query) alias
ON (join condition)
WHEN Matched THEN
    UPDATE SET
        col1 = col_val1
        col2=col2_val2
WHEN Not Matched THEN
    INSERT (column_list)
    VALUES (column_values);
    

--how to maintain table policyhistory which will have the policy name & number of times the policy has been borrowed
MERGE INTO policyHistory as ph
    USING Polict p
    ON (ph.pname = p.name)
WHEN MATCHED THEN
    UPDATE SET ph.count =ph.count+1
WHEN NOT MATCHED THEN
    INSERT (ph.pname, ph.count) VALUES (p.pname, 1);
    
    
    
    
    
    
--Database tranaction
--(transaction should end with either COMMIT or ROLLBACK)
-- permanency of DML operation are done using COMMI
--reverting the data is performed using ROLLBACK
--DDL commands are by default auto COMMIT
--ACID property:- atomicity, consitency, isolation, durability

--COMMIT: ends the current transation by making all pending data changes permanent





--SAVEPOINT: savepoint_name-> marks a save point within the current transation for further rollback







--ROLLBACK:- rollback ends the current transation by discading all pending data changes






--ROLLBACK TO savepoint_name:- ROLLBACK TO SAVEPOINT rolls back the current transation to the specified avepoint, thereby discarding any changes or avepoints created after the savepoint to which you are rolling back




--LOCKING :- prevent destructive interaction between concurrent transation when accessing shared resource








--Arithematic Expression
select 
pid,
MinAmountPerMonth + (MinAmountPerMonth*0.1) "Poliocy Amount"
from policy

--Concatenation Operation ||
select cname || 'lives in' || Addresss as customerAddress
from customer;


--DISTINCT:- this keyword in the select clause is used to eleminate duplicate rows
select DISTINCT address from customer;



--WHERE:- the WHERE clause follows the FROM clause
select * | {[DISTINCT] column | expression [alias], ..}
from table 
[WHERE condition(s)];



--Comparison Operators:- =, >, >=, <, <=, !=, <>, BETWEEN ... AND, IN (set), LIKE, IS NULL
--LIKE operators: '%', '-'
select cid, name, email, from customer where email like '%yahoo%';


--list the employees whose name starts withs with 's' and ends with 's'
select ename
from emp
where ename LIKE('s%') and ename LIKE('%s');

--BETWEEN X and Y (both are inclusive)
select * from policy 
where salary between 5000 and 8000;

--IN (set)
select cid, pid from policyenrollment 
where cid IN (5000, 6000, 7000);


--IS NULL
select * from policyenrollment
where penalty IS NULL;






--Logical operator:- AND, OR, NOT
select cid, cname 
from customer
where cid=1 and address = 'bangalore';


--Order by clause:- to retrive names of the customers in ascending order
select * from customer order by cname
--default - asc order
select cname from customer order by cname desc;





--Function
select theatre_id, theatre_name, location, ticket_cost,
case when(ticket_cost>=100 and ticket_cost<=150)
then 'Average'
when (ticket_cost>=151 and ticket_cost<=250)
then 'High'
when (ticket_cost>=251)
then 'Very High'
end commnets
from theatre_master
order by theatreid desc;






--Character function
--lower(column|exp)
select lower(cname) from customer where cid=1;

--upper(column|exp)
select uper(cname) from customer where cid=1;


--initcap(column|exp)
select initcap(cname) from customer where cid=1;

--concat(col1|exp1, col2|exp2)
select concat(cname, address) from customer where cid=1;

--substr(col|exp, m, [n]):- returns specified character from the character value starting at character position m,n character long
select substr(cname, 1, 2) from customer where cid=1;
--to
select substr(cname, 1) from customer where cid=1;
--tom
select substr(cname,-21, 2) from customer where cid=1;
--om


length(col|exp)
select length(cname) from customer where cid=1;

--Contains 5 character LENGTH
select ename 
from emp
where LENGTH(ename)=5;



--Number function
--abs(col | exp)
select abs(-5) from dual;


--ceil(col|exp)
select ceil(5.3) from dual;
--6




--floor(col|exp)
select floor(5.8) from dual;
--5

--Mod(m, n)
select mod(10,2) from dual;
--0



--round(n [,m]):- returns a number rounded to a certain number of decimal places. m refer to decimal place 
select round(10.678) from dual;
--10.7



--trunc(n[, m]):- returns a number truncated to a certain number of decimal places ;(-2 means to the left)
select trunc(10.678, 1) from dual;
--10.6
select trunc(10.67) from dual;
--10



--Date Function
--to get the current system date
select SYSDATE from dual;


--months_between
select cid, cname, round(months_between(sysdate, dob)/12) age from customer where cid =1;

--add_months
select add_months(sysdate, 4) from dual

--next_date
select next_day(sysdate, 'monday') from dual;


--last_day
select last_day(sysdate) from dual;


--round
select round(sysdate, 'year') from dual;
select round(sysdate, 'month') from dual;


--trunc
select trunc(sysdate, 'year') from dual;
select trunc(sysdate, 'month') from dual;






--Data type conversion

--to_char(number|date, [fmt]):- converts a number or date to string;
select to_char(sysdate, 'dd month yyyy') from dual;


--to_date(char, [fmt]):- convert a string to a date
select to_date('may-12-2021', 'mon-dd-yyyy') from dual;


--to_number(char, [fmt]):- convert a string to number
select to_number('234.67', 999.99) from dual;


--year, yyyy, yy
--MM, MONTH, MON
--WW:- week of year; W:- week of month
--D:- day of week; DAY:- name of day; DD:- day of month, DDD:- day of year
--HH, HH24
--MI:- minute
--SS:- second








--Conditional expression

IF-THEN-ELSE







--CASE expression
select pid, name,
case pname
when 'Money back plan' then 'Money saving'
when 'personal protect' then 'life insurance'
else 'Normal policy'
end "category of policy" from policy;








--DECODE expression/function

select pid, pname, decode(pname, 'Money back plan',
'money saving', 'personal protect', 'life insurance', 'normal policy'
) "category of policy" from policy






--General function
--NVL(exp1, exp2):- converts a null value to an actual value

select cid, pid, duedate, paiddate, amount, NVL(penalty, 0) penalty from policyenrollment;
--return 0 if penalty is null


--NVL2(exp1, exp2, exp3):- if exp1 is not null then return exp2, if exp1 is null then return exp3.
select cid, pid, duedate, NVL2(paiddate, 'paid', 'not Paid') status from policyenrollment;





--NULLIF:- compare two expression and return null if they are equal or the first expression if they are not equal





--COALESCE:- return the first not null expression in the expression list
select cid, cname, COALESCE(emailid, to_char(phoneno), address) contact from customer;







--Aggregate or Group function
--MAX, MIN, SUM, AVG, COUNT

select max(panelty) as maximum, min(panelty) as minimum from policyenrollment;


select cid, max(panelty) as maximum, min(panelty) as minimum 
from policyenrollment
group by cid;





--Having clause:- to restrict group
--you cannot use group function in the 'where'


select cid, sum(amount) as maximum
from policyenrollement
group by cid having sum(amount)>2000;





--JOINS:- use to combine the table using join when the result set is from more than one table

select cname, pname
from customer c 
join policies p
on c.cid = p.cid;

--

select table1.column, table2.column
from table1
join table2 
ON table1.column1=table2.column2;


--CARTESIAN JOINS:- when condition is not mentions then it occurs
select c.cid, c.name, enrollmentid, p.cid, pid
from customer c, policyenrollment p
order by c.cid, enrollementid;


--Types of join:- Equijoin, Non Wquijoin, Outer join, Self join

--Equijoin:- it is also called simple join or inner join, when two tables are joined using = operator in the join condition
select c.cid, c.name, p.cid
from customer c 
join policyenrollment p
ON c.cid = p.cid;


--A non equijoin is a join condition containing something other than an equality operator

--OUTER JOIN
--1. LEFT OUTER JOIN, 2.RIGHT OUTER JOIN, 3. FULL OUTER JOIN
--LEFT OUTER JOIN:- returns all the rows from the left table, with the matching rows of the right table
select table1.column, table2.column
from table1 LEFT OUTER JOIN table2 
ON table1.column1 = table2.column2;




--RIGHT OUTER JOIN:-returns all the rows from the right table, with the matching rows of the left table
select table1.column, table2.column
from table1 RIGHT OUTER JOIN table2 
ON table1.column1 = table2.column2;




--FULL OUTER JOIN:- returns all rows from both the table
select table1.column, table2.column
from table1 FULL OUTER JOIN table2 
ON table1.column1 = table2.column2;





--SELF JOIN:- it is a join in which a table is joined with itself, especially when the table has a foregin key which reference it's own primary key
--eg. query to display the books which are of the same price
select b1.bid, b2.bname, b2.price
from book b1, book b2,
where b1.bid != b2.bid and b1.price=b2.price;





--NATURAL JOIN:- is a type of equi join that compares the common columns of both the tables with each other

select cid, cname, pid
from customer
NATURAL JOIN policyenrollment;







--JOINS with the USING clause:- the using clause specifies which columns to test for equality when two tables are joined. It can be used insead of an ON or WHERE clause
select cid, cname, pid
from customer
join policyenrollment 
USING(cid);




--SUBQUERY:- is a select statement that is embedded in a clause of another SQL statement
--sub query can be placed inisde - WHERE | HAVING | FROM
select columnlist
from table
where columnname operator
            (
            select columnlist from table
            );
            
            
--single row subquery:-  = | < | <= | > | >= |<> 




--multiple row sub query :- IN | ALL | ANY
--<ANY , >ANY, =ANY, <ALL, >ALL


--subquery insert 
insert into policyenrollment_history select * from policyenrollment;

--subquery create
create table policyenrollment_history as select * from policyenrollment;

--subquery delete
delete from policyenrollment 
where cid=(
    select cid 
    from customer 
    where cname='deepak'
    );






--Database Object
--TABLE:- Basic unit of storage; composed of row and column



--2. View, :- view doesnot contain data by itself. view actually points to the table & whenever you create a view , you create a view as omething that select the subset of data froma particular table
--(view- logically represents subsets of data from one or more tables)
create view viewname as select query
[with check option [CONSTRAINT constraint]]
[with READ ONLY [CONSTRAINT constraint]]

create view policy_details as 
select pid, pname from policy;

--DENY DML operation:- to ensure that no DML operation occur throug view, create a view with read only option
create view policy_details as select pid, pname from policy with read only;








--4. Sequence:- generate unique numbers automatically
CREATE SEQUENCE seq_name
[increment by n]
[start with n]
[maxvalue n | nomaxvalue]
[minvalue n | nominvalue]
[cycle | nocycle]
[cache|nocache]

--cache:- specify how many values the oracle server pre-allocate and keeps in memory

create sequence emp_seq start with 1;


--NEXTVAL:- returns the next available sequence value
insert into emp_values(emp_seq.nextval, 'mini');

--CURRVAL:- returns the current sequence value
select emp_seq.currval from dual;


--MODIFYING SEQUENCE
Alter sequence emp_seq
increment by 20
maxvalue 9999999
NOCACHE
NOCYCLE


--to get the sequence information
select min_value, max_value, increment_by from user_sequences where sequence_name='emp_seq';

--to drop the create sequence
drop sequence book_seq;






--3. Synonym, :- basically alias name for an existing table name (gives alternate name to objects)
create [PUBLIC] synonym
syn_name for schema_obj;

create synonym enroll for policyenrollment;
drop synonym enroll;







--1. Index, :- helps to retrive the data faster ; (Improve the performance of some query)

create [unique] index
index_name ON 
table (column);


create index policy_ind ON POLICY(PNAME);

--INDEX TYPE
--1. Cluster index
create clustered index policy_ind1 on policy(pid);
--2.NON-clustered index
create index policy_ind2 on policy(pname);
--3.INIQUE index
create unique index customer_ind1 on customer(emailid);
--4. functional based index
create index customer_ind2 on customer(upper(cname));


--dropping an index;
drop index index_name;




--DCL: Data contol language:- Used to creates privilege to allow users to access and manipulate the databases
--GRANT:- to grant a privilage to the user
--(Grant command can be attached to any combination of select, insert, update, delete, alter)
GRANT privilege1, privilege2, privilege3 | ALL
ON TABLE | VIEW
TO userId [WITH CHECK option];


GRANT SELECT ON POLICY TO SAM;
GRANT TO ALL USERS;
GRANT SELECT ON POLICY TO PUBLIC;




--REVOKE:- to revoke(remove) a privilage from a user; (get back the given permission from the user)
REVOKE privilege1, privilege2, privilege3 | ALL
ON table | view 
FROM userId


REVOKE select ON POLICY FROM sam;









