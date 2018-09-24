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


def h(board):

    size = len(board)
    attacking = 0

    for i in range(size):
        for j in range(size):
            if is_attacking(board[j], j, board[i], i):
                attacking = attacking + 1
    attacking = attacking - size  # remove self attacks
    attacking = attacking / 2  # counting for overlinks

    return attacking


def main():
    size = 8
    board = n_sized_board(size)
    while h(board) > 0:
        board = n_sized_board(size)

    print(board)

main()