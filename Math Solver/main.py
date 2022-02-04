from libaries import *


class solver:
    def __init__(self):
        pass

    def break_equation(self):
        pass


class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")

        self.equation_lbl = Label(self.window, text="Equation")
        self.equation_lbl.grid(row=0,column=0)

        self.inp_box_width = 25#len(default_values.default_equation())
        self.inp_box = Text(self.window, width=self.inp_box_width, height=1)
        self.inp_box.grid(row=0, column=1)
        self.inp_box.insert('end', default_values.default_equation())

        self.solve_for_lbl = Label(self.window, text="Solve for")
        self.solve_for_lbl.grid(row=1,column=0)

        self.solve_for_box_width = 25#len(default_values.default_equation())
        self.solve_for_box = Text(self.window, width=self.solve_for_box_width, height=1)
        self.solve_for_box.grid(row=1, column=1)

        self.solve_btn_width = 20
        self.solve_btn = Button(self.window, width=self.solve_btn_width, text="Solve", command=self.solve_eq_data)
        self.solve_btn.grid(row=2, column=0, columnspan=2)
        #self.inp_box.insert('end', default_values.default_equation())

        #self.bindings()

    def bindings(self):
        #window.bind("<enter>", lambda x : self.solve_eq_data(x))
        pass


    def solve_eq_data(self):
        self.solve_for = self.solve_for_box.get("1.0", END)
        print(self.solve_for)
        self.solve_for.replace(" ", "")
        if self.solve_for_box.compare("end-1c", "==", "1.0"):
            messagebox.showerror("Empty", "Please enter one character")
            return
        if len(self.solve_for_box.get("1.0", 'end-1c')) > 1:
            messagebox.showerror("To many characters", "Please enter just one character")
            return

        self.equation = self.inp_box.get("1.0", END)
        self.equation_copy
        print(self.equation)
        #messagebox.showerror("Character not found", "Please enter a character from the equation")

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
