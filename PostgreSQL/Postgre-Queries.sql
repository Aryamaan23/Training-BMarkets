

--CREATE TABLE COLORC(COLOR_ID INT,GENERATEDAT INT,)
--INSERT INTO COLOR(COLOR_ID,COLOR_NAME) values (2,'Pink') 
  CREATE TABLE ARYAMAAN(NAMEA VARCHAR, AGE INT);
 SELECT * FROM ARYAMAAN;
 
 CREATE TABLE colorco(color_id int primary key generated always as identity
 				  (start with 5 increment by 10), color_name varchar not null);
 				  
 INSERT INTO colorco(color_id,color_name) overriding system value values(2,'Pink');
 
 SELECT * FROM colorco;
 
 CREATE TABLE DEPT1(DEPT_ID INT,DEPT_NAME VARCHAR(20),PRIMARY KEY(DEPT_ID));
 SELECT * FROM DEPT;
 
 DROP TABLE IF EXISTS EMP1;
 CREATE TABLE EMP1(eid varchar(5),ename varchar(20),esal int, primary key(eid), dept_id int,
				constraint fk_dept foreign key(DEPT_ID) references DEPT1(DEPT_ID));
 				
 ALTER TABLE EMP1 DROP CONSTRAINT fk_dept, ADD constraint fk_dept foreign key(DEPT_ID) references DEPT1(DEPT_ID) ON DELETE CASCADE;
 
 INSERT INTO DEPT1 VALUES(1,'Telecom');
 INSERT INTO DEPT1 VALUES(2,'Defence');
 INSERT INTO DEPT1 VALUES(3,'Airforce');
 
 SELECT * FROM DEPT1;
 
 INSERT INTO EMP1 VALUES('10000','Tanuj Shankar',50000,1);
 INSERT INTO EMP1 VALUES('102','Aryamaan',140000,2);
 INSERT INTO EMP1 VALUES('30000','Ankit Hans',20000,3);
 --INSERT INTO EMP1 VALUES('4000','Adit Patel',1000,4);
 
 SELECT * FROM EMP1; 
 SELECT * FROM EMP1 WHERE EID='102';
 SELECT * FROM EMP1 WHERE ENAME='Aryamaan' AND ESAL>=140000;
 SELECT * FROM EMP1 WHERE ENAME='Ankit Hans' OR ENAME='Tanuj Shankar';
 SELECT * FROM EMP1 WHERE ENAME IN ('Ankit Hans','Tanuj Shankar','Aryamaan');
 SELECT * FROM EMP1 WHERE ENAME LIKE 'Ar%';
 SELECT * FROM EMP1 WHERE ENAME ~* '^A.*n.*';
 SELECT * FROM EMP1 WHERE ESAL BETWEEN 2000 and 140000;
 SELECT * FROM EMP1 WHERE LENGTH(ENAME) <> 5;
 
 
 DELETE FROM EMP1 WHERE EID='102';
 
 SELECT CONCAT(ENAME,ESAL) FROM EMP1;
 
 SELECT ROUND(1372.472,1);
 
 SELECT COUNT(ESAL) FROM EMP1;
 
 SELECT ENAME,SUM(ESAL) 
 FROM EMP1 WHERE ENAME='Ankit Hans'
 group by ENAME;
 
 SELECT ENAME, SUM(ESAL) FROM EMP1 group by
 ENAME order by SUM(ESAL) desc;
 
 ---- SELF JOIN
 
 CREATE TABLE employee(eid int primary key,
					   fname varchar(20),
					   lname varchar(20),
					  manager_id int,
					  foreign key(manager_id)
					  references employee(eid) 
					  on delete cascade);
					  
 INSERT INTO employee values(1,'Ram','Patel',NULL),
                            (2,'Ana','Conner',1),
							(3,'Hasan','Reeres',1),
							(4,'Tom','Lester',2),
							(5,'Kelly','Christon',2),
							(6,'Kelsie','Hales',3),
							(7,'Sam','Norwan',3),
							(8,'Windy','Hays',3);

SELECT * FROM EMPLOYEE;
							
 SELECT e.fname || ' ' || e.lname emp,
 m.fname || ' ' || m.lname manager
 from employee e INNER JOIN employee m ON
 m.eid=e.manager_id order by manager;


-- Nested Query or Sub Query
Select * from emp1;
SELECT ename,esal from emp1 where esal >
(select esal from emp1 where ename='Ankit Hans');

Select * from emp1 where esal > (select avg(esal)
								from emp1);
								

--BEGIN
BEGIN;
BEGIN WORK;
BEGIN TRANSACTION;

update emp1 set esal=45000 where eid='102';

COMMIT; -- saved permanently on the disk

-- ROLLBACK OR ROLLBACK WORK OR ROLLBACK TRANSACTION

-- Indexing adds a pointer to the table

--Data strucutres used for indexing are hash or b-tree

Create index emp_index on emp1(eid);

Create unique index on emp1(eid);

drop index emp_index;


CREATE TABLE STUDENT(roll_no int,
					name varchar,
					address varchar,
					contact_no varchar,
					age int)
					
INSERT INTO Student values(1,'Aryamaan','1M/2XYZ','999',22),
                          (2,'Keshav','2M/2S','9999',20),
						  (3,'Udain','3A/2B','9999',20),
						  (4,'Anih','4A/2B','8988',22),
						  (5,'Dua','5A/2BC','87878',20),
						  (6,'Goutham','6A/2BC','6565',25),
						  (7,'Saurav','7A/2BC','4343',26),
						  (8,'Adit','8A/2B','23232',27),
						  (9,'Ankit','9A/2B','23232',28),
						  (10,'Tanuj','10A/2B','32323',29)
						  
						  
Select name,address from Student order by roll_no desc;

Select roll_no as code from Student;
                          
Create table Student_details(roll_no int,
							branch varchar,
							grade varchar)
							
							
INSERT INTO Student_details VALUES(1,'CSE','A'),
                           (2,'EEE','B'),
						   (3,'Mech','C'),
						   (4,'Civil','D'),
						   (5,'Nanotech','A'),
						   (6,'Aero','B'),
						   (7,'Chemical','C'),
						   (8,'Automobile','D'),
						   (9,'CSE','N'),
						   (10,'CSE','M'),
						   (11,'CSE','O')
						   
						   
SELECT grade,name from student s JOIN student_details sd
on s.roll_no=sd.roll_no
where age > 25;

Select * from student where address 
like '%A' OR address like '%B' OR address like '%C';

Select * from student where address like '%B' OR address like '%C';




                           
							
							

								
