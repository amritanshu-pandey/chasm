from flask import render_template
from . import bp
from ..models import User, Category, Tag

@bp.route('/')
def index():
	return render_template('bp/index.html', User=User, Category=Category, Tag = Tag)

@bp.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404

