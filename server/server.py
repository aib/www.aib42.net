#!/usr/bin/env python3

import flask

import routes

def main():
	app = flask.Flask(__name__)

	routes.process(app)

	app.run('0.0.0.0', '8000')

if __name__ == '__main__':
	main()
