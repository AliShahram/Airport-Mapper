#!/usr/bin/env python3

from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.constants
from tkinter import ttk
import webbrowser
import os.path
from frontend import Frontend
from importer import file_import


class GraphApp:
	@staticmethod
	def win_attributes(the_window):
		the_window.update_idletasks()
		w = the_window.winfo_screenwidth()
		h = the_window.winfo_screenheight()
		size = (410, 400)
		x = w / 2 - size[0] / 2
		y = h / 2 - size[1] / 2
		the_window.geometry("%dx%d+%d+%d" % (size + (x, y)))
		the_window.attributes('-topmost', 1)
		the_window.attributes('-topmost', 0)
		the_window.wm_title("Project 1: The Grapher")
		the_window.config(cursor='cross', background='#197278')
		the_window.overrideredirect(1)

	def __init__(self):
		self.win = Tk()
		self.win.protocol("WM_DELETE_WINDOW", self.win.destroy)
		self.win_attributes(self.win)
		self.web_server = object()
		self.server_is_running = False

		for button_type in ['upload', 'readme', 'quit']:
			ButtonCreator(self.win, button_type, self.fxn_mapper(button_type))

		self.win.mainloop()

	def run_front_end(self, graph_data):
		self.web_server = Frontend(graph_data)
		self.web_server.start()
		self.server_is_running = True

	def upload(self):
		filename = askopenfilename()
		if filename:
			graph_data = file_import(filename)
			self.run_front_end(graph_data)

	def quit(self):
		self.win.destroy()
		if self.server_is_running:
			self.web_server.stop()

	def open_readme(self):
		webbrowser.open("file://" + os.path.abspath("readme.txt"))

	def fxn_mapper(self, typ):
		if typ == 'upload':
			return self.upload
		if typ == 'readme':
			return self.open_readme
		if typ == 'quit':
			return self.quit


class ButtonCreator:
	def __init__(self, tk_obj, type, func):
		self.tk_obj = tk_obj
		self.img = PhotoImage(file="assets/" + type + ".gif")
		self.hover_img = PhotoImage(file="assets/" + type + "_hover.gif")

		self.btns_style = {'fill': tkinter.constants.BOTH, 'padx': '20', 'pady': '15'}
		self.style = ttk.Style()
		self.style.configure('BTN.TLabel', borderwidth=0, highlightthickness=0, padx=0, pady=0, ipadx=0, ipady=0)
		self.btn = ttk.Button(self.tk_obj, image=self.img, cursor='plus', command=func, style="BTN.TLabel")
		self.btn.pack(self.btns_style)

		self.btn.bind("<Enter>", self.on_enter)
		self.btn.bind("<Leave>", self.on_leave)

	def on_enter(self, event):
		self.btn.configure(image=self.hover_img)

	def on_leave(self, enter):
		self.btn.configure(image=self.img)
