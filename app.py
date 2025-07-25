from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
@app.route('/')
def home():
    return "Hello from Flask!"
