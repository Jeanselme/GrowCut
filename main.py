""" 
	Software for the GrowCut and other algorithms
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

from Interface.interface import *
from Interface.control import *
from tkinter import *

root = Tk()
root.title("GrowCut")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ScrollBar Creation
vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

# Canvas Creation
canvas = ImageCanvas(root, width = 200, height = 200, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

# Controler Creation
controler = Control(canvas)
canvas.focus_set()
canvas.bind("<B1-Motion>", controler.foreground)
canvas.bind("<B3-Motion>", controler.background)
canvas.bind("<Button-1>", controler.foreground)
canvas.bind("<Button-3>", controler.background)
canvas.bind("<Control-B1-Motion>", controler.erase)
canvas.bind("<F5>", controler._compute)

# Menu Creation
mainmenu = Menu(root)

menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Open", command=controler._open)
menuFile.add_command(label="Close", command=controler._close)
menuFile.add_separator()
menuFile.add_command(label="Save as", command=controler._save)
menuFile.add_separator()
menuFile.add_command(label="Quit", command=root.quit) 

menuCompute = Menu(mainmenu, tearoff=0)
menuCompute.add_command(label="Contours", command=controler._compute)
# menuCompute.add_command(label="Face detection")

mainmenu.add_cascade(label = "File", menu=menuFile) 
mainmenu.add_cascade(label = "Compute", menu=menuCompute) 
mainmenu.add_command(label = "Help", command=controler._help) 
mainmenu.add_command(label = "About", command=controler._about) 

root.config(menu = mainmenu) 

root.mainloop()