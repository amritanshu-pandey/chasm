import os, getpass
from app import create_app
from flask.ext.script import Manager
from app import models, db
from flask.ext.migrate import Migrate, MigrateCommand
from app import getconfigurations


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)

@manager.command
def version():
	''' show the version number of the application'''
	print("Version: ",getconfigurations('version').value+'.'+getconfigurations('subversion').value)

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
