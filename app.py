from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
import mysql.connector as c

conn = c.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="souraj111"
)

if conn.is_connected():
  print("hello")
else:
  print("fucck")
mycursor = conn.cursor()

# table = "CREATE TABLE registration (email varchar(255), password varchar(255))"
# mycursor.execute(table)



app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# Models
class Me(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), unique=False, nullable=False)
	
	age = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Name : {self.first_name}, Age: {self.age}"\

# function to render index page
@app.route('/')
def index():
  
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    # sql = "INSERT INTO registration (email, password) VALUES (%s, %s)"
    # val = (username,password)
    # mycursor.execute(sql,val)
    mycursor.execute("INSERT INTO registration (email, password) VALUES (%s, %s)", (username,password))
    conn.commit()
    return f"done"

if __name__ == '__main__':
	app.run()

