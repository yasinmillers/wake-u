import sqlite3

conn=sqlite3.connect('student.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT ,
                  course TEXT ,
                  marks INTEGER ,
                  email TEXT )
                  ''')  

cursor.execute("INSERT INTO students (name, course, marks, email) VALUES ('John Doe', 'Python', 85, 'john.doe@example.com')")       
cursor.execute("INSERT INTO students (name, course, marks, email) VALUES ('Jane Smith', 'Data Science', 92, 'jane.smith@example.com')")
cursor.execute("INSERT INTO students (name, course, marks, email) VALUES ('Alice Johnson', 'Web Development', 78, 'alice.johnson@example.com')")    
conn.commit()
