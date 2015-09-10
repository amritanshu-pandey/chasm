#!venv/bin/python3
import os, getpass
from app import create_app
from flask.ext.script import Manager
from app import models, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def version():
	''' show the version number of the application'''
	print("Version 0.1")

@manager.command
def adduser(email,username, isadmin):
	''' Add new tracked user of the application '''
	pwd1 = getpass.getpass('Password: ') 
	pwd2 = getpass.getpass('Confirm Password: ')
	if pwd1!=pwd2:
		raise AttributeError("Password doesn't match")
	else:
		user = models.User(email=email, username=username, password=pwd1, isadmin=isadmin)
		db.create_all()
		print(user)
		db.session.add(user)
		if db.session.commit():
			print('User added succesfully')


if __name__ == '__main__':
	manager.run()