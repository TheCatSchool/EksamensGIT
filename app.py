from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
# import re

app = Flask(__name__)
app.secret_key = "saidkey"

def get_db_connection(): #defines the database
    return mysql.connector.connect(
        host="10.200.14.14",
        user="work",
        password="123",
        database="example"
    )
data = get_db_connection()


@app.route('/')
def some():
   return redirect('/home')
@app.route('/home')
def home():
    return render_template("home.html")