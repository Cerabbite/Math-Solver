from libaries import *


class solver:
    def __init__(self):
        pass

    def equation_components(self, equation):
        components = {"Letters": [], "Numbers": [], "Special chars": []}
        for i in equation:
            if i.isdigit():
                components['Numbers'].append(int(i))
            elif i.isalnum():
                components['Letters'].append(str(i))
            else:
                components['Special chars'].append(str(i))
        return components


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")
        self.letters = []
        self.letters_btns = []
        Solver = solver()
        self.eq_comps = Solver.equation_components(default_values.default_equation())
        self.create_btn()

        self.equation_lbl = Label(self.window, text="Equation")
        self.equation_lbl.grid(row=0,column=0)

        self.inp_box_width = 25#len(default_values.default_equation())
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.grid(row=0, column=1, columnspan=2)
        self.inp_box.insert('end', default_values.default_equation())

        self.solve_for_lbl = Label(self.window, text="Solve for")
        self.solve_for_lbl.grid(row=1,column=0)

        self.solve_btn_width = 20
        self.solve_btn = Button(self.window, width=self.solve_btn_width, text="Solve", command=self.solve_eq_data)
        self.solve_btn.grid(row=2, column=0, columnspan=3)
        #self.inp_box.insert('end', default_values.default_equation())

        #self.bindings()

    def bindings(self):
        #window.bind("<Key>", lambda x : self.update(x))
        pass

    def create_btn(self):
        print(self.eq_comps['Letters'])
        for i in self.eq_comps['Letters']:
            if not i in self.letters:
                self.letters.append(i)
                btn = Button(self.window, width=5, text=i)
                btn.grid(row=1, column=1)
                self.letters_btns.append(btn)
                print(btn)

    def on_off(self):
        pass


    def solve_eq_data(self):
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
