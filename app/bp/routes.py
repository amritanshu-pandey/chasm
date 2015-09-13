from flask import render_template
from . import bp

@bp.route('/')
def index():
	return render_template('bp/index.html', brand="Amritanshu's Blog")

@bp.app_errorhandler(404)
def err404(e):
	return render_template('404.html', brand="Amritanshu's Blog"),404