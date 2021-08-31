board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

def printboard(board):
    print(' ')
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '       1' + '|' + '2' + '|' + '3')
    print('-+-+-' + '       -+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + '       4' + '|' + '5' + '|' + '6')
    print('-+-+-' + '       -+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + '       7' + '|' + '8' + '|' + '9')
    print(' ')
    print(' ')

def clearboard():
    for _ in board:
        board[_] = ' '

def spot_taken_x():
    """spot taken function for x"""
    ask_again = input('That space is all ready taken! Place you mark in an empty space.')
    if board[ask_again] != ' ':
        spot_taken_x()
    else:
        board[ask_again] = 'x'

def spot_taken_o():
    """spot taken function for o"""
    ask_again = input('That space is all ready taken! Place you mark in an empty space.')
    if board[ask_again] != ' ':
        spot_taken_o()
    else:
        board[ask_again] = 'o'

def turn_x():
    """turn function for player x"""
    turnx = input('Your turn x, where would you like to place your mark?:')
    if int(turnx) > 9:
        print('invalid play, try again')
        return turn_x()
    if board[turnx] == ' ':
        board[turnx] = 'x'
    else:
       spot_taken_x()

def turn_o():
    """turn function for player o"""
    turno = input('Your turn o, where would you like to place your mark?:')
    if int(turno) > 9:
        print('invalid play, try again')
        return turn_o()
    if board[turno] == ' ':
        board[turno] = 'o'
    else:
        spot_taken_o()


def checkwin():
    """function that checks for a win"""
    for _ in board:
        if board['1'] == 'x' and board['2'] == 'x' and board['3'] == 'x':
            return True
        elif board['4'] == 'x' and board['5'] == 'x' and board['6'] == 'x':
            return True
        elif board['7'] == 'x' and board['8'] == 'x' and board['9'] == 'x':
            return True
        elif board['1'] == 'x' and board['4'] == 'x' and board['7'] == 'x':
            return True
        elif board['2'] == 'x' and board['5'] == 'x' and board['8'] == 'x':
            return True
        elif board['3'] == 'x' and board['6'] == 'x' and board['9'] == 'x':
            return True
        elif board['1'] == 'x' and board['5'] == 'x' and board['9'] == 'x':
            return True
        elif board['3'] == 'x' and board['5'] == 'x' and board['7'] == 'x':
            return True
        elif board['1'] == 'o' and board['2'] == 'o' and board['3'] == 'o':
            return True
        elif board['4'] == 'o' and board['5'] == 'o' and board['6'] == 'o':
            return True
        elif board['7'] == 'o' and board['8'] == 'o' and board['9'] == 'o':
            return True
        elif board['1'] == 'o' and board['4'] == 'o' and board['7'] == 'o':
            return True
        elif board['2'] == 'o' and board['5'] == 'o' and board['8'] == 'o':
            return True
        elif board['3'] == 'o' and board['6'] == 'o' and board['9'] == 'o':
            return True
        elif board['1'] == 'o' and board['5'] == 'o' and board['9'] == 'o':
            return True
        elif board['3'] == 'o' and board['5'] == 'o' and board['7'] == 'o':
            return True
        else:
            return False


def restartwin():
    """asks to restart after a win"""
    restartq = input('Congratulations you win! Would you Like to play again? ')
    if restartq[0].lower() == 'y':
        return True
    elif restartq[0].lower() == 'n':
        return False


def restarttie():
    """asks to restart after a tie"""
    tieq = input('Tie game! Would you Like to play again? ')
    if tieq[0].lower() == 'y':
        return True
    elif tieq[0].lower() == 'n':
        return False


def game():
    """function that calls all other functions to run actual game"""
    printboard(board)
    plays = 1
    while plays < 10:
        if plays % 2 == 0:
            turn_o()
        else:
            turn_x()
        printboard(board)
        plays += 1
        if plays > 4:
            if checkwin() != True:
                continue
            if restartwin() == True:
                plays = 1
                clearboard()
                printboard(board)
            else:
                return 'thanks for playing!'
        else:
            continue
    if restarttie() == True:
        clearboard()
        game()
    else:
        print('thanks for playing!')


if __name__ == '__main__':
    game()