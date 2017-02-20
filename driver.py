#!/usr/bin/env python3

from importer import file_import
from app_runner import graph_app

def runner(file_path):

	# This file path should be acquired with Tkinter or smth.
    #file_path = "input_files/data_airports_v2.csv"

	data = file_import(file_path)

	graph_app(data)


if __name__ == "__main__":
	main()
