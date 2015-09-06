from flask import render_template
from . import bp

@bp.route('/')
def index():
	return render_template('bp/index.html', brand='Chasm')

@bp.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404