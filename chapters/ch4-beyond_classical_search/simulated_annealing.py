import sys

import random
from math import exp

from utils.queens import h, n_sized_board


def guess():
    return random.random()
def signmoid(delta_E, t):
    if t == 0:
        return 1

    e_to_x = 1 + exp(-delta_E / t)

    return 1/e_to_x

def check_eutropy(c, n, t):
    delta_E = h(n) - h(c) # if delta_E, N is a good solution
    if delta_E > 0:
        return n
    else: # lets force it to work
        if signmoid(delta_E, t) * guess() < .5:
            return n

    return c


def sum_a(board,size):

    for t in range(sys.maxsize):
        board_temp =  list(board)
        for i in range(size):
            board_temp[i] = board[i]
            for j in range(size):
                board_temp[j] = i
                if guess() > .5:
                    board = check_eutropy(board, board_temp, t)

        print(h(board))

    print('board: {}, cost: {}'.format(board, h(board)))

size = 4
sum_a(n_sized_board(size),size)