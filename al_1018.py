import sys

n, m = map(int, sys.stdin.readline().split())

board_list = [['_' for i in range(m)] for j in range(n)]
board_w = [['_' for i in range(8)] for j in range(8) ]
board_b = [['_' for i in range(8)] for j in range(8) ]

for i in range(n):
    board_list[i] = list(sys.stdin.readline().rstrip())
    
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                board_w[i][j] = 'W'
                board_b[i][j] = 'B'
            else:
                board_w[i][j] = 'B' 
                board_b[i][j] = 'W'
        elif i % 2 == 1:
            if j % 2 == 0:
                board_w[i][j] = 'B'
                board_b[i][j] = 'W'
            else:
                board_w[i][j] = 'W' 
                board_b[i][j] = 'B'

def count_board_diff(board_a, board_b):
    count = 0
    for i in range(8):
        for j in range(8):
            if board_a[i][j] != board_b[i][j]:
                count +=1
    return count

min_count = 64
len_n = n - 7
len_m = m - 7

def get_board_in_list(board, i, j):
    new_board = [['_' for i in range(8)] for j in range(8)]
    for row in range(8):
        for col in range(8):
            new_board[row][col] = board[row+i][col+j]
    return new_board

for i in range(len_n):
    for j in range(len_m):
        in_board = get_board_in_list(board_list, i, j)
        min_w = count_board_diff(in_board, board_w)
        min_b = count_board_diff(in_board, board_b)
        min_count = min(min_w, min_b, min_count)

print(min_count)        


        


