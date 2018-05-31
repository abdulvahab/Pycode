# Movie chooser
# Demostrate check buttons

from tkinter import *

class Application(Frame):
    """GUI Application for favourite movie types."""
    def __init__(self,master):
        """Initiliaze frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets for movie type choices."""
        # Create description label
        Label(self,
              text = "Choose your favourite movie type"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Select One:"
              ).grid(row = 1, column = 0, sticky = W)

        # Create variable for single, favourite type of movie
        self.favourite = StringVar()
        self.favourite.set(None)
        

        # Create comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favourite,
                    value = "comedy.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        # Create drama radio button
        
        Radiobutton(self, text = "Drama",
                    variable = self.favourite,
                    value = "Drama.",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)
        # Create romance radio button
        
        Radiobutton(self, text = "Romance",
                    variable = self.favourite,
                    value = "Romance.",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        # Create text box to display results
        self.results_txt = Text(self, width = 40, height =5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Update text widget and display user's favourite movie types."""
        message = "Your favourite movie is "
        message += self.favourite.get()
            
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)
# main
root = Tk()
root.title("Movie Chooser 2")

app = Application(root)
root.mainloop()
        
