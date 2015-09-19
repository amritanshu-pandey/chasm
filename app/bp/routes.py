from flask import render_template, request
from . import bp
from ..models import User, Category, Tag

@bp.route('/')
def index():
	catid=request.args.get('catid')
	return render_template('bp/index.html', User=User, Category=Category, Tag = Tag, catid = catid)

@bp.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404

