import os

BASEDIR = os.path.abspath(os.path.dirname('__file__'))

class Config():
	SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
	SQLALCHEMY_DATABASE_URI = "postgresql://chasmd:dev@localhost/chasm-devel"

class TestingConfig(Config):
	TESTING = True

class ProductionConfig(Config):
	pass

config = {
	"development": DevelopmentConfig,
	"testing": TestingConfig,
	"production": ProductionConfig,

	"default": DevelopmentConfig
}	