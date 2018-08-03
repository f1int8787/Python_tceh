import sys
def init_board():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
    return board

def current_board(coursor, board):
    coursor = [list_o for list_m in coursor for list_o in list_m]
    board = [list_o for list_m in board for list_o in list_m]
    show_board(board)
    return("""
      {9}   |  {10}   |  {11}  \n 
      {0}   |  {1}   |  {2}  \n     
    ------+------+------\n
      {12}   |  {13}   |  {14}  \n
      {3}   |  {4}   |  {5}  \n 
    ------+------+------\n
      {6}   |  {7}   |  {8}  \n
      {15}   |  {16}   |  {17}  \n""".format(*board, *coursor))    

def show_coursor(x,y):
    try:
        coursor = [['*',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        coursor[x][y], coursor[0][0] = coursor[0][0], coursor[x][y]
    except IndexError as e:
        print('Can\'t move that way!',e)
    except TypeError as e:
        print('Can\'t move that way!')
    else:
        return coursor
    
def show_board(board = None):
    if board:
        board1 = board
        return(board1)               

def menu(x = 0, y = 0):
    print("welcome to the x-0!")
    player1 = 'player1'
    player2 = 'player2'
    name = [player1, player2]
    board = init_board()
    print(current_board(show_coursor(x,y), board))
    print(show_coursor(x,y))
    print(board)
    while True:
        for player in name:
            while True:        
                    coursor_pos = input("""please,{} chose the position with w,a,s,d\n>>>"""
                                        .format(player))
                    if coursor_pos == 'w':
                        x -= 1
                    elif coursor_pos == 's':
                        x += 1
                    elif coursor_pos == 'd':
                        y += 1
                    elif coursor_pos == 'a':
                        y-= 1
                    elif coursor_pos == 'e':
                        if player == 'player1':
                            board[x][y] = 'x'
                        else:
                            board[x][y] = 'o'                    
                        print(current_board(show_coursor(x,y),board))
                        break
                    print(x,y)
                    try:                        
                        print(current_board(show_coursor(x,y), board))
                    except TypeError as e:
                        print('Can\'t move that way!',e)
                        x, y = 0, 0
 
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print('Quitting the game') 
        sys.exit(0)    