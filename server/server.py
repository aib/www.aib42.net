import flask
import os

import routes

def load():
	app = flask.Flask(__name__, root_path=os.getcwd())
	routes.process(app)
	return app

def main():
	load().run()

if __name__ == '__main__':
	main()
