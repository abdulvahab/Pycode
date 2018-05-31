# Guess my number game usinf GUI

from tkinter import*
import random

class Application(Frame):
    def __init__(self,master):
        super (Application,self).__init__(master)
        self.grid()
        self.attempts = 2
        self.create_widgets()
        
    def create_widgets(self):
        self.number = random.randint(1,101)
        Label(self,
              text = "Guess your number between 1 & 100"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Enter your number"
              ).grid( row = 1, column = 0, sticky = W)
        
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 1, column = 1, sticky = W)
        self.bttn  = Button(self,
                     text = "SUBMIT",
                     command = self.play 
                     ).grid( row = 2, column = 1, sticky = W)
        
        self.result_txt = Text(self, width = 75, height = 2, wrap= WORD)
        self.result_txt.grid(row = 4, column = 0, columnspan = 4)
            
    def play(self):
        
        if self.attempts:
            guess = int(self.guess_ent.get())
            if guess == self.number:
                result = "Congratulation you have guessed it",guess
                tries = "attempts used:",self.attempts
                self.choice()                                       
            elif (guess > 100 or guess < 1) :
                result = guess ,"is invalid number,guess between 1 & 100"
                tries= "attempts left:",self.attempts
            elif guess > self.number:
                self.attempts -=1
                result = "Guess Lower than:",guess
                tries = "attempts left:",self.attempts
            elif guess < self.number :
                self.attempts -=1
                result = "Guess Higher than:",guess
                tries = "attempts left:",self.attempts
        else:
            result = "You have used maximum tries"
            self.choice()
     
                   
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, result)
        self.result_txt.insert(0.0, "\n")
        self.result_txt.insert(0.0, tries)                  
  
    def choice(self):
        bttn1 = Button(self,
               text = "Play Again",
               command = self.play_again
               ).grid(row = 8, column = 1, sticky = W)
        bttn2 = Button(self,
               text = "Quit",
               command = self.good_bye
               ).grid(row=8, column = 1, sticky = E)
        
        
    def good_bye(self):
        close(app)
                
 
    def play_again(self):
        self.destroy()
        start()

       
root = Tk()
root.title("Guess Number Game")
def start():
    app = Application(root)
    root.mainloop
def close(app):
    app.destroy()
    Lable(app,text ="Good Bye")


start()

        



"""def good_bye():
        root = Tk()
        root.title("Guess Number Game")
        app = Application(root)
        app.pack()
        mainloop()
        app = Application(root)
        bttn2 = Button(app,
                text = "Quit",
                command = self.good_bye
                ).grid(row=8, column = 1, sticky = E)
        bttn2.pack()
        root.destro()
        mainloop()
       root = Tk()
        app = Frame(root)
        Label(self,
              text = "Good-Bye , See You again"
              ).grid(row =0 , column = 0, sticky = W)"""
     




        
        
