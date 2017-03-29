import flask

STATIC_DIR = '../html'
TEMPLATE_DIR = '../templates'

def process(app):
	app.template_folder = TEMPLATE_DIR

	@app.route('/')
	def root():
		return flask.render_template('index.html')

	@app.route('/<path:path>')
	def get_path(path):
		return flask.send_from_directory(STATIC_DIR, path)
