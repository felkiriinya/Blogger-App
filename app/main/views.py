from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from flask_login import login_required,current_user
# from ..models import User,Pitch,Comment,Upvote,Downvote
# from .forms import UpdateProfile,AddPitch,CommentForm,UpvoteForm,Downvote
# from .. import db,photos
from flask.views import View,MethodView

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'SafeSpace'
    
    return render_template('index.html', title = title)
