import flask

import articles

ARTICLE_DIR = '../articles'
STATIC_DIR = '../html'
TEMPLATE_DIR = '../templates'

def process(app):
	app.template_folder = TEMPLATE_DIR

	articles_ = articles.Articles()
	articles_.load_from_dir(ARTICLE_DIR)

	@app.route('/')
	def root_r():
		return flask.render_template('index.html')

	@app.route('/articles')
	def articles_r():
		def article_view(a):
			return {
				'id': a.id,
				'title': a.title,
				'date': a.date,
				'href': flask.url_for('article_r', article_id=a.id)
			}
		return flask.render_template('articles.html', articles=map(article_view, articles_.list_by_date()))

	@app.route('/article/<article_id>')
	def article_r(article_id):
		article = articles_.get(article_id)
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
