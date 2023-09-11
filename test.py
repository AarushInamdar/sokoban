try:
    current_row, current_column = loc_player_index(modded_board)
    player_move = input()
    print()
    if player_move == QUIT:
        print('Goodbye')
        break
    elif player_move == ' ':
        modded_board = copy.deepcopy(board)
        print_latest_board(modded_board)
    elif player_move == 'w':
        up_push_function(modded_board, current_row, current_column)
        print_latest_board(modded_board)
    elif player_move == 'a':
        left_push_function(modded_board, current_row, current_column)
        print_latest_board(modded_board)
    elif player_move == 's':
        down_push_function(modded_board, current_row, current_column)
        print_latest_board(modded_board)
    elif player_move == 'd':
        right_push_function(modded_board, current_row, current_column)
        print_latest_board(modded_board)
    else:
        # print()
        print('enter a valid move:', end='')
except:
    target_state = False;
    for current_row in modded_board:
        if TARGET in current_row:
            target_state = True;

    if target_state == False:
        print("You Win!")
    break
