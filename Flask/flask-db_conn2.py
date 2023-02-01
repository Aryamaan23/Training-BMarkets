import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='Finserv@2023')

class Student:
    def __init__(self,sid,sname,sadd):
        self.sid=sid
        self.sname=sname
        self.sadd=sadd

class DBConnection:
    conn=None
    curr=None
    def __init__(self):
        pass
    @classmethod
    def conndb(cls):
        cls.conn=psycopg2.connect("dbname=flask_db user=postgres password=Finserv@2023")
        cls.curr=cls.conn.cursor()

    @classmethod
    def create_table(cls,tablename,f1,f2,f3):
        cls.curr.execute("CREATE TABLE " + str(tablename) + "(" + str(f1) + "varchar primary key," + str(f2) + "varchar" + str(f3) + "varchar );")
        cls.conn.commit()

    @classmethod
    def insert_db(cls,tablename,f1,f2,f3):
        cls.curr.execute("insert into" + str(tablename) + "values(%s,%s,%s)",(str(f1),str(f2),str(f3)))
        cls.conn.commit()

    @classmethod
    def select_result(cls,tablename):
        cls.curr.execute("Select * from " + str(tablename) + ";")
        students=cls.curr.fetchall()
        for student in students:
            print(student)

