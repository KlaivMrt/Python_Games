from view import StartPanel, InfoBox, GridView, Replay
from model import Model




class Controller:
    def __init__(self, root, top):
        self.root = root
        self.model = Model(self)  # You pass this parameter so the model can 'see' the controller
        self.grid_v = GridView(self, top)
        self.info_b = InfoBox(self, root)

    def give_names_model(self, name):  # Passes the names to the Model Taken from the info box
        self.model.save_names(name)

    def give_names_board(self):
        # This function delivers the names, taken from the model to the score board of the InfoBox
        p1, p2 = self.model.return_p_names()
        return p1, p2

    def give_scores_board(self):
        s1, s2 = self.model.return_p_scores()
        return s1, s2

    def activate_board(self):
        # This function activates the board by calling the .activate_btns method of the GridView class
        # Also sets the first player for placing his/her symbol
        self.grid_v.activate_btns()
        self.model.set_p1_1st()

    def set_symbol(self, i, j):
        # Calls the .set_symbol method from the model and returns its results
        return self.model.set_symbol(i, j)

    def play(self):
        # This function calls the .play method from th model
        self.model.play()
        self.info_b.set_board()


    def replay_win(self):
        self.win = Replay(self)
        # self.win.no.config(command = self.root.destroy)
        # self.win.yes.config(command =
        #         lambda : [self.activate_board(), self.win.root.destroy()])

    def reset_game(self):
        # This method calls .reset_btns() and .reset_grid() methods to reset both the grids in
        # the Model and GridView classes.
        # It is also responsible for the pop-up window of the replay function
        self.grid_v.reset_btns()
        self.model.reset_grid()
        self.replay_win()













