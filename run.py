from flask import Flask, flash, redirect, render_template, request, session, abort
import os, config
from src.app.Service.AuthService import AuthService
from src.app.Service.ML.Prediction import Prediction
from src.app.Helper.utils import b64ToImg, idToPath

app = Flask(__name__)


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    if(session['logged_in']):
        return index()
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
    if session.get('logged_in'):
        return index()
    if not session.get('logged_in'):
        return render_template('login.html')

    newUser = AuthService.createUser(request)
    if newUser == "Success":
        session['logged_in'] = True
    else:
        flash(newUser)
    return index()


@app.route("/predict", methods=['GET', 'POST'])
def predictMalignancy():
    img = b64ToImg(request.form.get('img_b64'))
    mask = b64ToImg(request.form.get('mask_b64'))
    with Prediction.graph.as_default():
        y_pred = Prediction.predictor(img, mask)

    return y_pred

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug = config.DEBUG)

