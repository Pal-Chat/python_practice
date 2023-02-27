# python_practice
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the create operation
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor = mydb.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)
        mydb.commit()
        return 'User created successfully!'
    else:
        return render_template('create.html')

# Define the route for the read operation
@app.route('/read')
def read():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return render_template('read.html', result=result)

# Define the route for the update operation
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        cursor = mydb.cursor()
        sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        val = (name, email, id)
        cursor.execute(sql, val)
        mydb.commit()
        return 'User updated successfully!'
    else:
        return render_template('update.html')

# Define the route for the delete operation
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        cursor = mydb.cursor()
        sql = "DELETE FROM users WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        mydb.commit()
        return 'User deleted successfully!'
    else:
        return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
