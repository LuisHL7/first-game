from tkinter import *
import random

class LuckySeven:

	def __init__(self):
		self.crear_interfaz()

	def crear_interfaz(self):
		# Define the window
		window = Tk()
		window.minsize(340,450)
		window.geometry('340x450')

		# Add the button
		button = Button(window, text="Play", command=self.play, font='Arial 18 bold', background='Yellow')
		button.pack()

		# Load image
		photo = PhotoImage(file=r'dinero.png')
		
		# Save image in win
		self.win = Label(window, image = photo)

		# Create 3 fields
		self.fields = [StringVar() for element in range(3)]
		position = 10 #Starting margin of the first field
		for field in self.fields:
			label = Label(window, textvariable= field, background='Purple', foreground='White', font='Arial 42 bold')
			label.place(x=position, y=100, height=100, width=100)	
			position += 110 # startig margin of the second field

		# Show the window
		mainloop()

	def generate_number(self):
		return random.randint(0,9)


	def play(self):
		it_seven = False
		for i in range(3):
			value = self.generate_number()
			self.fields[i].set(value)
			if(value == 7):
				it_seven = True
		
		if(it_seven):
			self.win.pack(side=BOTTOM)
		else:
			self.win.pack_forget()


play = LuckySeven()
