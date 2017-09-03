import flask

import articles

ARTICLE_DIR = 'articles'
STATIC_DIR = 'html'
TEMPLATE_DIR = 'templates'

def process(app):
	app.template_folder = TEMPLATE_DIR

	_articles = articles.Articles()
	_articles.load_from_dir(ARTICLE_DIR)

	@app.route('/')
	def root_r():
		return flask.render_template('index.html', articles=map(_article_view, _articles.list_by_date()))

	@app.route('/articles', strict_slashes=False)
	def articles_r():
		return flask.render_template('articles.html', articles=map(_article_view, _articles.list_by_date()))

	@app.route('/article/<article_id>', strict_slashes=False)
	def article_r(article_id):
		article = _articles.get(article_id)
		view = {
			'title': article.title,
			'author': article.authors,
			'date': article.date,
			'content': article.content
		}
		return flask.render_template('article.html', **view)

	@app.route('/<path:path>')
	def get_path_r(path):
		return flask.send_from_directory(STATIC_DIR, path)

	def _article_view(a):
		return {
			'id': a.id,
			'title': a.title,
			'date': a.date,
			'href': flask.url_for('article_r', article_id=a.id)
		}
