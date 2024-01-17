from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
import sqlite3
import csv

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)
#db = connection 



@app.route('/')
def index():
    connection=sqlite3.connect("Database.db")
    cursor = connection.cursor()

    sql="ATTACH DATABASE 'Database.db' as 'database'"
    cursor.execute(sql)


    with open('log1.csv') as i:
        reader = csv.reader(i)
        data = list(reader)


    sqlCommand = """
        CREATE TABLE logs ( 
	    post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	    date TEXT NOT NULL, 
	    duration TEXT NOT NULL, 
	    average_temp TEXT NOT NULL, 
	    net_energy_effect TEXT NOT NULL );"""


    #cursor.execute(sqlCommand)
    # inserting data into the table
    for row in data:
        sql = ''' INSERT INTO logs (date, duration, average_temp, net_energy_effect) VALUES(?,?,?,?) '''
        cursor.execute(sql,row)


    sql = "SELECT * FROM logs"
    cursor.execute(sql)
    
    #result = cursor.fetchall()
    #for i in result:
     #   print(i)


    records = cursor.fetchall()
    return render_template('index.html', records=records)
    
    
    connection.commit()
    connection.close()


if __name__ == "__main__":
    app.run(debug=True)

