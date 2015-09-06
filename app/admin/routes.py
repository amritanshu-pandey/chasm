from flask import render_template, redirect, request, url_for, flash
from . import admin, forms
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..models import User


@admin.route('/')
@login_required
def index():
	return render_template('admin/index.html', brand='Chasm')

@admin.route('/login', methods=['GET','POST'])
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user,form.remember_me.data)
			print(user)
			print('validated')
			return redirect(url_for('.index'))
		flash('Invalid username or password')
	return render_template('admin/login.html', form=form)

@admin.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('.login'))

@admin.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404