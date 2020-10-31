from . import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))

   

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'

class Blog(db.Model):
   
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    blogger = db.Column(db.String())
    posted_at = db.Column(db.DateTime)
    # comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    # upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    # downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

    
    @classmethod
    def get_blogs(cls, id):
        blogs= Blog.query.order_by(blog_id=id).desc().all()
        return blogs


    def __repr__(self):
        return f'Blog {self.description}'    

class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
