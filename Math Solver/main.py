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


    def update(self):
        #value = self.inp_box.get("1.0", END)
        #print(value)
        print('x')

if __name__ == "__main__":
    window = Tk()
    main(window)
    window.bind("<Up>", main.update())
    window.mainloop()
