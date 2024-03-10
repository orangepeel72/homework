from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = 'information.db'
app = Flask(__name__)

def create_connection(db):
    try:
        connection = sqlite3.connect(db)
        return connection
    except Error as e:
        print(e)


@app.route('/')
def render_home():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT students.first_name, students.last_name, work.assignment, work.class FROM allocations INNER JOIN students ON students.id=allocations.student INNER JOIN work ON work.id=allocations.assignment ORDER BY students.id"
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return render_template('home.html', data = data)


if __name__ == '__main__':
    app.run()
