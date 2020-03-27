from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
basefile = "1"
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
        # self.wm_iconbitmap('icon.ico')

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        # self.basefile
        self.button()
        print(basefile)



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
        


    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("txt files","*.txt"),("all files","*.*")) )
        global basefile 
        basefile = os.path.basename(self.filename)
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        print(basefile)
    print(basefile)





root = Root()
root.mainloop()
print(basefile)

# import tkinter.filedialog as filedialog
# import tkinter as tk

# master = tk.Tk()

# def input():
#     input_path = tk.filedialog.askopenfilename()
#     input_entry.delete(1, tk.END)  # Remove current text in entry
#     input_entry.insert(0, input_path)  # Insert the 'path'


# def output():
#     path = tk.filedialog.askopenfilename()
#     input_entry.delete(1, tk.END)  # Remove current text in entry
#     input_entry.insert(0, path)  # Insert the 'path'


# top_frame = tk.Frame(master)
# bottom_frame = tk.Frame(master)
# line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

# input_path = tk.Label(top_frame, text="Input File Path:")
# input_entry = tk.Entry(top_frame, text="", width=40)
# browse1 = tk.Button(top_frame, text="Browse", command=input)

# output_path = tk.Label(bottom_frame, text="Output File Path:")
# output_entry = tk.Entry(bottom_frame, text="", width=40)
# browse2 = tk.Button(bottom_frame, text="Browse", command=output)

# begin_button = tk.Button(bottom_frame, text='Begin!')

# top_frame.pack(side=tk.TOP)
# line.pack(pady=10)
# bottom_frame.pack(side=tk.BOTTOM)

# input_path.pack(pady=5)
# input_entry.pack(pady=5)
# browse1.pack(pady=5)

# output_path.pack(pady=5)
# output_entry.pack(pady=5)
# browse2.pack(pady=5)

# begin_button.pack(pady=20, fill=tk.X)


# # master.mainloop()
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)