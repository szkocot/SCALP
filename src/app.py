from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from src.app.Service.AuthService import AuthService

app = Flask(__name__)


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('../templates/login.html')
    else:
        return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    status = AuthService.login(request)
    if status == "Success":
        session['logged_in'] = True
    else:
        flash(status)
    return index()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()

@app.route('/register', methods=['POST'])
def register():
    newUser = AuthService.createUser(request)
    if newUser == "Success":
        session['logged_in'] = True
    else:
        flash(newUser)
    return index()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000)
