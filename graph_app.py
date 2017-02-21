#!/usr/bin/env python3

from tkinter import *
from tkinter.filedialog import askopenfilename
from frontend import Frontend
from importer import file_import


class GraphApp:
	@staticmethod
	def win_attributes(the_window):
		the_window.update_idletasks()
		w = the_window.winfo_screenwidth()
		h = the_window.winfo_screenheight()
		size = (500, 500)
		x = w / 2 - size[0] / 2
		y = h / 2 - size[1] / 2
		the_window.geometry("%dx%d+%d+%d" % (size + (x, y)))
		the_window.attributes('-topmost', 1)
		the_window.attributes('-topmost', 0)
		the_window.wm_title("Project 1: The Grapher")

	def __init__(self):
		self.win = Tk()
		self.win.protocol("WM_DELETE_WINDOW", self.win.destroy)
		self.win_attributes(self.win)
		self.web_server = object()
		self.server_is_running = False

		upload_btn = Button(self.win, text='Upload File', command=self.upload_file)
		upload_btn.pack()
		quit_btn = Button(self.win, text='Quit', command=self.quit_program)
		quit_btn.pack()

		self.win.mainloop()

	def upload_file(self):
		filename = askopenfilename()
		graph_data = file_import(filename)
		self.run_front_end(graph_data)

	def quit_program(self):
		self.win.destroy()
		if self.server_is_running:
			self.web_server.stop()

	def run_front_end(self, graph_data):
		self.web_server = Frontend(graph_data)
		self.web_server.start()
		self.server_is_running = True
