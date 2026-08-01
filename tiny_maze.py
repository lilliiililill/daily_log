# 2026.08.02
# tiny_maze.py

import random

tiles = "·▲◆"

maze = "".join(random.choice(tiles) for _ in range(20))

print(maze)
print("보물 개수:", maze.count("◆"))
