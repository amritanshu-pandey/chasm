from flask import render_template, redirect, request, url_for, flash
from . import admin, forms
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..models import User
from app import db


@admin.route('/')
@login_required
def index():
	if current_user.isadmin:
		return render_template('admin/index.html', brand='Chasm')
	else:
		return render_template('bp/index.html', brand='Chasm')

@admin.route('/login', methods=['GET','POST'])
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			if user.isadmin:
				login_user(user,form.remember_me.data)
				print(user)
				print('validated')
				return redirect(url_for('.index'))
			else:
				login_user(user,form.remember_me.data)
				return redirect(url_for('bp.index'))
		flash('Invalid username or password')
	return render_template('admin/login.html', form=form)

@admin.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('.login'))

@admin.route('/create_user', methods=['GET','POST'])
@login_required
def createUser():
	form = forms.UserCreationForm()
	if(not current_user.isadmin):
		flash('Only an admin can create new users')
		return redirect(url_for('bp.index'))
	else:
		if form.validate_on_submit():
			user = User(
				email=form.email.data,
				firstname=form.firstname.data,
				lastname=form.lastname.data,
				username=form.nickname.data,
				mobile=form.mobile.data,
				bio = form.bio.data,
				password = form.password.data,
				isadmin = form.isadmin.data
				)
			db.session.add(user)
			db.session.commit()
			flash('User added succesfully')
			return redirect(url_for('.index'))
	return render_template('admin/user_entry.html', form=form)

@admin.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404