from libaries import *


class solver:
    def __init__(self):
        pass


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")

        self.inp_box_width = 11
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.pack()
        self.inp_box.insert('end', default_values.default_equation())

        self.bindings()

    def bindings(self):
        window.bind("<Key>", lambda x : self.update(x))


    def update(self, x):
        #value = self.inp_box.get("1.0", END)
        #print(value)
        print('x')

if __name__ == "__main__":
    window = Tk()
    f_main = main(window)
    #window.bind("<Up>", f_main.update())
    window.mainloop()
