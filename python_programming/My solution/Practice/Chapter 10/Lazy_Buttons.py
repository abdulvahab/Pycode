# Lazy Buttons
# Demostrates creating buttons

from tkinter import *
r = Tk()
r.title("Lazy Buttons")
r.geometry("200x85")

# create a frame in the window to hold other widgets

a = Frame(r)
a.grid()

# create button in the frame
bttn1 = Button(a,text = "I do nothing!")
bttn1.grid()

# Create a second button in the frame

bttn2 = Button(a)
bttn2.grid()

bttn2.configure(text = "Me too!")

# create a third button in the frame
bttn3 = Button(a)
bttn3.grid()
bttn3["text"] = "same here!"

# kick off the window 's event loop
r.mainloop()
