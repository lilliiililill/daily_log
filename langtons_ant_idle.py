# 2026.07.18
# langtons_ant_idle.py

import tkinter as tk

SIZE = 31
CELL = 15

board = [[0] * SIZE for _ in range(SIZE)]

x = y = SIZE // 2

direction = 0

moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

root = tk.Tk()
root.title("Langton's Ant")

canvas = tk.Canvas(

    root,
    width = SIZE * CELL,
    height = SIZE * CELL,
    bg = "white"

)

canvas.pack()

def move_ant():

    global x, y, direction

    board[y][x] ^= 1

    color = "black" if board[y][x] else "white"
    canvas.create_rectangle(

        x * CELL,
        y * CELL,
        (x + 1) * CELL,
        (y + 1) * CELL,
        fill = color,
        outline = "gray"

    )

    direction = (direction + (1 if board[y][x] else -1)) % 4
    dx, dy = moves[direction]

    x = (x + dx) % SIZE
    y = (y + dy) % SIZE

    canvas.delete("ant")
    canvas.create_oval(

        x * CELL + 3,
        y * CELL + 3,
        (x + 1) * CELL - 3,
        (y + 1) * CELL - 3,
        fill = "red",
        tags = "ant"

    )

    root.after(30, move_ant)

move_ant()
root.mainloop()
