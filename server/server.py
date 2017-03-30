import flask
import os

import routes

def main():
	app = flask.Flask(__name__, root_path=os.getcwd())

	routes.process(app)

	app.run()

if __name__ == '__main__':
	main()
