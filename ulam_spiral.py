# 2026.08.16
# ulam_spiral.py

N = 39
x = y = N // 2
dx, dy = 1, 0
step = turn = 1

board = [[0] * N for _ in range(N)]

def prime(n):

    return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))

for n in range(1, N * N + 1):

    board[y][x]  = n

    x, y = x + dx, y + dy

    if n == turn:

        dx, dy = -dy, dx
        step += (dy == 0)

        turn += step


for row in board:

    print("".join("██" if prime(n) else "  " for n in row))
