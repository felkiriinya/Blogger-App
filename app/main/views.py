from flask import render_template,request,redirect,url_for,abort,flash,session
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Quote
from .forms import UpdateProfile,AddBlog
from datetime import datetime

from .. import db,photos
from ..requests import get_quote
from flask.views import View,MethodView

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Blogger'
    
    return render_template('index.html', title = title)

@main.route('/quotes')
def quotes():

    '''
    '''
    quote = get_quote()
    title = 'Blogger | Quotes'
    
    return render_template('quotes.html', title = title,quote = quote)



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

@main.route('/blogs')
def blogs():
    title = 'Blogs Added'
    blog = Blog.query.filter_by().first()

    return render_template('blogs.html', title=title, blog =blog)

@main.route('/blogs/new', methods = ['GET','POST'])
@login_required
def new_blog():
    
    form = AddBlog()
    # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        # pitcher = form.pitcher.data
        description = form.description.data
        title = form.title.data 
        owner_id = current_user
        blogger = current_user
        new_blog = Blog(owner_id =current_user._get_current_object().id,blogger = blogger,title = title,description=description)
        db.session.add(new_blog)
        db.session.commit()
        
        
        return redirect(url_for('main.blogs'))
    return render_template('add_blog.html',form=form)


