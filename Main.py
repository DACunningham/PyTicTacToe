import sys

loc_one = [9, 1]
loc_two = [9, 5]
loc_three = [9, 9]
loc_four = [5, 1]
loc_five = [5, 5]
loc_six = [5, 9]
loc_seven = [1, 1]
loc_eight = [1, 5]
loc_nine = [1, 9]
separator = "*"*10

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
    return _update_board(loc_one, board, symbol)
 
def two(board, symbol):
    return _update_board(loc_two, board, symbol)
 
def three(board, symbol):
    return _update_board(loc_three, board, symbol)
 
def four(board, symbol):
    return _update_board(loc_four, board, symbol)
 
def five(board, symbol):
    return _update_board(loc_five, board, symbol)
 
def six(board, symbol):
    return _update_board(loc_six, board, symbol)
 
def seven(board, symbol):
    return _update_board(loc_seven, board, symbol)
 
def eight(board, symbol):
    return _update_board(loc_eight, board, symbol)
 
def nine(board, symbol):
    return _update_board(loc_nine, board, symbol)


def _update_board(loc_number, board, symbol):
    board[loc_number[0]][loc_number[1]] = symbol
    return board


def user_input_turn(player_name):

    _is_valid_input = False
    while not _is_valid_input:
        try:
            _location = int(input(f"{player_name} what square number do you want? "))
            if _location < 10 and _location > 0:
                _is_valid_input = True
                return _location
            print(f"{separator} ERROR: You did not input a single digit from 1 - 9. Please enter 1 - 9. {separator}")
        except Exception as ex:
            print(f"{separator} ERROR: You did not input a single digit from 1 - 9. Please enter 1 - 9. {separator}")
            print(ex.__str__)
        
        


def _player_turn(board, player):
    _user_turn = user_input_turn(player["name"])
    return _location_number_to_indexes(_user_turn, board, player["token"])


def _set_player_token(player_one, player_two):
    
    _is_correct_token = False
    while not _is_correct_token:
        _player_1_token = input(f"{separator} Does Player 1 want to be 'X' or 'O'? ")
        if _player_1_token.lower() == "x":
            player_one["token"] =  _player_1_token.upper()
            player_two["token"] =  "O"
            _is_correct_token = True
        elif _player_1_token.lower() == "o":
            player_one["token"] =  _player_1_token.upper()
            player_two["token"] =  "X"
            _is_correct_token = True
        else:
            print(f"{separator} ERROR: You did not select 'X' or 'O'. Please select either 'X' or 'O'. {separator}")
    
    
def _check_line_win(board, positions):
    _symbols = []
    _symbols.append(_get_board_location_symbol(board, positions[0]))
    _symbols.append(_get_board_location_symbol(board, positions[1]))
    _symbols.append(_get_board_location_symbol(board, positions[2]))

    if " " in _symbols:
        return False
    else:
        return _symbols[0] == _symbols[1] == _symbols[2]


def _get_board_location_symbol(board, location):
    return board[location[0]][location[1]]
        

def _calculate_winner(board):

    _win_combinations = {
        "left_vert": [loc_one, loc_four, loc_seven],
        "centre_vert": [loc_two, loc_five, loc_eight],
        "right_vert": [loc_three, loc_six, loc_nine],
        "botton_horiz": [loc_one, loc_two, loc_three],
        "middle_horiz": [loc_four, loc_five, loc_six],
        "top_horiz": [loc_seven, loc_eight, loc_nine],
        "right_diag": [loc_one, loc_five, loc_nine],
        "left_diag": [loc_three, loc_five, loc_seven]
    }

    for key, combination in _win_combinations.items():
        if _check_line_win(board, combination):
            return True
        else:
            pass


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
    _turn_count = 0

    _set_player_token(_player_one, _player_two)

    while not _game_over and _turn_count <= 9:
        _print_board(_board)

        if _turn_count == 9:
            print(f"{separator} It's a draw! {separator}")
            print(f"{separator} Application will now exit. {separator}")
            sys.exit(1)

        if _is_player_one_turn:
            _board = _player_turn(_board, _player_one)
        else:
            _board = _player_turn(_board, _player_two)

        if _calculate_winner(_board):
            if _is_player_one_turn:
                _print_board(_board)
                print(f"{separator} Player One wins! {separator}")
                print(f"{separator} Application will now exit. {separator}")
                sys.exit(1)
            else:
                _print_board(_board)
                print(f"{separator} Player Two wins! {separator}")
                print(f"{separator} Application will now exit. {separator}")
                sys.exit(1)

        _is_player_one_turn = not _is_player_one_turn
        _turn_count += 1
