from flask import Blueprint, flash, render_template, request, session, redirect, url_for
import tensorflow as tf
from src.app.Service.AuthService import AuthService
from src.app.Service.SystemManager import SystemManager
from src.app.Service.ML.ml import Predictor
from src.app.Helper.utils import b64ToImg, allowedFile, mask_img, np_img_to_b64
from src.app.Collection.UserCollection import UserCollection, User
from src.app.Collection.IsicCollection import IsicCollection

main = Blueprint('main', __name__)

system = SystemManager()
system.validate()
predictor = Predictor()
graph = tf.get_default_graph()


@main.route('/index')
@main.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@main.route('/login', methods=['POST', "GET"])
def login():
    if request.method == "POST":
        data = request.form.to_dict(flat=True)
        status = AuthService().login(data)
        if status == "Success":
            session['logged_in'] = True
            userData = AuthService().user.getUserData(data['username'])
            (session['user_id'], session['name'], session['surname'], session['email']) = (
                userData.id, userData.name, userData.surname, userData.email)
            AuthService().checkAdmin(data['username'])
            return redirect(url_for('main.index'), 302)
        else:
            flash(status)
    return index()


@main.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return index()


@main.route('/classifier-data', methods=['GET'])
def classifierData():
    isic = IsicCollection()
    try:
        page = int(request.args.get('page'))
        page = page if page is not None and page < 0 else 0
    except Exception as e:
        page = 0
    if request.args.get('prev-page'):
        page -= 1
        page = page if page < 0 else 0
    if request.args.get('next-page'):
        page += 1

    filters = request.args.to_dict(flat=True)
    if len(filters) > 0:
        filters.pop('page')
        try:
            filters.pop('prev-page')
        except Exception as e:
            None
        try:
            filters.pop('next-page')
        except Exception as e:
            None
        isic.parseFilters(filters)

    start = 0
    limit = offset = 20
    if page > 0:
        start = limit * page
        offset = start + 20
    pages = isic.getPages(limit)
    isic = isic.getCollection(offset, limit)
    return render_template('classifierData.html', data=isic, page=page, pages=pages)


@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        data = request.form.to_dict(flat=True)
        newUser = AuthService().createUser(data)
        if newUser == "Success":
            session['logged_in'] = True
            return redirect(url_for("main.success"), code=302)
        else:
            flash(newUser)
    return index()


@main.route('/success')
def success():
    return render_template('success.html')


@main.route('/project')
def project():
    return render_template('project.html')


@main.route("/userList", methods=['GET', 'POST'])
def userList():
    if session['logged_in'] and session['isAdmin']:
        users = UserCollection().getCollection()
        return render_template('userList.html', users=users)
    else:
        return redirect('index', 403, flash('Restricted!'))


@main.route("/reset", methods=['GET', 'POST'])
def reset():
    return index()


@main.route("/classification", methods=['GET', 'POST'])
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
            user = User()
            user.id = session['user_id']
            user.updateCheckedImages()
            return render_template("result.html", p_mal=y_pred['malignant'], p_ben=y_pred['benign'],
                                   img_masked=img_masked)

        except ValueError as e:
            print(e)
            flash('Wrong img size')
            return redirect(request.url)

    return render_template('classification.html')


@main.route("/editUser", methods=['GET', 'POST'])
def editUser():
    if not session['logged_in'] and session['isAdmin']:
        return redirect(url_for('main.index'), 403, flash("Restricted!"))
    if request.method == "POST":
        id = request.form.get('id')
        oldData = User().getUserById(id)
        newpassword = AuthService().encodePassword(
            request.form.get('password')) if oldData.password != request.form.get(
            'password') else oldData.password
        user = User()
        data = request.form.to_dict(flat=True)
        user.id = data.get('id')
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.email = data.get('email')
        user.password = newpassword
        user.admin = data.get('admin')
        user.username = data.get('username')
        user.update()
        return redirect(url_for('main.userList'), 302, flash('Changes has been saved!'))
    id = request.args.get('id')
    userData = User().getUserById(id)
    return render_template("editUser.html", userData=userData)


@main.route("/delete", methods=["GET"])
def deleteUser():
    if (session['isAdmin'] is not True):
        return redirect(url_for('main.index'), 302, flash("Admin privileges required"))
    id = request.args.get('id')
    if (session['user_id'] == id):
        return redirect(url_for('main.userList'), 302, flash('You cannot delete yourself'))
    else:
        userData = User()
        userData.id = id
        userData = userData.deleteUser()
        return redirect(url_for('main.userList'), 302, flash('Deleted user!'))

@main.route("/fullPreview", methods=["GET"])
def fullPreview():
    if not session['logged_in']:
        return redirect(url_for('main.index'), 403, flash("Restricted!"))
    id = request.args.get('id')
    metadata = IsicCollection().getMetadataById(id)
    return render_template("fullPreview.html", metadata = metadata)