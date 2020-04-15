import numpy as np

class Board:
    def __init__(self, size=4):
        self.size = size
        self.config = np.full((size, size), 'o', dtype=object)
        self.conflicts = np.zeros((size, size), 'int')

    def find_conflicts(self):
        for i in range(self.size):
            for j in range(self.size):
                self.conflicts[i][j] = self.calc_attack(i, j)

    def goal_test(self):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.config[i][j] == 'x':
                    score += self.conflicts[i][j]

        if score: return True
        return False

    def calc_attack(self, i, j):
        attacks = 0

        # Horizontal attack from left
        cols = j
        while cols > 0:
            cols -= 1
            if self.config[i][cols] == 'x':
                attacks += 1

        # Horizontal attack from right
        cols = j
        while cols < self.size-1:
            cols += 1
            if self.config[i][cols] == 'x':
                attacks += 1

        # Diagonal upward left
        rows = i
        cols = j
        while rows > 0 and cols > 0:
            rows -= 1
            cols -= 1
            if self.config[rows][cols] == 'x':
                attacks += 1

        # Diagonal downward right
        rows = i
        cols = j
        while rows < self.size-1 and cols < self.size-1:
            rows += 1
            cols += 1
            if self.config[rows][cols] == 'x':
                attacks += 1

        # Diagonal downward left
        rows = i
        cols = j
        while rows < self.size - 1 and cols > 0:
            rows += 1
            cols -= 1
            if self.config[rows][cols] == 'x':
                attacks += 1

        # Diagonal upward right
        rows = i
        cols = j
        while rows > 0 and cols < self.size-1:
            rows -= 1
            cols += 1
            if self.config[rows][cols] == 'x':
                attacks += 1

        return attacks


class SearchSolution:
    def __init__(self, max_steps):
        self.board = SearchSolution.take_input_config()
        self.max_steps = max_steps
        self.board.find_conflicts()

    def initialize_game(self):
        step = 0
        while step < self.max_steps:
            if self.board.goal_test():
                pass
            else:
                #pick a random queen and move it to min conflict place and recalculate
                # Repeat until max steps or goal true, whichever comes first
                #print solution
                pass


    @staticmethod
    def take_input_config():
        while True:
            try:
                size = int(input("Please enter the board size"))
                break
            except ValueError:
                print("Entered value is not a valid integer")
                continue

        board = Board(size)

        for i in range(size):
            while True:
                try:
                    j = int(input(f"Please enter the row number for queen in column {i+1}"))
                    board.config[i][j] = 'x'
                    break
                except ValueError:
                    print(f"Entered value is not a valid index, row number ranges from 0 to {size}")
                    continue

        return board