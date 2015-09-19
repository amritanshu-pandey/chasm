from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL
from wtforms import ValidationError
from ..models import User, load_user
from .routes import *
from flask.ext.login import login_user, logout_user, login_required, current_user
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email(), Length(1,64)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Log In')


class UserCreationForm(Form):
	firstname = StringField('First name', validators=[DataRequired(), Length(1,100)])
	lastname = StringField('Last name', validators=[DataRequired(), Length(1,100)])
	nickname = StringField('Nickname', validators=[DataRequired(), Length(1,64)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(1,64)])
	password = PasswordField('Enter Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',message='Password must match')])
	mobile = StringField('Mobile#')
	bio = TextAreaField('Bio')
	isadmin = BooleanField('Make this user an Administrator')
	submit = SubmitField('Submit')

class ProfileEditForm(Form):
	firstname = StringField('First name', validators=[DataRequired(), Length(1,100)])
	lastname = StringField('Last name', validators=[DataRequired(), Length(1,100)])
	nickname = StringField('Nickname', validators=[DataRequired(), Length(1,64)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(1,64)])
	mobile = StringField('Mobile#')
	bio = TextAreaField('Bio')
	isadmin = BooleanField('Make this user an Administrator')
	submit = SubmitField('Submit')
	
class CategoriesForm(Form):
	name = StringField('Add new category', validators=[DataRequired(), Length(1,100)])
	navigation = BooleanField('Visible in Navigation Bar')
	submit = SubmitField('Add Category')

class CategoryEditForm(Form):
	name = StringField('Category Name', validators=[DataRequired(), Length(1,100)])
	navigation = BooleanField('Visible in Navigation Bar')
	submit = SubmitField('Save Category')

class UserEditForm(Form):
	firstname = StringField('First name', validators=[DataRequired(), Length(1,100)])
	lastname = StringField('Last name', validators=[DataRequired(), Length(1,100)])
	nickname = StringField('Nickname', validators=[DataRequired(), Length(1,64)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(1,64)])
	mobile = StringField('Mobile#')
	bio = TextAreaField('Bio')
	isadmin = BooleanField('Make this user an Administrator')
	submit = SubmitField('Submit')

class PostEntryForm(Form):
	title = StringField('Title', validators=[DataRequired(message='Please fill'), Length(1,500)])
	intro_text = PageDownField('Intro Text')
	body = PageDownField('Body')
	category = SelectField('Category', coerce=int)
	tags = StringField('Tags', validators=[Length(0,1000)])
	submit = SubmitField('Submit')

class PostEditForm(Form):
	title = StringField('Title', validators=[DataRequired(message='Please fill'), Length(1,500)])
	intro_text = PageDownField('Intro Text')
	body = PageDownField('Body')
	url = StringField('URL', validators=[DataRequired(), Length(1,200)])
	category = SelectField('Category', coerce=int)
	tags = StringField('Tags', validators=[Length(0,1000)])
	submit = SubmitField('Submit')


