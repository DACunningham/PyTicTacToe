import sys

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


def user_input_turn(player_name):
    _location = int(input(f"{player_name} what square number do you want? "))
    return _location


def _location_number_to_indexes(num, board, symbol):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine
    }

    func = switcher.get(num, lambda: "ERROR: Invalid location selected.")
    return func(board, symbol)


def one(board, symbol):
    return _update_board(9, 1, board, symbol)
 
def two(board, symbol):
    return _update_board(9, 5, board, symbol)
 
def three(board, symbol):
    return _update_board(9, 9, board, symbol)
 
def four(board, symbol):
    return _update_board(5, 1, board, symbol)
 
def five(board, symbol):
    return _update_board(5, 5, board, symbol)
 
def six(board, symbol):
    return _update_board(5, 9, board, symbol)
 
def seven(board, symbol):
    return _update_board(1, 1, board, symbol)
 
def eight(board, symbol):
    return _update_board(1, 5, board, symbol)
 
def nine(board, symbol):
    return _update_board(1, 9, board, symbol)


def _update_board(row_index, col_index, board, symbol):
    board[row_index][col_index] = symbol
    return board


def _player_turn(board, player):
    _user_turn = user_input_turn(player["name"])
    return _location_number_to_indexes(_user_turn, board, player["token"])


def _calculate_winner():
    pass


def _set_player_token(player_obj, token):
    player_obj["token"] = token
    return player_obj

if __name__ == "__main__":
    _board = _generate_blank_board()
    _player_one = {
        "name": "Player 1",
        "token": "X"
    }
    _player_two = {
        "name": "Player 2",
        "token": "O"
    }
    _game_over = False
    _is_player_one_turn = True

    _player_1_token = input("Does Player 1 want to be 'X' or 'O'? ")
    if _player_1_token.lower() == "x":
        _player_one = _set_player_token(_player_one, _player_1_token.upper())
        _player_two = _set_player_token(_player_two, "O")
    elif _player_1_token.lower() == "o":
        _player_one = _set_player_token(_player_one, _player_1_token.upper())
        _player_two = _set_player_token(_player_two, "X")
    else:
        print("ERROR: You did not select 'X' or 'O'. Application will now exit...")
        sys.exit(1)

    while not _game_over:
        _print_board(_board)
        if _is_player_one_turn:
            _board = _player_turn(_board, _player_one)
        else:
            _board = _player_turn(_board, _player_two)

        _is_player_one_turn = not _is_player_one_turn
