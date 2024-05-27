import tkinter
import window


class DrawPadApp(window.GUIWindow):
    def __init__(self):
        super().__init__(1000, 720, title="Drawing Pad")
        self.canvas = tkinter.Canvas(self.window, width=self.width-80, height=self.height-180, bg="white")
        self.canvas.bind("<ButtonRelease-1>", self.reset_pos)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.draw_width = 5
        self.draw_col = "#000000"

        button_frame = tkinter.Frame(self.window)
        button_frame.pack()

        self.button = tkinter.Button(button_frame, command=self.red, bg="red")
        self.button1 = tkinter.Button(button_frame, command=self.orange, bg="orange")
        self.button2 = tkinter.Button(button_frame, command=self.yellow, bg="yellow")
        self.button3 = tkinter.Button(button_frame, command=self.lime, bg="lime")
        self.button4 = tkinter.Button(button_frame, command=self.green, bg="green")
        self.button5 = tkinter.Button(button_frame, command=self.dark_blue, bg="dark blue")
        self.button6 = tkinter.Button(button_frame, command=self.light_blue, bg="light blue")
        self.button7 = tkinter.Button(button_frame, command=self.pink, bg="pink")
        self.button8 = tkinter.Button(button_frame, command=self.purple, bg="purple")
        self.button9 = tkinter.Button(button_frame, command=self.brown, bg="#964B00")
        self.button10 = tkinter.Button(button_frame, command=self.grey, bg="grey")
        self.button11 = tkinter.Button(self.window, command=self.black, bg="black")
        self.button12 = tkinter.Button(self.window, command=self.white, bg="white")

        self.button.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button1.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button2.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button3.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button4.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button5.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button6.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button7.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button8.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button9.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button10.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)


        self.button99 = tkinter.Button(self.window, command=self.changee, text="Submit", font=("Verdana", 8))

        self.button_clear = tkinter.Button(self.window, command=self.clear_canvas, text="Clear Canvas", font=("Verdana", 10))

        self.user_input_title = tkinter.Label(self.window, text="Enter Pencil Width:", fg="#000000",font=("Calibri", 12))
        self.user_inputtt = tkinter.Entry(self.window, fg="#000000", font=("Calibri", 12))

        self.window.bind("<space>", lambda event: self.canvas.delete("all"))
        self.mouse_pos = (None, None)   # hold the previous mouse position

        self.canvas.pack()

        self.user_input_title.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.user_inputtt.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button99.pack(side=tkinter.LEFT, pady=10, padx=20, ipadx=18, ipady=10)
        self.button11.pack(side=tkinter.LEFT, pady=10, padx=(45, 0), ipadx=18, ipady=10)
        self.button12.pack(side=tkinter.LEFT, pady=10, padx=(20, 0), ipadx=18, ipady=10)
        self.button_clear.pack(side=tkinter.LEFT, pady=10, padx=(80, 0), ipadx=18, ipady=10)

    def draw(self, event) -> None:
        x, y = self.mouse_pos
        if x is not None and y is not None:
            self.canvas.create_line(x, y, event.x, event.y, width=self.draw_width, fill=self.draw_col)
        self.mouse_pos = (event.x, event.y)

    def red(self):
        self.draw_col = "red"

    def orange(self):
        self.draw_col = "orange"

    def yellow(self):
        self.draw_col = "yellow"

    def lime(self):
        self.draw_col = "lime"

    def green(self):
        self.draw_col = "green"

    def dark_blue(self):
        self.draw_col = "dark blue"

    def light_blue(self):
        self.draw_col = "light blue"

    def pink(self):
        self.draw_col = "pink"

    def purple(self):
        self.draw_col = "purple"

    def brown(self):
        self.draw_col = "#964B00"

    def grey(self):
        self.draw_col = "grey"

    def black(self):
        self.draw_col = "black"

    def white(self):
        self.draw_col = "#fff"

    def clear_canvas(self):
        self.canvas.delete("all")

    def changee(self):
        self.draw_width = self.user_inputtt.get()

    def reset_pos(self, event) -> None:
        self.mouse_pos = (None, None)
        print(self.mouse_pos)

if __name__ == "__main__":
    app = DrawPadApp()
    app.run()

