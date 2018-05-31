# click_counter
# Demostrates binding an event with a event handler


from tkinter import *
class Application(Frame):
    """A GUI Application which counts button clicks"""
    def __init__(self,master):
        """Initilize the Frame"""
        super(Application,self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 #number of button clicks
        self.create_widget()

    def create_widget(self):
        """creates button which display number of clicks"""
        self.bttn = Button(self, text = "total clicks : 0")
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Increse click count and display new total."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks:" + str(self.bttn_clicks)

        
        

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x200")

app = Application(root)

root.mainloop()
            



