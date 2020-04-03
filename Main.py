
def _generate_blank_board():
    _board = [[" " for x in range(11)] for y in range(11)]
    _verticalMarker = "|"
    _horizontalMarker = "-"

    for index, row in enumerate(_board):
        if index <= 2 or (index  >= 4 and index <= 6) or index >= 8:
            row[3] = _verticalMarker
            row[7] = _verticalMarker
        elif index == 3 or index == 7:
            for index in range(len(row)):
                row[index] = _horizontalMarker

    return _board


def _print_board(board):
    _row_strings = []

    for row in board:
        _row_strings.append("".join(row))
    
    for row in _row_strings:
        print(row)


def draw_board():
    _blank_board = _generate_blank_board()
    _print_board(_blank_board)


def user_input():
    


if __name__ == "__main__":
    draw_board()


