def check(board, m):
        # 가로
        for r in board:
            if r == [m, m, m]:
                return True
        # 세로
        for c in range(3):
            if [board[0][c], board[1][c], board[2][c]] == [m, m, m]:
                return True
        # 대각선
        if [board[0][0], board[1][1], board[2][2]] == [m, m, m]:
            return True
        if [board[2][0], board[1][1], board[0][2]] == [m, m, m]:
            return True

def solution(board):
    board = [list(row) for row in board]
    o_cnt = sum(r.count('O') for r in board)
    x_cnt = sum(r.count('X') for r in board)

    if not (x_cnt == o_cnt):
        return 0
    
    # O and X 둘 다 승리
    if check(board, 'O') and check(board, 'X'):
        return 0
    
    # O가 승리
    if check(board, 'O') and o_cnt != x_cnt + 1:
        return 0
    
    # X가 승리
    if check(board, 'X') and o_cnt != x_cnt:
        return 0
    
    return 1