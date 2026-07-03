# 2026.07.04
# infinite_zoom.py

size = 1

while True:

    for y in range(-size, size + 1):

        line = ""

        for x in range(-size, size + 1):

            line += "█" if (x & y) == 0 else " "

        print(line)

    input("\nEnter를 누르면 확대됩니다...")
    size *= 2
