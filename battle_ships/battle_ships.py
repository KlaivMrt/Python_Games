class Cell:
    def __init__(self):
        self.free = True  # this attribute indicates i the sell is occupied or not from a ship
        self.hit = None  # this one indicates if the ship is hit or not
        self.sh_symbol = str()  # this shows the ship's symbol to let the user know where he has placesd it on the board


class Boards:
    def __init__(self):
        self.grid = []

    def get_grid(self):
        for i in range(10):  # The grid has 10 rows
            line = []  # creating a new line for each row
            for j in range(10):  # and 10 columns
                cell = Cell()  # creating a new instance for each position of the grid
                line.append(cell)  # The line is filled with each new cell generated
            self.grid.append(line)  # the grid is filled with each new line generated
        return self.grid

    def display(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(' - ' if self.grid[i][j].free else self.grid[i][j].sh_symbol, end='')
            print()

    def reset_grid(self):
        self.grid = []

class Ships:
    def __init__(self):
        self.ships = {
            'Carrier': [' C ', 5],
            'Battleship': [' B ', 4],
            'Destroyer': [' D ', 3],
            'Submarine': [' S ', 3],
            'Patrol': [' P ', 2]
        }


class Players:
    def __init__(self):
        self.name = str()
        self.score = 0
        self.board = Boards()
        self.ships = Ships()
        self.deployed = []

    def reset_deployed(self):
        self.deployed = []

    def get_name(self, p):
        self.name = input(f'Please, type your name.\n'
                          f'{p}: ').capitalize()

    def choose_ship(self):
        global ship, row, column, ppp  # making these variables global the following loops will be able to evaluate them
        repeat = True
        while repeat:
            ship = input('Choose your ship: ').replace(' ', '').capitalize()
            if ship in self.ships.ships:
                repeat = False  # in case the ship inputted by the user is in the dictionary of ships, the loop won't be repeated.
            else:
                repeat = True  # else the loop will repeat until te user places a valid input

        row_ = True
        while row_:
            try:
                row = int(input('Choose row: '))
                if row in range(1, 11):
                    row_ = False  # if the user's input is within the range the loop won't repeat
                else:
                    row_ = True  # else it will repeat until it gets a valid input
            except ValueError:  # if the user inputs a string the loop will repeat due to the rise of a value error
                print('Type a valid number')

        column_ = True
        ccc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        while column_:
            column = input('Choose column: ').upper()
            if column in ccc:
                column_ = False  # if the user's input is in the list of answers the loop won't repeat.
            else:
                column_ = True

        position = True
        while position:
            positions = ['V', 'H']
            ppp = input('Choose position  V/H : ').upper()
            if ppp in positions:
                position = False  # if the position is in the list of valid answers the loop won't repeat
            else:
                position = True

        return ship, row -1, ord(column) -65, ppp  # the function returns 4 values simultaneously.

    def place(self, r, c, s, p, b):  # this function places the symbol of the ship in the coordinates required.
        ship_s = self.ships.ships[s][1]
        if p == 'V':
            for i in range(r, r + ship_s):
                if b[i][c].free:
                    b[i][c].free = False
                    b[i][c].sh_symbol = self.ships.ships[s][0]
        if p == 'H':
            for i in range(c, c + ship_s):
                if b[r][i].free:
                    b[r][i].free = False
                    b[r][i].sh_symbol = self.ships.ships[s][0]

    def reset_ships(self, s, b):  # this function resets the cells of the grid: both there symbols and .free status
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j].sh_symbol == self.ships.ships[s][0]:
                    b[i][j].free = True
                    b[i][j].sh_symbol = ''

    def can_place_s(self, s, r, c, p, b):  # this function counts the occupied cells and returns the count
        ship_s = self.ships.ships[s][1]
        occ = 0
        if p == 'V':
            for i in range(r + 1, r + ship_s):
                if b[i - 1][c].free is False:
                    occ += 1

        if p == 'H':
            for i in range(c + 1, c + ship_s):
                if b[r][i - 1].free is False:
                    occ += 1
        return occ

    def place_ships(self, p, b):  # this function places together all the above mentioned
        for i in range(5):
            repeat = True
            # TODO: Make an update so the ships do not touch each other.

            while repeat:  #
                ship, row, col, posit = self.choose_ship()  # these variables will be used as the coordinates and parameters of the rest functions
                if ship in self.deployed: # if the ship has been already deployed on the grid a message pops up and the user is asked to place another one.
                    print(f'You have already deployed the {ship}.')
                    self.board.display()
                else:
                    try:
                        occupied_c = self.can_place_s(ship, row, col, posit, b)
                        if occupied_c == 0:  # if the number of occupied cells is 0 the ship can be deployed
                            self.place(row, col, ship, posit, b)

                            repeat = False
                            self.deployed.append(ship)

                            position = 'Vertical' if posit == 'V' else 'Horizontal'
                            print(f'{p.name} has placed {ship} in position: {row}, {column}, {position}')
                            self.board.display()

                        else:
                            print('The position you\'ve chosen for your ship contains another.'
                                  '\nPlease, try again.')

                    except IndexError:  # if the ship is placed beyond the boarders
                        self.reset_ships(ship, b)  # the board is freed and cleared from the ship's symbol
                        print("You can't place your ship out of the borders.\n"
                              "Please, try again.")


class ConsoleGame:
    def choose_r(self):  # this function returns the number of column required by the user
        repeat = True
        while repeat:
            try:
                shooting_r = int(input('Choose row:  '))
                if shooting_r in range(1, 11):
                    repeat = False
                    return shooting_r - 1
                else:
                    print('Row out of range.\n'
                          'Please, try again.')
            except ValueError:
                print("Row out of range"
                      "\nPlease, try again.")

    def choose_col(self):  # this function return the appropriate index of column required by the user
        repeat = True
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        while repeat:
            col = input('Choose your column:  ').capitalize()
            if col in columns:
                repeat = False
                return ord(col) -65
            else:
                print('Column out of range.\n'
                      'Please, try again.')

    def oponents_grid(self, b):
        for i in range(len(b)):
            for j in range(len(b[i])):
                print(' - ' if b[i][j].hit is None else b[i][j].hit, end='')  # shows the opponent's grid based on the hit attribute of each cell
            print()

    def win(self, b): # this function checks the number of cells occupied by a ship and the number of these cells that has been hit
        counter = 0  # hit cells
        ship = 0  # cells occupied by a ship
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j].free == False:
                    ship += 1
                if b[i][j].free == False and b[i][j].hit != None:  # each of these cells that has been hit is being tracked
                    counter += 1
        if ship == counter:
            return True

    def shoot(self, p, board):
        # repeat = True
        # while repeat:
        print()
        print()
        print(f'{p.name}, commence shooting!')
        self.oponents_grid(board)
        print()

        repeat = True
        while repeat:
            row = self.choose_r()
            col = self.choose_col()
            print()

            if board[row][col].hit != None:  # if the person shoots in the same place a message is displayed and the coordinates are required again
                print('You have already shot in this position.\n'
                      'Please, try again.')
            elif board[row][col].sh_symbol == '' and board[row][col].hit == None:  # if the player hits the see a W for white is displayed on the given coordinates on the board
                board[row][col].hit = ' W '
                repeat = False
            elif board[row][col].sh_symbol != '' and board[row][col].hit == None:  # if a ship is hit a R for red is displayed on the given coordinates on the board
                board[row][col].hit = ' R '
                repeat = False

        self.oponents_grid(board)
        print()
        print()
        print()
        print()






if __name__ == "__main__":
    with open('welcome.txt', 'r') as w:
        print(w.read())

    p1 = Players()  # Declaring two variables Players
    p2 = Players()

    p1.get_name("Player 1")  # Asking for p1 name
    p2.get_name("Player 2")  # Asking for p2 name

    while True:
        board1 = p1.board  # Declaring a variable for p1 board
        b1 = board1.get_grid()  # Creating a board for p1
        board1.display()  # Displaying p1's board
        print()
        print()
        print(f'{p1.name}, place your ships!')
        p1.place_ships(p1, b1)  # Allowing p1 to place the ships
        print()
        print()


        board2 = p2.board
        b2 = board2.get_grid()
        board2.display()
        print()
        print()
        print(f'{p2.name}, place your ships!')
        p2.place_ships(p2, b2)
        print()
        print()

        play = ConsoleGame()

        repeat = True
        while repeat:  # players take turns in shooting up until someones ships are completely destroyed
            play.shoot(p1, b2)

            if play.win(b2):  #
                print(f'{p1.name} won the game!!')
                p1.score += 1
                repeat = False

            play.shoot(p2, b1)
            if play.win(b1):
                print(f'{p2.name} won the game!!')
                p2.score += 1
                repeat = False

        print(f'|         SCORE:         '
              f'\n|------------------------'
              f'\n|{p1.name}: {p1.score}   '
              f'\n|------------------------'
              f'\n|{p2.name}: {p2.score}   ')

        board1.reset_grid()  # grids are reset
        p1.reset_deployed()  # list of deployed ships are reset

        board2.reset_grid()
        p2.reset_deployed()

        re_play = input('Do you wish to re-play? (Y/N) >> ').upper()
        if re_play == 'Y':
            pass
        else:
            break
