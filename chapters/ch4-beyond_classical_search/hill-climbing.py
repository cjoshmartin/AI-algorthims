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
    size = 8
    board = n_sized_board(size)
    input_board = list(board)
    sort_over = 'h_cost'

    def format(cost, value):
        return {sort_over: cost, 'value': value}

    def sorter(item):
        return item[sort_over]

    should_not_quit = True
    counter = 0
    while should_not_quit :
        board_copy = list(board)
        for i in range(size):
            lowest_h = []

            for j in range(size):
                board_copy[i] = j
                lowest_h.append(format(h(board_copy), j))

            lowest_h.sort(key=sorter)
            board_copy[i] = lowest_h[0]['value']

        curr_h = h(board)
        new_h = h(board_copy)

        if counter > 50 or curr_h < new_h:
            print('Local minimum')
            should_not_quit = False
        elif curr_h < 1:
            should_not_quit = False
        elif new_h < 1:
            board = board_copy
            should_not_quit = False
        else:
            board = board_copy

        if curr_h == new_h:
            counter = counter + 1

    print('board: {}, cost: {}'.format(input_board, h(input_board)))
    print('board: {}, cost: {}'.format(board, h(board)))


main()
