import sqlite3
connection=sqlite3.connect("Database.db")
cursor = connection.cursor()

sql="ATTACH DATABASE 'Database.db' as 'Database'"
cursor.execute(sql)

sqlCommand = """
    CREATE TABLE comments ( 
	post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL, 
	email TEXT NOT NULL, 
	website_url TEXT NULL, 
	comment TEXT NOT NULL );"""

#cursor.execute(sqlCommand)
print("table created in Database.db")


sql = """INSERT INTO comments ( name, email, website_url, comment )
VALUES ( 'Shivam Mamgain', 'xyz@gmail.com',
'shivammg.blogspot.com', 'Great tutorial for beginners.' );"""

cursor.execute(sql) 

sql = """
UPDATE comments
SET name = 'John Smith'
WHERE email = 'xyz@gmail.com';
"""
cursor.execute(sql)

dude = ('Jane Smith', 'xxx@gmail.com', 'jane.com','I like this.')
sql = ''' INSERT INTO comments ( name, email, website_url, comment )
VALUES(?,?,?,?) '''
cursor.execute(sql,dude)

sql = "SELECT * FROM comments"
cursor.execute(sql)

#sql = "DELETE FROM comments WHERE post_id = 2;"
#cursor.execute(sql)

result = cursor.fetchall()
for i in result:
    print(i)


connection.commit()
connection.close()
