""" 
	Library for user interaction
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from tkinter.filedialog import *
from tkinter.messagebox import *

class Control :
	def __init__(self, canvas) :
		self.canvas = canvas

	def _help(self) :
		""" Shows a window with a help message """
		showinfo("Help", "Click with the right button of the mouse for applying background.\nClick with the left one in order to apply foreground.\nIf you press simultaneously Ctrl + right button, you can erase previous mistakes.\nPress F5 in order to refresh the computing of the new image.") 

	def _about(self) :
		""" Shows a window with author's name """
		showinfo("GrowCut", "Created by Vincent Jeanselme\nvincent.jeanselme@gmail.com")

	def _open(self) :
		""" Opens a new file if noone is already open """
		if self.canvas.open == False :
			filepath = askopenfilename(title="Open an image",filetypes=[('jpeg files','.jpg'),('png files','.png'),('all files','.*')])
			self.canvas.addImage(filepath) 
		else :
			showwarning("Close", "Close the current image in order to open a new one")

	def _close(self) :
		""" Closes the current Image if it is possible """
		if self.canvas.open == True :
			self.canvas.deleteImage()
		else :
			showwarning("Close", "Anyfile is open")

	def _save(self) :
		""" Saves the current content of the canvas if an image is open """
		if self.canvas.open == True :
			filepath = asksaveasfile(title="Save an image",filetypes=[('jpeg files','.jpg'),('png files','.png'),('all files','.*')])
			self.canvas.save(filepath.name)
		else :
			showwarning("Save", "Anyfile is open")

	def _compute(self, event=None) :
		""" Computes the GrowCut algorithm on the current image """
		if self.canvas.open == True :
			self.canvas.config(cursor="watch")
			self.canvas.compute(10)
			self.canvas.config(cursor="")
		else :
			showwarning("Compute", "Anyfile is open")

	def foreground(self, event) :
		""" Puts the pixel in background """
		if self.canvas.open == True :
			self.canvas.foreground(event, 5)

	def background(self, event) :
		""" Puts the pixel in background """
		if self.canvas.open == True :
			self.canvas.background(event, 5)

	def erase(self, event):
		""" Erases from the computing the selected pixel """
		if self.canvas.open == True :
			self.canvas.erase(event, 1, 5)