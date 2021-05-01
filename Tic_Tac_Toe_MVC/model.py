
class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''
        self.score = 0

class Model:
    def __init__(self, control):
        self.controller = control
        self.grid = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.p1 = Player()
        self.p2 = Player()
        self.p1.symbol = 'X'
        self.p2.symbol = 'O'

        self.current_p = self.p1

    def reset_grid(self):
        self.grid = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def save_names(self, name):  # Saves the name taken from the InfoBox
        self.current_p.name = name
        print(self.current_p.name)
        if self.current_p == self.p1:
            self.current_p = self.p2


    def return_p_names(self):  # returns players's names
        return self.p1.name, self.p2.name

    def return_p_scores(self):
        return self.p1.score, self.p2.score

    def set_p1_1st(self):  # Sets as current_p = p1
        self.current_p = self.p1

    def set_symbol(self, i, j):
        # Function sets the symbol of the current player playing to the grid according to the coordinates
        # given by the button clicked
        # In the end it returns the symbol so the btn can display it.
        self.grid[i][j] = self.current_p.symbol
        for i in range(3):
            for j in range(3):
                print('-' if self.grid[i][j] == '' else self.grid[i][j], end='')
            print()

        if self.current_p == self.p1:
            self.current_p = self.p2
            return self.p1.symbol
        else:
            self.current_p = self.p1
            return self.p2.symbol

    def check(self):
        # Checks the grid to see who's the winner and returns his/hers symbol
        # Else it returns False in case the is a tie

        counter = 0
        for i in range(3):
            if self.grid[i][0] != '' and self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                return self.grid[i][0]
            if self.grid[0][i] != '' and self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return self.grid[0][i]
        for i in range(3):
            if self.grid[i][0] != '' and self.grid[i][1] != '' and self.grid[i][2] != '':
                counter += 1

        if self.grid[0][0] != '' and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return self.grid[0][0]
        if self.grid[0][2] != '' and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return self.grid[0][2]
        if counter == 3:
            return False

    def play(self):
        # This function is responsible for
        # checking the winner and setting the score
        if self.check() == self.p1.symbol:
            print(f'{self.p1.name} is the winner!')
            self.p1.score += 1
            self.controller.reset_game()  # Resets everything
        elif self.check() == self.p2.symbol:
            print(f'{self.p2.name} is the winner!')
            self.p2.score += 1
            self.controller.reset_game()
        elif self.check() == False:
            print('It\'s a tie!')
            self.controller.reset_game()

























