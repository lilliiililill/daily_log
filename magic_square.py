# 2026.06.28
# magic_square.py

n = 5

board = [[0] * n for _ in range(n)]

row = 0
col = n // 2

for num in range(1, n * n + 1):

    board[row][col] = num

    next_row = (row - 1) % n
    next_col = (col + 1) % n

    if board[next_row][next_col]:

        row = (row + 1) % n

    else:

        row = next_row
        col = next_col

width = len(str(n * n))

for line in board:

    print(" ".join(f"{num:>{width}}" for num in line))

print(f"\n한 줄의 합 = {n * (n * n + 1) // 2}")
