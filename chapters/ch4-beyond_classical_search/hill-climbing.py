from utils.queens import n_sized_board, is_attacking


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
    size = 4
    board = n_sized_board(size)
    sort_over = 'h_cost'

    def format(cost, value):
        return {sort_over: cost, 'value': value}

    def sorter(item):
        return item[sort_over]

    cur_h = h(board)

    while cur_h > 0:
        for i in range(size):
            lowest_h = []
            board_copy = list(board)
            for j in range(size):
                board_copy[i] = j
                lowest_h.append(format(h(board_copy), j))

            lowest_h.sort(key=sorter)
            board[i] = lowest_h[0]['value']
        cur_h = h(board)

    print('board: {}, cost: {}'.format(board, h(board)))


main()
