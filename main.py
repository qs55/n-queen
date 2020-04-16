import numpy as np
import random
import sys

class Board:
    def __init__(self, size=4):
        self.size = size
        self.config = np.full((size, size), 'o', dtype=object)
        self.conflicts = np.zeros((size, size), 'int')

    def find_conflicts(self):
        for i in range(self.size):
            for j in range(self.size):
                self.conflicts[i][j] = self.calc_attack(i, j)

    def conflicted_index(self):
        index = []
        for i in range(self.size):
            for j in range(self.size):
                if self.config[i][j] == 'x':
                    if self.conflicts[i][j] > 0:
                        index.append((i,j))
        return index

    def goal_test(self):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.config[i][j] == 'x':
                    score += self.conflicts[i][j]

        if score: return False
        return True

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

        # print(f"Attack on {i,j} = {attacks}")
        return attacks

    def print_config(self, flag):
        if flag:
            print("Final Config of the board:")
            print()
            for i in range(self.size):
                print("| ", end="")
                for j in range(self.size):
                    print(self.config[i][j], end=" | ")
                print()
        else:
            print("Solution could not be found in defined Maximum number of steps")

    def find_min_column(self, row, col):
        min = sys.maxsize
        min_index = row
        for i in range(self.size):
            if i == row:
                continue
            else:
                if self.conflicts[i][col] < min:
                    min = self.conflicts[i][col]
                    min_index = i
        return min_index






class SearchSolution:
    def __init__(self, max_steps):
        self.board = SearchSolution.take_input_config()
        # self.board.print_config(True)
        self.max_steps = max_steps
        self.board.find_conflicts()

    def initialize_game(self):
        step = 0
        while step < self.max_steps:
            if self.board.goal_test():
                # print("test success")
                self.board.print_config(True)
                return
            else:
                conflicted = self.board.conflicted_index()
                row,col  = random.choice(conflicted)
                new_row = self.board.find_min_column(row, col)
                self.board.config[row][col] = 'o'
                self.board.config[new_row][col] = 'x'

                self.board.find_conflicts()
                #pick a random queen and move it to min conflict place and recalculate
                # Repeat until max steps or goal true, whichever comes first
                #print solution
                pass
            step += 1
        else:
            self.board.print_config(False)

    @staticmethod
    def take_input_config():
        while True:
            try:
                size = int(input("Please enter the board size : "))
                if size > 0:
                    break
                else:
                    print("Entered invalid size value")
                    continue
            except ValueError:
                print("Entered value is not a valid integer. Please enter again. ")
                continue

        board = Board(size)

        for j in range(size):
            while True:
                try:
                    i = int(input(f"Please enter the row number for queen in column {j} : "))
                    if i < size:
                        board.config[i][j] = 'x'
                        break
                    else:
                        print("Entered Index value is incorrect")
                        continue
                except ValueError:
                    print(f"Entered value is not a valid index, row number ranges from 0 to {size-1} : ")
                    continue

        return board

class Main:
    ss = SearchSolution(500)
    ss.initialize_game()