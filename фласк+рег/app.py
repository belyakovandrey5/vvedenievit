import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


conn = psycopg2.connect(database="users",
                        user="postgres",
                        password="1488",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            try:
                cursor.execute("SELECT * FROM login.tabl1 WHERE login=%s AND password=%s",
                               (str(username), str(password)))
                records = list(cursor.fetchall())

                return render_template('account.html', full_name=records[0][1])
            except:
                return "Введите корректные данные"

        elif request.form.get("registration"):
            return redirect("/registration/")
    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        elif login != cursor.execute("SELECT * FROM login.tabl1 WHERE login=%s",
                           (str(login))):
        password = request.form.get('password')
            cursor.execute("INSERT INTO login.tabl1 (name, login, password) values (%s, %s, %s)",
                           (str(name), str(login), str(password)))
            conn.commit()
            return redirect("/login/")
    elif:
            return "Такой пользователь уже существует"
    return render_template('registration.html')
