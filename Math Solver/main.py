from libaries import *


class solver:
    def __init__(self):
        self.letters = []
        self.letters_btns = []

    def equation_components(self, equation, window):
        components = {"Letters": [], "Numbers": [], "Special chars": []}
        for i in equation:
            if i.isdigit():
                components['Numbers'].append(int(i))
            elif i.isalnum():
                components['Letters'].append(str(i))
            else:
                components['Special chars'].append(str(i))
        print("Extracting success")
        for i in self.letters_btns:
            i.grid_remove()
        self.letters = []
        self.letters_btns = []
        print(components['Letters'])
        for i in components['Letters']:
            if not i in self.letters:
                self.letters.append(i)
                btn = Button(window, width=3, text=i)
                btn.grid(row=1, column=len(self.letters))
                self.letters_btns.append(btn)
        return components


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")
        self.Solver = solver()
        self.eq_comps = self.Solver.equation_components(default_values.default_equation(), self.window)
        #self.create_btn(self.letters_btns)

        self.equation_lbl = Label(self.window, text="Equation")
        self.equation_lbl.grid(row=0,column=0)

        self.inp_box_width = 25#len(default_values.default_equation())
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.grid(row=0, column=1, columnspan=100)
        self.inp_box.insert('end', default_values.default_equation())

        self.solve_for_lbl = Label(self.window, text="Solve for")
        self.solve_for_lbl.grid(row=1,column=0)

        self.solution_lbl = Label(self.window, text="Solution")
        self.solution_lbl.grid(row=2,column=0)

        self.solve_btn_width = 20
        self.solve_btn = Button(self.window, width=self.solve_btn_width, text="Solve", command=self.solve_eq_data)
        self.solve_btn.grid(row=3, column=0, columnspan=101)
        #self.inp_box.insert('end', default_values.default_equation())

        self.bindings()

    def bindings(self):
        self.eq_comps = self.window.bind("<Key>", lambda x : self.Solver.equation_components(self.inp_box.get("1.0", END), self.window))


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
