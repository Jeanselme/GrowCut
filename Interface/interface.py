""" 
	Library for user interface
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from tkinter import *
from automaton import *
from PIL import Image, ImageTk, ImageDraw

class ImageCanvas(Canvas) :
	def __init__(self, master=None, **options) :
		self.open = False
		Canvas.__init__(self, master, options)

	def addImage(self, filepath) :
		""" Adds the image in the current window """
		self.image = Image.open(filepath)
		self.image_res = Image.open(filepath)
		self.photo = ImageTk.PhotoImage(self.image)
		self.config(height=self.photo.height(), width=self.photo.width())
		self.automaton = Automaton(self.photo.height(),self.photo.width(), list(self.image.getdata()))
		self.image_id = self.create_image(0,0,anchor=NW, image=self.photo)
		self.config(scrollregion=self.bbox("all"))
		self.open = True			

	def deleteImage(self) :
		""" Deletes the image from the window """
		self.delete(ALL)
		self.config(width=200, height=200, scrollregion=self.bbox("all"))
		self.open = False

	def save(self,filepath) :
		""" Saves the image in the indicated file """
		self.image_res.save(filepath)

	def compute(self, iteration) :
		""" Computes the growcut """
		items = list(self.find_all())
		items.remove(self.image_id)
		for item in items :
			self.delete(item)
		tab = self.automaton.compute(iteration)

		# Delete the old result
		del self.image_res
		self.image_res = self.image.copy()
		draw = ImageDraw.Draw(self.image_res)
		for x in range(self.photo.width()) :
			for y in range(self.photo.height()) :
				if tab[x+y*self.photo.width()] <= 0 :
					# Draw the new result
					self.create_line(x,y,x,y, stipple="gray75")
					draw.line((x,y,x,y), fill="rgb(0,0,0)")

	def foreground(self, event, radius) :
		""" Puts the pixel in the foreground and draw a circle """
		x = int(self.canvasx(event.x))
		y = int(self.canvasy(event.y))
		if (0 <= x and x < self.photo.width() and 0 <= y and y < self.photo.height()) :
			self.automaton.addForeground(x, y)
			self.create_oval(x-radius, y-radius,x+radius, y+radius, fill = "red")

	def background(self, event, radius) :
		""" Puts the pixel in the background and draw a circle  """
		x = int(self.canvasx(event.x))
		y = int(self.canvasy(event.y))
		if (0 <= x and x < self.photo.width() and 0 <= y and y < self.photo.height()) :
			self.automaton.addBackground(x, y)
			self.create_oval(x-radius, y-radius,x+radius, y+radius, fill = "blue")

	def erase(self, event, radius, radius_init) :
		""" Erase the circle """
		x = int(self.canvasx(event.x))
		y = int(self.canvasy(event.y))
		if (0 <= x and x < self.photo.width() and 0 <= y and y < self.photo.height()) :
			items = list(self.find_overlapping(x-radius, y-radius,x+radius, y+radius))
			items.remove(self.image_id)
			for item in items :
				self.automaton.erase(int(self.coords(item)[0]+radius_init), int(self.coords(item)[1]+radius_init))
				self.delete(item)

class AutoScrollbar(Scrollbar):
	def set(self, lo, hi):
		""" Sets the high and width of the adaptative scrollbar """
		if float(lo) <= 0.0 and float(hi) >= 1.0:
			self.tk.call("grid", "remove", self)
		else:
			self.grid()
		Scrollbar.set(self, lo, hi)