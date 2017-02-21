#-*- coding: utf-8 -*-


from tkinter import *
import tkinter.constants
import tkinter.filedialog
import driver

class Window(tkinter.Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
        self.init_window()
        root.geometry("300x400")
        
    def init_window(self):
        self.master.title("QUIT")
        self.pack(fill=BOTH, expand = 3)
        self.quitButton = Button(self, text = "QUIT", command = self.client_exit)
        self.quitButton.place(x=120, y=50)
        
        
    
        # options for buttons
        button_opt = {'fill': tkinter.constants.BOTH, 'padx': '5', 'pady': '5'}
        
        # define buttons
        self.browseButton = Button(self, text='BROWSE', command=self.askopenfilename).pack(**button_opt)
        
        
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'This is a title'
        
        
        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'
        
    def askopenfilename(self):
        
        # get filename
        filename = tkinter.filedialog.askopenfilename(**self.file_opt)
    
        # open file on your own
        if filename:
            driver.runner(filename)

        
        
    def client_exit(self):
        exit()


if __name__ == "__main__":

    root = Tk()
    Window(root).pack()
    root.mainloop()
