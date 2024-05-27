import tkinter
import drawpad


class LoginProgram:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.configure(bg="black")
        self.window.geometry("780x340")
        self.title = tkinter.Label(self.window, text="To Unlock my Drawing Pad...", fg="#00FF00", bg="#000000", font=("Calibri", 48))
        self.username_title = tkinter.Label(self.window, text=" Enter Username", fg="#00FF00", bg="#000000", font=("Calibri", 24))
        self.username_input = tkinter.Entry(self.window, fg="#000000", bg="#00ff00", font=("Calibri", 24))
        self.password_title = tkinter.Label(self.window, text="Enter Password:", bg="#000000", fg="#00FF00", font=("Calibri", 24))
        self.password_input = tkinter.Entry(self.window, fg="#000000", bg="#00ff00", font=("Calibri", 24), show="*")
        self.button = tkinter.Button(self.window, text="Login", fg="#00FF00", bg="#000000", command=self.printer, font=("Calibri", 20))

        self.title.pack()
        self.username_title.pack()
        self.username_input.pack()
        self.password_title.pack()
        self.password_input.pack()
        self.button.pack()

    def run(self):
        self.window.mainloop()

    def printer(self):
        if self.username_input.get().lower() == "sulaiman.nasir" and self.password_input.get() == "funtech":
            app = drawpad.DrawPadApp()
            app.run()
            pass
        else:
            print("incorrect Username or Password")

window = LoginProgram()
window.run()
