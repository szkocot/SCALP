from flask import Flask, flash, render_template, request, session, redirect, url_for
import config
from src.app.Service.AuthService import AuthService
from src.app.Service.JsonDataParser import JsonDataParser
from src.app.Service.SystemManager import SystemManager
from src.app.Service.ML.Prediction import Prediction
from src.app.Helper.utils import b64ToImg
from src.app.Collection.UserCollection import UserCollection

app = Flask(__name__)

system = SystemManager()
system.validate()

jsons = JsonDataParser()
jsons.setPath("D:\\ISIC\\ISIC\\benign\\description")


# fileList = jsons.importFiles()

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == "POST":
        auth = AuthService()
        data = request.form.to_dict(flat=True)
        status = auth.login(data)
        if status == "Success":
            session['logged_in'] = True
            return render_template('success.html')
        else:
            flash(status)
    return index()


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return index()


@app.route('/register', methods=['POST', 'GET'])
def register():
    auth = AuthService()
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        data = request.form.to_dict(flat=True)
        newUser = auth.createUser(data)
        if newUser == "Success":
            session['logged_in'] = True
            return redirect(url_for("success"), code=302)

        else:
            flash(newUser)
    return index()


@app.route('/success')
def success():
    return render_template('success.html')


@app.route("/predict", methods=['GET', 'POST'])
def predictMalignancy():
    img = b64ToImg(request.form.get('img_b64'))
    mask = b64ToImg(request.form.get('mask_b64'))
    with Prediction.graph.as_default():
        y_pred = Prediction.predictor(img, mask)

    return y_pred


@app.route("/adminPage", methods=['GET', 'POST'])
def adminPage():
    userCollection = UserCollection()
    users = userCollection.getUserCollection()
    return render_template('adminPage.html', users=users)


@app.route("/reset", methods=['GET', 'POST'])
def reset():
    return index()


if __name__ == '__main__':
    app.secret_key = config.CSRF_SESSION_KEY
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
