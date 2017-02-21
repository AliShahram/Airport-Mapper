#!/usr/bin/env python3

from multiprocessing import Process
from flask import Flask
from flask import render_template
import webbrowser


class Frontend:
	def __init__(self, graph_data):
		self.app = Flask(__name__)
		self.server = Process(target=self.run_server)
		self.graph_data = graph_data
		self.port_num = 7000

		@self.app.route("/")
		def index():
			return render_template("index.html")

		@self.app.route("/graph-data")
		def graph_data():
			return self.graph_data

	def start(self):
		self.server.start()

	def stop(self):
		self.server.terminate()
		self.server.join()

	def run_server(self):
		webbrowser.open_new("http://localhost:" + str(self.port_num) + "/")
		self.app.run(debug=True, port=self.port_num, use_reloader=False)
