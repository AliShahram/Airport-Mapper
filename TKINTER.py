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
        options['filetypes'] = [('all files', '.*'), ('text files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.csv'
        options['parent'] = root
        options['title'] = 'This is a title'
        
        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'
        
        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1
        
        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'
        
    def askopenfilename(self):
        
        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """
        
        # get filename
        filename = tkinter.filedialog.askopenfilename(**self.file_opt)
    
        # open file on your own
        if filename:
            driver.runner(filename)
            return (filename)
    
    
        
        
        
    def client_exit(self):
        exit()




root = Tk()
root.geometry("300x400")
app = Window(root)
root.mainloop()
