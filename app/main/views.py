from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
from flask.views import View,MethodView

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Blogger'
    
    return render_template('index.html', title = title)

@main.route('/loggedin')
def loggedin():

    title = 'Blogger'

    return render_template('loggedin.html',title =title)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = f'{uname} Profile'
    return render_template("profile/profile.html", user = user, title = title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])

def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    title = 'Update | Profile'
    return render_template('profile/update.html',form =form, title = title)
@main.route('/user/<uname>/update/pic',methods= ['POST'])

def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

