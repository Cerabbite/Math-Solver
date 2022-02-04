from libaries import *


class solver:
    def __init__(self):
        self.letters = []
        self.letters_btns = []
        self.stored = None

    def create_buttons(self, window, components):
        stored = None
        for i in self.letters_btns:
            i[0].grid_remove()

        self.letters = []
        self.letters_btns = []
        #print(components['Letters'])
        index = 0
        for i in components['Letters']:
            #print(len(self.letters))
            if not i[0] in self.letters and len(self.letters) <= 2:
                self.letters.append(i[0])
                if self.stored == i[0]:
                    btn = Button(window, width=3, text=i[0], command=lambda button=index: self.select_solve_for(button), bg='lightblue')
                    btn.grid(row=1, column=len(self.letters))
                    self.letters_btns.append([btn, 'selected'])
                else:
                    btn = Button(window, width=3, text=i[0], command=lambda button=index: self.select_solve_for(button))
                    btn.grid(row=1, column=len(self.letters))
                    self.letters_btns.append([btn, 'not-selected'])
                index += 1

    def equation_components(self, equation, window, create_btn=False):
        components = {"Letters": [], "Numbers": [], "Special chars": []}
        index = 0
        for i in equation:
            if i.isdigit():
                components['Numbers'].append([int(i), index])
            elif i.isalnum():
                components['Letters'].append([str(i), index])
            else:
                components['Special chars'].append([str(i), index])
            index += 1

        if create_btn:
            self.create_buttons(window, components)
        return components

    def select_solve_for(self, button):
        if self.letters_btns[button][1] == 'not-selected':
            self.letters_btns[button][0].configure(bg='lightblue')
            for i in range(len(self.letters_btns)):
                if not i == button:
                    self.letters_btns[i][0].configure(bg='#f0f0f0')
            self.letters_btns[button][1] = 'selected'
            self.stored = self.letters[button]
        elif self.letters_btns[button][1] == 'selected':
            self.letters_btns[button][0].configure(bg='#f0f0f0')
            self.letters_btns[button][1] = 'not-selected'
            self.stored = None

    def solve(self, equation, window):
        #3x-4x^2+1=1
        x, y, z = symbols('x y z')
        self.eq_comps = self.equation_components(equation, window)
        #self.sympy_eq = equation.replace('x', '*x')
        #self.sympy_eq = self.sympy_eq.replace('y', '*y')
        #self.sympy_eq = self.sympy_eq.replace('z', '*z')
        self.sympy_eq = equation.split('=')
        self.new_eq_p1 = None
        print(self.eq_comps)
        #print(self.sympy_eq)

        prev = None
        index = 0
        for current in self.sympy_eq[0]:
            if current.isalnum() and not current.isdigit() and prev.isdigit():
                self.new_eq_p1 += f'*{current}'
            elif not self.new_eq_p1:
                self.new_eq_p1 = current
            elif current == '^':
                #self.new_backup = self.new_eq_p1
                self.new_eq_p1 = self.new_eq_p1[:-1]
                num = 1
                vars = ""
                while True:
                    var = self.sympy_eq[0][index-num]
                    if var.isalnum():
                        vars += var
                    else:
                        break
                    num += 1
                    if num >= index:
                        break
                vars = vars[::-1]
                self.vars_new = None
                prev2 = None
                for i in vars:
                    if i.isalnum() and not i.isdigit() and prev2.isdigit():
                        self.vars_new += f'*{i}'
                    elif not self.vars_new:
                        self.vars_new = i
                    else:
                        self.vars_new += i
                    prev2 = i
                num -= 1
                self.new_eq_p1 = self.new_eq_p1[:-num]
                self.new_eq_p1 += f"Pow({self.vars_new}, "
            elif prev == "^":
                self.new_eq_p1 += f"{current})"
            else:
                self.new_eq_p1 += current
            prev = current
            index += 1

        print(self.new_eq_p1)

        self.new_eq_p2 = None

        prev = None
        for current in self.sympy_eq[1]:
            if current.isalnum() and not current.isdigit() and prev.isdigit():
                self.new_eq_p2 += f'*{current}'
            elif not self.new_eq_p2:
                self.new_eq_p2 = current
            else:
                self.new_eq_p2 += current
            prev = current

        print(self.new_eq_p2)
        print(Eq(self.new_eq_p1, self.new_eq_p2))



class main:
    def __init__(self, window):
        self.window = window
        self.window.title("Math solver")
        self.Solver = solver()
        self.eq_comps = self.Solver.equation_components(default_values.default_equation(), self.window, create_btn=True)
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
        self.solve_btn = Button(self.window, width=self.solve_btn_width, text="Solve", command=self.run_solver)
        self.solve_btn.grid(row=3, column=0, columnspan=101)
        #self.inp_box.insert('end', default_values.default_equation())

        self.bindings()

    def bindings(self):
        self.eq_comps = self.window.bind("<Key>", lambda x : self.Solver.equation_components(self.inp_box.get("1.0", END), self.window, create_btn=True))

    def run_solver(self):
        self.Solver.solve(self.inp_box.get("1.0", END), self.window)

    def on_off(self):
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
