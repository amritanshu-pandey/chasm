from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
import hashlib
from flask import request


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow())
    isadmin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(200))
    mobile = db.Column(db.String(20))
    bio = db.Column(db.Text())
    avatar_hash = db.Column(db.String(64))
    posts = db.relationship('Post', backref='Author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Username: %s>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    body = db.Column(db.Text())
    url = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '< Post Title: %s>' % self.title

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True, unique=True)
    navigation = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return '< Category Name: %s>' % self.name