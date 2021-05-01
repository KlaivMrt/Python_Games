import time
start = time.time()

class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''
        self.score = int()

    def get_info(self, player):
        self.name = input(player + ", please type your name >> ").capitalize()
        # self.symbol = input(f'Hello {self.name}! \n Please type your symbol >> ').upper()


class Board:
    def __init__(self):
        self.grid = []
        self.reset_grid()

    def show_grid(self):
        for i in range(len(self.grid)):
            for element in self.grid[i]:
                print('- ' if element == None else element + ' ', end = '')
            print()


    def reset_grid(self):
        self.grid = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]


class Console_G:
    def __init__(self):
        self.b = Board()

    def game_on(self):
        repeat = True
        while repeat:
            for i in range(len(self.b.grid)):
                for j in self.b.grid[i]:
                    if j is None:
                        return True
                    else:
                        repeat = False
        return False

    def check(self):
        for i in range(3):
            if self.b.grid[i][0] is not None and self.b.grid[i][0] == self.b.grid[i][1] == self.b.grid[i][2]:
                return self.b.grid[i][0]
            if self.b.grid[0][i] is not None and self.b.grid[0][i] == self.b.grid[1][i] == self.b.grid[2][i]:
                return self.b.grid[0][i]
        if self.b.grid[0][0] is not None and self.b.grid[0][0] == self.b.grid[1][1] == self.b.grid[2][2]:
            return self.b.grid[0][0]
        if self.b.grid[0][2] is not None and self.b.grid[0][2] == self.b.grid[1][1] == self.b.grid[2][0]:
            return self.b.grid[0][2]
        return None



    def get_value(self):
        repeat = True
        while repeat:
            try:
                number = int(input('>> >> >> '))
                if number in range(1, 4):
                    repeat = False
                    return number

                else:
                        print('Value out of range. Try again!')
            except ValueError:
                print('You have typed an invalid input. Please try again!')

    def play(self, p1, p2):
        p1.symbol = 'X'
        p2.symbol = 'O'
        current_p = p1
        while self.game_on():
            print(f'It\'s {current_p.name}\'s turn.')
            retry = True
            self.b.show_grid()

            while retry:
                print('Choose your row.')
                r = self.get_value()
                print('Choose your column')
                c = self.get_value()

                if self.b.grid[r - 1][c - 1] == None:
                    self.b.grid[r - 1][c - 1] = current_p.symbol
                    retry = False
                    if current_p == p2:
                        current_p = p1
                    else:
                        current_p = p2

                elif self.b.grid[r - 1][c - 1] != None:
                    print("You can't place you're symbol here. Please try again!")

            if self.check() == p1.symbol:
                print(f'{p1.name} is the winner!')
                p1.score += 1
                break
            elif self.check() == p2.symbol:
                print(f'{p2.name} is the winner!')
                p2.score += 1
                break

        else:
            self.b.show_grid()
            print('Its a tie!')


if __name__ == '__main__':

    with open('message.txt', 'r') as m:
        print(m.read())


    p1 = Player()
    p2 = Player()

    p1.get_info('Player 1')
    p2.get_info('Player 2')
    while True:

        board = Board()
        play = Console_G()

        # play.game_on()
        play.play(p1, p2)
        print  (f'|         SCORE:         '
                f'\n|------------------------'
                f'\n|{p1.name}: {p1.score}   '
                f'\n|------------------------'
                f'\n|{p2.name}: {p2.score}   ')
        replay = input('Play again? (y/n) >>> ')
        if replay == 'y':
            board.reset_grid()
        else:
            print('Thanks for playing!')
            break
    print(time.time() - start)