# Movie chooser
# Demostrate check buttons

from tkinter import *

class Application(Frame):
    """GUI Application for favourite movie types."""
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets for movie type choices."""
        # Create description label
        Label(self, text = "Choose your favourite movie types").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Select all that apply:").grid(row = 1, column = 0, sticky = W)

        # Create comedy check button
        self.likes_comedy = BooleanVar()
        Checkbutton(self, text = "Comedy",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        # Create drama check button
        self.likes_drama = BooleanVar()
        Checkbutton(self, text = "Drama",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)
        # Create romance check button
        self.likes_romance = BooleanVar()
        Checkbutton(self, text = "Drama",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        # Create text box to display results
        self.results_txt = Text(self, width = 40, height =5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Update textwidget and display user's favourite movie types."""
        likes = ""
        if self.likes_comedy.get():
            likes += "You like comedic movies.\n"
        if self.likes_drama.get():
            likes += "You like dramatic movies.\n"
        if self.likes_romance.get():
            likes += "You like romantic movies.\n"
            
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)
# main
root = Tk()
root.title("Movie Chooser")

app = Application(root)
root.mainloop()
        
