from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='admin.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	from .bp import bp as chasm_blueprint
	app.register_blueprint(chasm_blueprint)

	from .admin import admin as chasm_admin
	app.register_blueprint(chasm_admin, url_prefix='/admin')

	return app