from libaries import *


class solver:
    def __init__(self):
        pass


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")

        self.lbl = Label(self.window, text="Equation")
        self.lbl.grid(row=0,column=0)

        self.inp_box_width = 25#len(default_values.default_equation())
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.grid(row=0, column=1)
        self.inp_box.insert('end', default_values.default_equation())

        self.lbl2 = Label(self.window, text="Solve for")
        self.lbl2.grid(row=1,column=0)

        self.inp_box_width2 = 25#len(default_values.default_equation())
        self.inp_box2 = Text(self.window, width=self.inp_box_width2, height=1)
        self.inp_box2.grid(row=1, column=1)
        #self.inp_box.insert('end', default_values.default_equation())

        #self.bindings()

    def bindings(self):
        #window.bind("<Key>", lambda x : self.update(x))
        pass


    """def update(self, x):
        self.value = self.inp_box.get("1.0", END)
        self.lvalue = len(self.value)-1
        if self.lvalue < 12: self.lvalue = 12
        self.inp_box_width = self.lvalue
        self.inp_box.pack_forget()
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.pack()
        self.inp_box.insert('end', self.value)
        self.value = None"""

if __name__ == "__main__":
    window = Tk()
    f_main = main(window)
    #window.bind("<Up>", f_main.update())
    window.mainloop()
