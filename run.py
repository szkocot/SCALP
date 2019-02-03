from flask import Flask, flash, render_template, request, session, redirect, url_for
import config
from src.app.Service.AuthService import AuthService
from src.app.Service.SystemManager import SystemManager
from src.app.Model.User import User
from src.app.Service.ML.Prediction import Prediction
from src.app.Helper.utils import b64ToImg
from src.app.Collection.UserCollection import UserCollection
import timeit

start = timeit.timeit()
app = Flask(__name__)

system = SystemManager()
system.validate()

end = timeit.timeit()
print(end - start)


@app.route('/index')
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
            auth.checkAdmin(data['username'])
            return redirect(url_for('index'), 302)
        else:
            flash(status)
    return index()


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
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


@app.route('/project')
def project():
    return render_template('project.html')


@app.route("/predict", methods=['GET', 'POST'])
def predictMalignancy():
    img = b64ToImg(request.form.get('img_b64'))
    mask = b64ToImg(request.form.get('mask_b64'))
    with Prediction.graph.as_default():
        y_pred = Prediction.predictor(img, mask)

    return y_pred


@app.route("/adminPage", methods=['GET', 'POST'])
def adminPage():
    if session['logged_in'] and session['isAdmin']:
        userCollection = UserCollection()
        users = userCollection.getUserCollection()
        return render_template('adminPage.html', users=users)
    else:
        return redirect('index', 403, flash('Restricted!'))


@app.route("/reset", methods=['GET', 'POST'])
def reset():
    return index()


@app.route("/binary", methods=['GET', 'POST'])
def binary():
    if request.method == "POST":
        binImage = "this will be image"
        return render_template('binarization.html', binImage=binImage)

    return render_template('binarization.html')


@app.route("/segmentation", methods=['GET', 'POST'])
def segmentation():
    if request.method == "POST":
        segmentedImage = "this will be image"
        return render_template('segmentation.html', binImage=segmentedImage)

    return render_template('segmentation.html')


@app.route("/editUser", methods=['GET', 'POST'])
def editUser():
    if request.method == "POST":
        user = User()
        user.update(request.form.to_dict(flat=True))
        return redirect(url_for('adminPage'), 302, flash('Changes has been saved!'))
    id = request.args.get('id')
    userData = User()
    userData = userData.getUserById(id)
    return render_template("editUser.html", userData=userData)


@app.route("/delete", methods=["GET"])
def deleteUser():
    if (session['isAdmin'] is not True):
        return redirect(url_for('index'), 302, flash("Admin privileges required"))
    id = request.args.get('id')
    userData = User()
    userData = userData.deleteUser(id)
    return redirect(url_for('adminPage'), 302, flash('Deleted user!'))


if __name__ == '__main__':
    app.secret_key = config.CSRF_SESSION_KEY
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
