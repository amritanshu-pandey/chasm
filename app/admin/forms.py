from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Email(), Length(1,64)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Log In')


class UserCreationForm(Form):
	firstname = StringField('First name', validators=[Required(), Length(1,100)])
	lastname = StringField('Last name', validators=[Required(), Length(1,100)])
	nickname = StringField('Nickname', validators=[Required(), Length(1,64)])
	email = StringField('Email', validators=[Required(), Email(), Length(1,64)])
	password = PasswordField('Enter Password', validators=[Required()])
	confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password',message='Password must match')])
	mobile = StringField('Mobile#')
	bio = TextAreaField('Bio')
	isadmin = BooleanField('Make this user an Administrator')
	submit = SubmitField('Submit')


