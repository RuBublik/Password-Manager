from scapy.all import *
from Tkinter import *

def openFileWindow():
	fileWindow=Tk()
	fileWindow.mainloop()
	
def closePassWindow():
	passwordWindow.destroy()
	openFileWindow()

def checkPassword():
	password=passEntry.get()
	if password=="asdf":
		closePassWindow()
	statusText.set("Incorrect password, please retry.")
	

def openPassWindow():
	global passwordWindow
	passwordWindow=Tk()
	passwordWindow.resizable(width=False,heigth=False)
	global statusText
	statusText=StringVar()
	statusText.set(" ")
	passLabel=Label(passwordWindow,text="     Please input the password:      ")
	passLabel.pack()
	global passEntry
	passEntry=Entry(passwordWindow)
	passEntry.pack()
	passStatus=Label(passwordWindow,fg="red",textvariable=statusText)
	passStatus.pack()
	passButton=Button(passwordWindow,text="   Proceed   ",command=checkPassword)
	passButton.pack()
	passwordWindow.mainloop()
	
	
openPassWindow()
