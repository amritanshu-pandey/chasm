from flask import render_template, redirect, request, url_for, flash
from . import admin, forms
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..models import User, Category
from app import db

cuser = current_user


@admin.route('/')
@login_required
def index():
    if current_user.isadmin:
        return render_template('admin/index.html', brand="Amritanshu's Blog")
    else:
        return render_template('bp/index.html', brand="Amritanshu's Blog")

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
                return redirect(url_for('.index'))
        flash('Invalid username or password')
    return render_template('admin/login.html', form=form , brand="Amritanshu's Blog")

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
            return redirect(url_for('.manageUsers'))
    return render_template('admin/user_entry.html', form=form)

@admin.route('/edit_profile', methods=['GET','POST'])
@login_required
def editProfile():
    form = forms.ProfileEditForm()
    if(not current_user.isadmin):
        flash('Only an admin can create new users')
        return redirect(url_for('bp.index'))
    else:
        if form.validate_on_submit():
            user = User.query.filter_by(email=current_user.email).first()
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            if User.query.filter_by(email=form.email.data).first() and form.email.data != current_user.email:
                flash('Email already exists! Please enter an unique email id')
                return redirect(url_for('.editProfile'))
            user.email = form.email.data
            if User.query.filter_by(username=form.nickname.data).first() and form.nickname.data != current_user.username :
                flash('Username already exists! Please enter an unique username')
                return redirect(url_for('.editProfile'))
            user.username = form.nickname.data
            user.mobile = form.mobile.data
            user.bio = form.bio.data
            user.isadmin = form.isadmin.data
            db.session.commit()
            flash('User profile modified succesfully')
            return redirect(url_for('.index'))
        else:
            form.firstname.data = current_user.firstname
            form.lastname.data = current_user.lastname
            form.nickname.data = current_user.username
            form.email.data = current_user.email
            form.mobile.data = current_user.mobile
            form.bio.data = current_user.bio
            form.isadmin.data = current_user.isadmin
    return render_template('admin/edit_profile.html',form=form)

@admin.route('/categories', methods=['GET','POST'])
@login_required
def addCategory():
    form = forms.CategoriesForm()
    if(not current_user.isadmin):
        flash('Only an admin can create new users')
        return redirect(url_for('bp.index'))
    else:
        if form.validate_on_submit():
            if Category.query.filter_by(name=form.name.data).first():
                flash('Category already exists')
                return redirect(url_for('admin.addCategory'))
            category = Category(
                name = form.name.data,
                navigation = form.navigation.data
            )
            db.session.add(category)
            db.session.commit()
            flash('Category added succesfully')
            return redirect(url_for('admin.addCategory'))
        categories = Category.query.all()
    return render_template('admin/categories.html', form=form, categories = categories)

@admin.route('/categories/<int:id>', methods=['GET','POST'])
@login_required
def editCategory(id):
    category = Category.query.filter_by(id=id).first()
    form = forms.CategoryEditForm()
    if(not current_user.isadmin):
        flash('Only an admin can access this page')
        return redirect(url_for('bp.index'))
    else:
        if form.validate_on_submit():
            cat = Category.query.filter_by(name=form.name.data).first()
            category.name = form.name.data
            category.navigation = form.navigation.data
            print("********",category.name)
            print(form.name.data)
            if cat and category.name!=form.name.data:
                flash('Category already exists')
                return redirect(url_for('admin.editCategory', id=id))
            db.session.commit()
            flash('Category updated succesfully')
            return redirect(url_for('admin.addCategory'))
        else:
            form.name.data = category.name
            form.navigation.data = category.navigation
        categories = Category.query.all()
    return render_template('admin/categories.html', form=form, categories = categories)

@admin.route('/category/delete/<int:id>', methods=['GET','POST'])
@login_required
def deleteCategory(id):
    if(not current_user.isadmin):
        flash('Only an admin can access this page')
        return redirect(url_for('bp.index'))
    else:
        cat = Category.query.get(id)
        Category.query.filter_by(id=id).delete()
        db.session.commit()
        print("++++++++++++++",cat)
        flash('Category '+cat.name+' deleted')
        return redirect(url_for('admin.addCategory'))

@admin.route('/users')
@login_required
def manageUsers():
    if(not current_user.isadmin):
        flash('Only an admin can access this page')
        return redirect(url_for('bp.index'))
    else:
        users = User.query.all()
    return render_template('admin/users.html', users = users)

@admin.app_errorhandler(404)
def err404(e):
    return render_template('404.html'),404