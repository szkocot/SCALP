from flask import Flask, flash, render_template, request, session, redirect, url_for
import tensorflow as tf
import config, os
from src.app.Service.AuthService import AuthService
from src.app.Service.SystemManager import SystemManager
from src.app.Model.User import User
from src.app.Service.ML.ml import Predictor
from src.app.Helper.utils import b64ToImg, allowedFile, mask_img, np_img_to_b64
from src.app.Collection.UserCollection import UserCollection

app = Flask(__name__)
app.secret_key = config.CSRF_SESSION_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

system = SystemManager()
system.validate()

predictor = Predictor()
graph = tf.get_default_graph()


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
            userData = auth.user.getUserData(data['username'])
            (session['user_id'], session['name'], session['surname'], session['email']) = (
            userData.id, userData.name, userData.surname, userData.email)
            auth.checkAdmin(data['username'])
            return redirect(url_for('index'), 302)
        else:
            flash(status)
    return index()


@app.route('/preview')
def preview(page=1):
    return render_template('preview.html', models=models, page=page)


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return index()


# @app.route('/more')
# def more():
#     # this route will only be called from JavaScript when the page is scrolled
#
#     # read query parameters to know what data to get
#     page = request.args.get('page', 1)
#     per_page = request.args.get('per_page', 20)
#
#     # get the requested set of data
#     data = get_some_data(page, per_page)
#
#     # return it as json
#     return jsonify(data=format_data_appropriate_for_jsonify(data))

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


'''
@app.route("/predict", methods=['GET', 'POST'])
def predictMalignancy():
    img = b64ToImg(request.form.get('img_b64'))
    mask = b64ToImg(request.form.get('mask_b64'))
    with Prediction.graph.as_default():
        y_pred = Prediction.predictor(img, mask)

    return y_pred

@app.route("/binary", methods=['GET', 'POST'])
def binary():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url, 302, flash("Please upload correct file!"))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowedFile(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

    return render_template('binarization.html')
 '''


@app.route("/binary", methods=['GET', 'POST'])
def binary():
    return render_template('binarization.html')


@app.route("/segmentation", methods=['GET', 'POST'])
def segmentation():
    if request.method == "POST":
        segmentedImage = "this will be image"
        return render_template('segmentation.html', binImage=segmentedImage)

    return render_template('segmentation.html')


@app.route("/classification", methods=['GET', 'POST'])
def classification():
    if request.method == 'POST':
        try:
            files = {'image': request.files['image'], 'mask': request.files['mask']}
        except KeyError as e:
            flash('No selected file')
            return redirect(request.url)

        for _, v in files.items():
            if not allowedFile(v.filename):
                flash('Wrong file extension')
                return redirect(request.url)
        try:
            with graph.as_default():
                y_pred = predictor(request.files['image'], request.files['mask'])

            img_masked = np_img_to_b64((mask_img(request.files['image'], request.files['mask'])))
            return render_template("result.html", p_mal=y_pred['malignant'], p_ben=y_pred['benign'],
                                   img_masked=img_masked)

        except ValueError as e:
            print(e)
            flash('Wrong img size')
            return redirect(request.url)

    return render_template('classification.html')


@app.route("/editUser", methods=['GET', 'POST'])
def editUser():
    if not session['logged_in'] and session['isAdmin']:
        return redirect(url_for('index'), 302, flash("Restricted!"))
    if request.method == "POST":
        user = User()
        user.update(request.form.to_dict(flat=True))
        return redirect(url_for('adminPage'), 302, flash('Changes has been saved!'))
    id = request.args.get('id')
    userData = User()
    userData = userData.getUserById(id).__dict__
    return render_template("editUser.html", userData=userData)


@app.route("/delete", methods=["GET"])
def deleteUser():
    if (session['isAdmin'] is not True):
        return redirect(url_for('index'), 302, flash("Admin privileges required"))
    id = request.args.get('id')
    if (session['user_id'] == id):
        return redirect(url_for('adminPage'), 302, flash('You cannot delete yourself'))
    else:
        userData = User()
        userData = userData.deleteUser(id)
        return redirect(url_for('adminPage'), 302, flash('Deleted user!'))


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
