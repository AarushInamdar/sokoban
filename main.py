from game_settings import *
import copy


def loc_player_index(modded_board):
    for r, row in enumerate(modded_board):
        for c, cell in enumerate(row):
            if cell in (SPRITE, SPRITE_T):
                return (r, c)


def in_playable_zone(modded_board, row_num, col_num):
    return 0 <= row_num < len(modded_board) and 0 <= col_num < len(modded_board[0])


def down_push_function(modded_board, row, col):
    curr = (row, col)
    new = (row + 1, col)
    direction = "advance_down"
    success = attempt_move(modded_board, curr, new, direction)
    return success, modded_board


def up_push_function(modded_board, row, col):
    curr = (row, col)
    new = (row - 1, col)
    direction = "advance_up"
    success = attempt_move(modded_board, curr, new, direction)
    return success, modded_board


def left_push_function(modded_board, row, col):
    curr = (row, col)
    new = (row, col - 1)
    direction = "advance_left"
    success = attempt_move(modded_board, curr, new, direction)
    return success, modded_board


def right_push_function(modded_board, row, col):
    curr = (row, col)
    new = (row, col + 1)
    direction = "advance_right"
    success = attempt_move(modded_board, curr, new, direction)
    return success, modded_board


def can_advance_obj(modded_board, row_num, col_num, direction):
    if direction == "advance_right":
        return modded_board[row_num][col_num + 1] in (EMPTY, TARGET)
    elif direction == "advance_left":
        return modded_board[row_num][col_num - 1] in (EMPTY, TARGET)
    elif direction == "advance_down":
        return modded_board[row_num + 1][col_num] in (EMPTY, TARGET)
    elif direction == "advance_up":
        return modded_board[row_num - 1][col_num] in (EMPTY, TARGET)


def print_latest_board(modded_board):
    count = 0
    for row in range(len(modded_board)):
        i = 0
        count += 1
        for col in range(len(modded_board[0])):
            i += 1
            if i == 8:
                print(modded_board[row][col], end='')
            else:
                print(modded_board[row][col], end=' ')

        print()


def execute_player_move(current_board, current_position, new_position):
    r, c = current_position
    nr, nc = new_position

    if current_board[nr][nc] == TARGET:
        current_board[nr][nc] = SPRITE_T
    else:
        current_board[nr][nc] = SPRITE
    if current_board[r][c] == SPRITE_T:
        current_board[r][c] = TARGET
    else:
        current_board[r][c] = EMPTY


def move_obj(modded_board, current_position, directional_push):
    curr_r, curr_c = current_position
    newr, newc = (-1, -1)
    if directional_push == "advance_right":
        newr, newc = curr_r, curr_c + 1
    elif directional_push == "advance_left":
        newr, newc = curr_r, curr_c - 1
    elif directional_push == "advance_down":
        newr, newc = curr_r + 1, curr_c
    else:
        newr, newc = curr_r - 1, curr_c
    if modded_board[newr][newc] == TARGET:
        new_val = BOX_S
    else:
        new_val = BOX_NS
    modded_board[newr][newc] = new_val
    modded_board[curr_r][curr_c] = TARGET if modded_board[curr_r][curr_c] == BOX_S else EMPTY


def attempt_move(modded_board, curr, new, direction):
    new_row, new_col = new
    if in_playable_zone(modded_board, new_row, new_col):
        if modded_board[new_row][new_col] in (BOX_NS, BOX_S):
            if can_advance_obj(modded_board, new_row, new_col, direction):
                move_obj(modded_board, new, direction)
                execute_player_move(modded_board, curr, new)
        elif modded_board[new_row][new_col] in (EMPTY, TARGET):
            execute_player_move(modded_board, curr, new)


def check_win(board):
    win_not_status = True
    for row in board:
        if TARGET in row:
            win_not_status = False
    if win_not_status == True:
        print("You Win!")
        return win_not_status


modded_board = copy.deepcopy(board)
print_latest_board(modded_board)

while True:
    try:
        row_num, col_num = loc_player_index(modded_board)
        move_choice = input()
        print()
        if move_choice in ['q', 'Q']:
            print('Goodbye')
            break
        elif move_choice == ' ':
            modded_board = copy.deepcopy(board)
            print_latest_board(modded_board)
        elif move_choice in ['w', 'W']:
            up_push_function(modded_board, row_num, col_num)
            print_latest_board(modded_board)
        elif move_choice in ['a', 'A']:
            left_push_function(modded_board, row_num, col_num)
            print_latest_board(modded_board)
        elif move_choice in ['s', 'S']:
            down_push_function(modded_board, row_num, col_num)
            print_latest_board(modded_board)
        elif move_choice in ['d', 'D']:
            right_push_function(modded_board, row_num, col_num)
            print_latest_board(modded_board)
        else:
            print('enter a valid move:', end='')
        if check_win(modded_board) == True:
            break
    except:
        if check_win(modded_board) == True:
            break
        break
