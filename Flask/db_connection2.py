import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='Finserv@2023')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS ownernew;')


cur.execute('CREATE TABLE ownernew (oid serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'pet_name varchar (50) NOT NULL,'
                                 'pet_type varchar (50) NOT NULL,'
                                 'date_of_adoption date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO ownernew(name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Aryamaan Pandey',
             'Tom',
             'Dog',
            )
            )

cur.execute('INSERT INTO ownernew(name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Akshit Khamesra',
             'Kitty',
             'Cat',
            )
            )


cur.execute('INSERT INTO ownernew (name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Tanuj Das',
             'Leo',
             'Cow',
            )
            )

cur.execute('INSERT INTO ownernew (name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Karan Bengani',
             'Bold',
             'Dog',
            )
            )

cur.execute('INSERT INTO ownernew (name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Hardik Garg',
             'Mastiff',
             'Cat',
            )
            )


conn.commit()


cur.close()
conn.close()