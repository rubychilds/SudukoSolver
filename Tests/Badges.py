from Tkinter import *
from PIL import Image, ImageTk

master = Tk()



class Button:

	def __init__(self, file, master):
		self.b = Button(master, justify = LEFT)
		self.photo = PhotoImage(file="mine32.gif")
		self.b.config(image=self.photo,width="10",height="10")
		self.b.pack(side=LEFT)

	# when clicked invert image and go somewhere
	def buttonClick(self):
		self.buttonInvert = self.b = Button(master, justify = LEFT)
		self.photo = PhotoImage(file="mine32.gif")
		self.b.config(image=self.photo,width="10",height="10")
		self.b.pack(side=LEFT)


def main():

	self.frame = Tkinter.Frame(tk,relief=RIDGE,borderwidth=2)
    self.frame.pack()
 	
 	pos = 0
	button = []

	for f in files:

		button.append(Button(f))
		b.pack(sides[pos])
		pos += 1

	if 


	mainloop()

# CALL FOR MAIN
if __name__ == "__main__":
	main()
