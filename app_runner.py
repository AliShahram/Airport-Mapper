#!/usr/bin/env python3

from flask import Flask
from flask import render_template
import webbrowser



def graph_app(graph_data):
    
    app = Flask(__name__)
    port_num = 7878
        
    @app.route("/")
    def index():
        return render_template("index.html")
        
    @app.route("/graph-data")
    def get_data():
        return graph_data

    webbrowser.get("safari").open_new("http://localhost:" + str(port_num) + "/")
    app.run(host='localhost', port=port_num, debug=True)


