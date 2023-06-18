import os
import random

clear = lambda: os.system('clear')
clear()

board_size = 8


def get_new_board():
    return [0] * (board_size * board_size)


def print_board(my_board):
    for i in range(0, board_size):
        for j in range(0, board_size):
            print(f"     {my_board[i * board_size + j]}", end='')
        print('\n')
    print('\n')


def get_affected_cells(x, y):
    cells = []
    for i in range(0, board_size):
        for j in range(0, board_size):
            if i == x or j == y or abs(i - x) == abs(j - y):
                cells.append(i * board_size + j)
    return cells


def set_queen(my_board, x, y):
    for i in range(0, board_size):
        for j in range(0, board_size):
            if i == x and j == y:
                my_board[i * board_size + j] = 'X'
            elif i == x or j == y:
                my_board[i * board_size + j] = 1
            elif abs(i - x) == abs(j - y):
                my_board[i * board_size + j] = 1


def is_valid_put(my_board, x, y):
    if my_board[x * board_size + y] != 0:
        return False

    affecting_cells = get_affected_cells(x, y)
    for cell in affecting_cells:
        if board[cell] == 'X':
            return False
    return True


bad_starting_points = []
tries = 0
for turn in range(11000):
    board = get_new_board()
    queens = 0
    clean_cells = [i for i in range(64)]
    dirty_cells = []
    starting_point = -1

    for _try in range(10000):
        tries += 1
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)

        if is_valid_put(board, row, col):
            set_queen(board, row, col)
            queens += 1
            if queens == board_size:
                break

    if queens == board_size:
        print(f"Eureka :) found in {tries} tries")
        print_board(board)
        break