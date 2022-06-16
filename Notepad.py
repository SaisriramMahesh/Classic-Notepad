# import
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class notepad:
	root = Tk()
	width = 300
	height = 300
	textarea = Text(root)
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff = 0)
	editmenu = Menu(menubar, tearoff = 0)
	helpmenu = Menu(menubar, tearoff = 0)
	# add scrollbar
	scrollbar = Scrollbar(textarea)
	file = None
	def __init__(self, **kwargs):
		# place icon
		try:
			self.root.wm_iconbitmap("Notepad.ico")
		except:
			pass
		# default window size is 300x300, to maximize or minimize
		try:
			self.width = kwargs['width']
		except KeyError:
			pass
		try:
			self.height = kwargs['height']
		except KeyError:
			pass
		# set window text
		self.root.title("Untitled - Notepad")
		# center the window
		screenwidth = self.root.winfo_screenwidth()
		screenheight = self.root.winfo_screenheight()
		# for left align
		left = (screenwidth / 2) - (self.width / 2)
		# for right align
		right = (screenheight / 2) - (self.height / 2)
		# top and bottom arrangement
		self.root.geometry('%dx%d+%d+%d' % (self.width,
						   self.height, left, right))
		# to make text area resizable
		self.root.grid_rowconfigure(0, weight = 1)
		self.root.grid_columnconfigure(0, weight = 1)
		# add controls
		self.textarea.grid(sticky = N + E + S + W)
		# open new file
		self.filemenu.add_command(label = "New", command = self.newfile)
		# open existing file
		self.filemenu.add_command(label = "Open", command = self.openfile)
		# save current file
		self.filemenu.add_command(label = "Save", command = self.savefile)
		# create a line in the dialog
		self.filemenu.add_separator()
		self.filemenu.add_command(label = "Exit", command = self.quitapplication)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)
		# cut feature
		self.editmenu.add_command(label = "Cut", command = self.cut)
		# copy feature
		self.editmenu.add_command(label = "Copy", command = self.copy)
		# paste feature
		self.editmenu.add_command(label = "Paste", command = self.paste)
		# edit feature
		self.menubar.add_cascade(label = "Edit", menu = self.editmenu)
		# description of notepad feature
		self.helpmenu.add_command(label = "About Notepad", command = self.showabout)
		self.menubar.add_cascade(label = "Help", menu = self.helpmenu)
		self.root.config(menu = self.menubar)
		self.scrollbar.pack(side = RIGHT, fill = Y)
		# scrollbar adjustment according to content
		self.scrollbar.config(command = self.textarea.yview)
		self.textarea.config(yscrollcommand = self.scrollbar.set)
	def quitapplication(self):
		self.root.destroy()
	#exit
	def showabout(self):
		showinfo("Notepad", "Hi! this is a classic Notepad created by Saisriram")
	def openfile(self):
		self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), 
			                       ("Text Documents", "*.txt")])
		if self.file == "":
			# if no file to open
			self.file = None
		else:
			# try opening the file
			# set the window title
			self.root.title(os.path.basename(self.file) + "- Notepad")
			self.textarea.delete(1.0, END)
			file = open(self.file, "r")
			self.textarea.insert(1.0, file.read())
			file.close()
	def newfile(self):
		self.root.title("Untitled - Notepad")
		self.file = None
		self.textarea.delete(1.0, END)
	def savefile(self):
		if self.file == None:
			self.file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt", 
				                          filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
			if self.file == "":
				self.file = None
			else:
				# try to save the file
				file = open(self.file, "w")
				file.write(self.textarea.get(1.0, END))
				file.close()
				# change window title
				self.root.title(os.path.basename(self.file) + "- Notepad")
		else:
			file = open(self.file, "w")
			file.write(self.textarea.get(1.0, END))
			file.close()
	def cut(self):
		self.textarea.event_generate("<<Cut>>")
	def copy(self):
		self.textarea.event_generate("<<Copy>>")
	def paste(self):
		self.textarea.event_generate("<<Paste>>")
	def run(self):
		# run the application
		self.root.mainloop()
# run the application
notepad = notepad(width = 300, height = 300)
notepad.run()
