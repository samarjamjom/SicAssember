# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# import os
# basefile = "1"
# class Root(Tk):
#     def __init__(self):
#         super(Root, self).__init__()
#         self.title("Python Tkinter Dialog Widget")
#         self.minsize(640, 400)
#         # self.wm_iconbitmap('icon.ico')

#         self.labelFrame = ttk.LabelFrame(self, text = "Open File")
#         self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
#         # self.basefile
#         self.button()
#         print(basefile)



#     def button(self):
#         self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
#         self.button.grid(column = 1, row = 1)
        


#     def fileDialog(self):

#         self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
#         (("txt files","*.txt"),("all files","*.*")) )
#         global basefile 
#         basefile = os.path.basename(self.filename)
#         self.label = ttk.Label(self.labelFrame, text = "")
#         self.label.grid(column = 1, row = 2)
#         self.label.configure(text = self.filename)
#         print(basefile)
#     print(basefile)





# root = Root()
# root.mainloop()
# print(basefile)

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


import tkinter as tk

root = tk.Tk()


text2 = tk.Text(root, height=20, width=50)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()







# locctr = tk.Text(root, height=2, width=40)
# locctr.pack()
# quote = "\nLocation counter: "+str(loc_ctr)
# locctr.insert(tk.END, quote)

# length = tk.Text(root, height=2, width=40)
# length.pack()
# quote = "\nthe length of the program: "+str(prog_leng)
# length.insert(tk.END, quote)

# text2 = tk.Text(root, height=50, width=40)
# scroll = tk.Scrollbar(root, command=text2.yview)
# text2.configure(yscrollcommand=scroll.set)
# text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
# text2.tag_configure('big', font=('Verdana', 20, 'bold'))
# text2.tag_configure('color',
#                     foreground='#476042',
#                     font=('Tempus Sans ITC', 12, 'bold'))
# text2.tag_bind('follow',
#                '<1>',
#                lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
# text2.insert(tk.END,'\nSYMTAB\n', 'big')
# quote =  SymbolTable
# text2.insert(tk.END, quote, 'color')
 
# text2.pack(side=tk.LEFT)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)


# text3 = tk.Text(root, height=50, width=40)
# scroll = tk.Scrollbar(root, command=text3.yview)
# text3.configure(yscrollcommand=scroll.set)
# text3.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
# text3.tag_configure('big', font=('Verdana', 20, 'bold'))
# text3.tag_configure('color',
#                     foreground='#476042',
#                     font=('Tempus Sans ITC', 12, 'bold'))
# text3.tag_bind('follow',
#                '<1>',
#                lambda e, t=text3: t.insert(tk.END, "Not now, maybe later!"))
# text3.insert(tk.END,'\nLITTAB\n', 'big')
# quote =  SymbolTable
# text3.insert(tk.END, quote, 'color')
 
# text3.pack(side=tk.RIGHT)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)
