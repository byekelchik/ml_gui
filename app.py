from ml_model import *
from db_connection import connection
from flask import Flask, request, render_template, redirect
import pyodbc
import sys

app = Flask(__name__)

@app.route('/')
def index():
    
    newList = []
    cnxn = connection.get_data.connect_to_db()
    cursor = cnxn.cursor()
    rows = cursor.execute('SELECT * FROM testdb.test LIMIT 10')
    for row in rows.fetchall(): 
        newList.append(row)
    
    return render_template('index.html', tasks=newList)

@app.route('/addrow/', methods=['GET','POST'])
def add_row():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = int(request.form['age'])

        print(id, flush=True)
        print(type(id),file=sys.stdout)

        #query
        query = "INSERT INTO testdb.test(ID, FirstName, LastName, Age) VALUES ({s_id}, {s_firstname} ,{s_lastname}, {s_age} +)".format(s_id=str(id), s_firstname=firstname, s_lastname=lastname, s_age=str(age))

        cnxn = connection.get_data.connect_to_db()
        cursor = cnxn.cursor()
        rows = cursor.execute(
            """
            INSERT INTO testdb.test
            (ID, FirstName, LastName, Age)
            VALUES (?, ?, ?, ?)
            """,
            (str(id), lastname, firstname, str(age))
        )
        cursor.commit()
        cursor.close()
        return redirect('/')

    else:
        return render_template('addrow.html')


if __name__ == "__main__":
    app.run(debug=True)
