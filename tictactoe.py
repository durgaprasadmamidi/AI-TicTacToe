"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for row in board:
        for value in row:
            if value == 'O':
                ocount += 1
            elif value == 'X':
                xcount += 1
    if xcount > ocount:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    available = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == EMPTY:
                available.add((i, j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    mark = player(board)
    if board[action[0]][action[1]] == 'X' or board[action[0]][action[1]] == 'O':
        raise Exception('Move not possible')
    else:
        newBoard[action[0]][action[1]] = mark
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != EMPTY:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in ['X', 'O'] or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

def Find(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    if player(board) == 'X':
        maxScore = -math.inf
        for toChoose in actions(board):
            score = Find(result(board, toChoose))
            if score >= maxScore:
                maxScore = score
        return  maxScore
    if player(board) == 'O':
        minScore = math.inf
        for toChoose in actions(board):
            score = Find(result(board, toChoose))
            if score < minScore:
                minScore = score
        return  minScore

def minimax(board):
    
    if terminal(board):
        return utility(board)
    if player(board) == 'X':
        maxScore = -math.inf
        bestMove = (None, None)
        for toChoose in actions(board):
            score = Find(result(board, toChoose))
            if score >= maxScore:
                maxScore = score
                bestMove = toChoose
        return bestMove
    if player(board) == 'O':
        minScore = math.inf
        bestMove = (None, None)
        for toChoose in actions(board):
            score = Find(result(board, toChoose))
            if score < minScore:
                minScore = score
                bestMove = toChoose
        return bestMove
