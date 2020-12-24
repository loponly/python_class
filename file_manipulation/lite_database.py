# sqllite connect cursor execute fetchone fetchall
import sqlite3

connection = sqlite3.connect('data.db')

# connection = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword"
# )


cursor = connection.cursor()

query = 'CREATE TABLE  person(id int,name varchar)'
insert_qr = 'INSERT INTO person VALUES(1,"BOB")'

# SQL syntax
cursor.execute('SELECT * FROM person')

print(cursor.fetchall())

connection.commit()

connection.close()
