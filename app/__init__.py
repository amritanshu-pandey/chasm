from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='admin.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	moment.init_app(app)

	from .bp import bp as chasm_blueprint
	app.register_blueprint(chasm_blueprint)

	from .admin import admin as chasm_admin
	app.register_blueprint(chasm_admin, url_prefix='/admin')

	app.jinja_env.globals.update(navbar_categories=navbar_categories, getconfigurations=getconfigurations, getPosts = getPosts)

	return app

def navbar_categories():
	from app import db, models
	categories = models.Category.query.filter_by(navigation=True).all()
	return(categories)

def getconfigurations():
	from app import db, models
	configs = models.Config.query.first()
	return(configs)

def getPosts(id):
	from app import db, models
	posts = models.Post.query.filter_by(category_id=id).first()
	return(posts)