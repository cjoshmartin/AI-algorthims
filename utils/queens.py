import random


def queen_placement(size):
    return random.randint(0, size - 1)


def n_sized_board(size):
    board = []
    for n in range(size):
        board.append(queen_placement(size))

    return board


def is_attacking(r1, c1, r2, c2):
    if r1 == r2:
        return True
    if c1 == c2:
        return True

    diagonal = (c2 - c1) / (r2 - r1)

    if abs(diagonal) == 1:
        return True