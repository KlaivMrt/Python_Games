import tkinter as tk

# This is the first panel displayed with the rules of the game!


def disabled(widget):  # this function disables the widget passed as a parameter
    widget.config(state='disabled')



class StartPanel:
    def __init__(self, root):
        self.label = tk.Label(root)
        self.label.pack()

        self.start = tk.Button(root, text='START')
        self.start.config(command=lambda x = root: self.start_game(x))
        self.start.pack()

        self.get_rules()


    def get_rules(self):
        with open('rules.txt', 'r') as r:
            read = r.read()
            self.label.config(text=read)

    def start_game(self, root):
        root.destroy()

# This is the board of the game!

class GridView:
    def __init__(self, controller, root):
        self.controller = controller

        self.btn1 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn1, 0, 0))
        self.btn2 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn2, 0, 1))
        self.btn3 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn3, 0, 2))
        self.btn4 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn4, 1, 0))
        self.btn5 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn5, 1, 1))
        self.btn6 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn6, 1, 2))
        self.btn7 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn7, 2, 0))
        self.btn8 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn8, 2, 1))
        self.btn9 = tk.Button(root, text='', padx=40, pady=35, state='disabled', command= lambda : self.clicked(self.btn9, 2, 2))

        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=1, column=0)
        self.btn5.grid(row=1, column=1)
        self.btn6.grid(row=1, column=2)
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)

        self.btns = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5,
                      self.btn6, self.btn7, self.btn8, self.btn9]

    def activate_btns(self):
        for btn in self.btns:
            btn.config(text='', state='active')

    def clicked(self, btn, i, j):
        # This function is responsible for displaying each players symbol.
        btn.config(text=self.controller.set_symbol(i, j),state='disabled')
        self.controller.play()

    def rewrite(self, btns):  # Returns all the btns in the board in their initial state
        for btn in btns:
            btn.config(text='', state='disabled')

    def reset_btns(self):
        # This function resets all btns.
        for btn in self.btns:
            btn.config(text='', state='disabled')


# This is the window that gets the names of the players!

class InfoBox:
    def __init__(self, controller, root):

        self.controller = controller

        self.entry = tk.Entry(root)
        self.entry.focus()
        self.entry.pack(side = 'top',fill='x')

        self.submit_btn = tk.Button(root, text='SUBMIT',
                            command= lambda :[self.get_names(), self.set_board()])

        self.submit_btn.pack()

        self.label = tk.Label(root)
        self.label.pack(side='top', fill='x')


        self.string = tk.StringVar()
        self.string.set('''
SCORE:
---------------------------------------------
              : 
---------------------------------------------
              : 
                                ''')
        self.score_label = tk.Label(root, textvariable=self.string)
        self.score_label.pack()

        self.start_btn = tk.Button(root, text='LET\'S PLAY', state='disabled',
                                    command=self.commence_game)
        self.start_btn.pack()

        self.counter = 0

    def set_board(self):
        p1, p2 = self.controller.give_names_board()
        s1, s2 = self.controller.give_scores_board()
        self.string.set(f'''
SCORE:
----------------------------------------------------
{p1:<10} : {s1:>15}
----------------------------------------------------
{p2:<10} : {s2:>15}
                        ''')


    def get_names(self):
        # This function is going to be configured as the submit_btn command
        # It gets the names and sets the submit_btn disabled.

        name = self.entry.get()
        self.controller.give_names_model(name)
        self.entry.delete(0, 'end')
        self.counter += 1
        print(name)

        if self.counter == 2:
            self.submit_btn.config(state='disabled')
            self.entry.config(state='disabled')
            self.start_btn.config(state='active')

    def commence_game(self):
        self.start_btn.config(state='disabled')
        self.controller.activate_board()
        # self.controller

# This is the pop-up window that asks for a replay!

class Replay:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Toplevel()
        self.root.title('Nice!!!')
        self.root.geometry('250x100')

        self.l = tk.Label(self.root, text='Play again ?')
        self.l.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=15)
        self.yes = tk.Button(self.frame, text='Yes', width=15,
                             command= lambda :[self.controller.activate_board(), self.root.destroy()])
        self.yes.pack(side='left', padx=10)

        self.no = tk.Button(self.frame, text='No', width=15, command=self.controller.root.destroy)
        self.no.pack(side='right', padx=10)




