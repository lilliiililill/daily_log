# 2026.07.26
# rule30.py

width = 61
cells = [0] * width
cells[width // 2] = 1

for _ in range(30):

    print("".join("██" if cell else "  " for cell in cells))

    cells = [

        cells[(i - 1) % width]
        ^ (cells[i] | cells[(i + 1) % width])
        for i in range(width)

        ]
