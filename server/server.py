#!/usr/bin/env python3

import flask
import os

import routes

def main():
	app = flask.Flask(__name__, root_path=os.getcwd())

	routes.process(app)

	app.run('0.0.0.0', '80')

if __name__ == '__main__':
	main()
