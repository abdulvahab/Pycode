#Labler
# Demostrate a lable

from tkinter import *
root = Tk()
root.title("Labeler")
root.geometry("200x50")
# create a frame in the window to hold other widgets

app = Frame(root)
app.grid()

# create lable in the frame

lbl= Label(app, text = "I'm a lable!")
lbl.grid()
# kickoff the window's event loop
root.mainloop()
