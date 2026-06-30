# 15 SQL interview questions
1.Difference between DBMS and RDBMS
DBMS: Data Base management Syastem: we store data in a files such that there is no connection between the data files
RDBMS: Realational Data Base Management System: We store a data in such a way that there will be a relation between data files whuch helps
1.Easy to Create Realationships between different pieces of data
2.This allows faster data retrieval
3.When you are dealing with large datasets
It also supports 
1.Support Multiple Users
2.High Security
3.Optimized for Large Amount of Data

2.What is Primary Key and Foreign Key?
Primary Key:Is defined as a unique key in table and it should not have a Empty/Null value for primary key
Example:In a students table the Roll Number can be defined as a primary key
Foreign Key: Helps you connect data across tables, ensuring the records in one table can reference related information in another
Example:If we have a student table and a Course table which have roll number as a  comman row to linke between the two tables, then the roll number row serves as a foreign key

3.What are constrainst and their types?
SQL is like rules you set up for data in your tables
They help keep data accurate and reliable
Constaraints in SQL
1.NOT NULL: We can not have a empty value in a row like for roll number
2.UNIQUE: No two values in a column are same, example emails of students should be unique
3.PRIMARY KEY:It combines NOT NULL and UNIQUE constraint, One field which should uniquely identifi
4.Foreign Key:This one links tables together
5.CHECK: Helps you set a Condition example age>18
6.DEFAULT: If you don't specify the value then by default it will take a value, like while adding the country if we don't specify take INDIA as input 

4.Explain DDL and DML Commands in SQL.?

DDL:Data Defination Language 
DDL Commands:Define the Structure of the Database like Creating,Altering,Deleting,Drop of tables
DDL command don't deal with the actual data but just with the database structure

DML:Data Manipulation Language
Working with actual data, we use DML commands to actually insert,update,delete the data 
Example:
insert into employee
update employee
delete from employee
example query to add: insert into employee (name,position) values ('fasi','Software Engineer')

5.Difference between DELETE, DROP and TRUNCATE statements.?
DELETE: DELETE is used to remove the specific row from a table. The table structure remains the same, and this can be roll back
delete from students where id=2;
TRUNCATE: TRUNCATE is used to remove all the rows from a table quickly, structure remains same and this can't be roll back
truncate table student;
table remain
id     |   name      |      age
Drop:Drop is used to completely remove the table from database, this can not be rollback
drop table student;

6.Differentiate between Group by and Order by Clause
Group By: Is used with some aggrigate functions such as sum,avg,count etc
with group by we get 
Total salary of each department
Average salary in each department
Count of employees in each department
select department, avg(salary) from employes group by department
Order By: Its like sorting rows in a particular order, you are sorting the entire table based on one or more columns, such as salaries from highest to lowest
select * from employees order by salaries desc;

7.Difference between where clause and having clause.?
When to use where clause:Filter individual rows based on specific conditions like age or name 
select s_name, age from student where age >=18;

Having Clause:Think of it Like filtering after grouping
When to use Having clause:You use Having clause when you want to filter groups created by group by clause based on Aggregate results, Like counts or sums
Example:How many students are in each age group but only display age groups with more then one student
SELECT age, COUNT(roll_no) AS no_of_students
FROM student
GROUP BY age
HAVING COUNT(roll_no) > 1;

age     |    no_of_students
20      |    3
22      |    2

Step-by-Step Execution
🔹 1. FROM student
👉 SQL first looks at the student table
Example data:
roll_no | age
1       | 20
2       | 20
3       | 22
4       | 20
5       | 22
6       | 25
🔹 2. GROUP BY age
👉 Rows are grouped based on age
It internally creates groups like:
Age 20 → [1,2,4]
Age 22 → [3,5]
Age 25 → [6]
🔹 3. COUNT(roll_no)
👉 Counts number of students in each group
Age 20 → 3 students
Age 22 → 2 students
Age 25 → 1 student
🔹 4. HAVING COUNT(roll_no) > 1
👉 Filters groups, not rows
Keeps groups where count > 1
Removes groups where count ≤ 1
So:
Age 20 → ✅ keep (3)
Age 22 → ✅ keep (2)
Age 25 → ❌ remove (1)
🔹 5. Final Output
age | no_of_students
20  | 3
22  | 2

🧠 WHERE vs HAVING
Clause	Works On	When Used
WHERE	Rows	    Before grouping
HAVING	Groups	    After grouping

8.What are aggregate functions in SQL, and can you provide examples.?
a.count():it counts the number of rows or non-null values in a column
b.sum():it adds up all the values in a numeric column
sum(salary) gives total salary of employes from table
c.avg():calculates the average of a numeric column 
d.min():it finds the minimum value in a numeric column
e.max():it finds the maximum value in a numeric column

9.What you mean by indexing in SQL and what do you mean by clustered index.?
*Indexing in SQL: Indexing in sql is a technique used to improve the speed of data retrieval from a table
An index works like the index of a book 📖.
Instead of scanning the entire table, the database uses the index to quickly find the required data.
select * from student where roll_no=95
*Clustered Index:A clustered index determines the physical order of data stored in table
It means the table data itself is stored according to the clustered index column
Because the data can be stored only one way physically,a table can have only one clustered index
Example
Student Table with Clustered Index on roll_no
CREATE CLUSTERED INDEX idx_rollno
ON student(roll_no);
Data will be stored like this internally:
roll_no	name	age
101	    Rahul	20
102	    Aisha	21
103	    John	22
The rows are physically arranged by roll_no.

10.Normalization:Normalization in database works similarly by organizing data efficiently,minimizing redundancy (Duplicate Information), and Preventing issue when inserting,deleting,or Updating records.
Why is Normalization Important.?
a.Reduces Redundancy:Helps avoid storing the same information multiple times
b.Prevent Anomalies:Helps prevent errors when adding,removing or updating data
Types of Normalization(Normal Forms):
1.First Normal Form(1NF):Each table cell should contain a single value, and each column must have a unique name
First Normal Form (1NF)
Rule
Each column must contain atomic (single) values
No multiple values in a single column
Each record must be unique
❌ Not in 1NF
roll_no	name	subjects
1	    Rahul	Math, Science
Subjects column has multiple values

✅ In 1NF
roll_no	name	subject
1	    Rahul	Math
1	    Rahul	Science

Now each cell has a single value.

2.Secound Normal Form(2NF): All non-key attributes must depend on the primary key
Second Normal Form (2NF)
Rule
Must be in 1NF
No partial dependency
Non-key columns must depend on the entire primary key
Example
Table
student_id	course_id	student_name	course_name
Problem:
student_name depends only on student_id
course_name depends only on course_id
Solution: Split the table.
Student Table
student_id	student_name
Course Table
| course_id | course_name |
Enrollment Table
| student_id | course_id |

3.Third Normal Form(3NF):Every Non-key attribute must be independent of other non-key attributes
Third Normal Form (3NF)
Rule
Must be in 2NF
No transitive dependency
This means non-key columns should not depend on another non-key column.
❌ Example
student_id	student_name	department_id	department_name
Problem:
department_name depends on department_id, not directly on student_id.
✅ Solution
Student Table
| student_id | student_name | department_id |
Department Table
| department_id | department_name |
🎯 Simple Interview Summary
Normal Form	Rule
1NF	Remove multi-value columns
2NF	Remove partial dependency
3NF	Remove transitive dependency

4.Boyce-Codd Normal Form(BCNF):Every determinant (An attribute that can determine other attributes) must be a candidate key

11.Union and Union all operator in SQL.?
Union:The union operator combines both lsit into one, it removes any duplicates.
select name from schoolfriends union select name from workfriends;
Union all:It combines the two lists but keeps every name,even if they show up more than once(final answer contains duplicate values as well)
select name from schoolfriends union all select name from workfriends;

12.How to find the the second most salary in the table.?
This includes subquery
first we find out the max salary that is
select max(salary) from employee
now we put sub query
select max(salary) from employee where salary(select max(salary) from employee)
final query will be 
select name,salary from employee where salary=(select max(salary) from employee where salary <(select max(salary) from employee))

13.What are views in SQL.?
A view in sql is a virtual table created from the result of a sql query on one or more tables
It does not store the data physically;it only stores the query and whenever the view is used, the database executes the query
example:
create view detaileview as select studentdetail from studentdetails where sid>5;
and whenever we perfrom the below query
select * from detaileview
we can see the the table we have in view detailview

14.How can you convert a text into a date format.? Consider a text as 20-11-2024
Ans:convert string to date format use the str_to_date 
example: select str_to_date('27-10-2024','%d-%m-%y')

15.What are triggers in sql.?
Ans:Triggers are like reflex actions which allow you to set up an automatic action, that will run everytime a certain event happens in our database events like
Adding, Updating and Deleting data 
When do triggers run.?
a.Insert:When new data is added to a table
b.Update:When existing data in the table changes
c.Delete:When data is removed from a table
example:Decrease the available stock of a book whenever some borrows a book from library
Log the transaction to keep track of borrowed books
below is query
create trigger UpdateBooksStock
we are creating a trigger named as UpdateBooksStock
Here it's named which reflects what the trigger does-updates the stock of books
After insert on BorrowedBooks
This part tells the trigger when to activate.Here, it activates after a new record(row) is added to the BorrowedBooks Table
for each row
Then a looping statement fpr each row
This means that for every individual borrowed book entry(new row) added to Borrowedbooks,the trigger will apply
begin update books set available_count = available_count-1 where book_id=NEW.book_id;
end;
Finally update books