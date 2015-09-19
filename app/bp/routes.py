from flask import render_template, request
from . import bp
from ..models import User, Category, Tag, Post, db, Track

@bp.route('/')
def index():
	catid=request.args.get('catid')
	tracker = Track(
		ip = request.remote_addr,
		category = catid
	)
	db.session.add(tracker)
	db.session.commit()
	return render_template('bp/index.html', User=User, Category=Category, Tag = Tag, catid = catid)

@bp.route('/post/<slug>')
def viewPost(slug):
    post = Post.query.filter_by(url=slug).first()
    return render_template('bp/post.html', post=post, User=User, Category=Category, Tag = Tag)

@bp.app_errorhandler(404)
def err404(e):
	return render_template('404.html'),404

