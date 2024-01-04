
    
def solution(board):
    board = [list(row) for row in board]
    def check_win(t):
        for row in board:
            if row == [t,t,t]:
                return 1
        for row in range(3): 
            if [board[col][row] for col in range(3)] == [t,t,t]:
                return 1
        if [board[i][i] for i in range(3)] == [t,t,t]:
            return 1
        if [board[2][0], board[1][1], board[0][2]] == [t,t,t]:
            return 1
        return 0

    answer = 1
    # O -> X, X->O
    # 게임 계속 진행
    # 게임판이 규칙을 지켜서 진행했을 때 나올 수 있는 경우인지?
    
    o = 0
    x = 0
    dot = 0
    
    for row in board:
        o += row.count('O')
        x += row.count('X')
        dot += row.count('.')
    if check_win('O') and check_win('X'):
        answer = 0
    elif check_win('O'):
        if o != x+1:
            answer = 0
    elif check_win('X'):
        if o != x:
            answer = 0
    else:
        if o ==x or o==x+1:
            answer = 1
        else:
            answer = 0
    return answer