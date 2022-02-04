from libaries import *


class solver:
    def __init__(self):
        pass


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")

        self.inp_box = Text(self.window, width=10)
        self.inp_box.pack()
        self.inp_box.insert('end', settings)

if __name__ == "__main__":
    window = Tk()
    main(window)
    window.mainloop()
