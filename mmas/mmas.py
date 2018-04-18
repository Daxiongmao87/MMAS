ifrom flask import Flask, render_template, request
from flask_mysqldb import MySQL

mysql = MySQL(app)
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

def fetchdata():
    cur = mysql.connect().cursor()
    cur.execute('''SELECTT * FROM table''') #Obviously needs to be changed
    rv = cur.fetchone()

    return str(rv)

if __name__ == "__main__":
    app.run()
