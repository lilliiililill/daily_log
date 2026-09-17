# 2026.09.18
# color_palette.py

import tkinter as tk
import random

def random_color():

    return tuple(random.randint(0, 255) for _ in range(3))

def to_hex(rgb):

    r, g, b = rgb
    return f"#{r:02X}{g:02X}{b:02X}"

def generate_palette(n=5):

    root = tk.Tk()
    root.title("랜덤 컬러 팔레트")

    for _ in range(n):

        rgb = random_color()
        hex_code = to_hex(rgb)

        frame = tk.Frame(root)
        frame.pack(fill = "x", padx = 10, pady = 5)

        swatch = tk.Label(frame, bg = hex_code, width = 10, height = 2)
        swatch.pack(side = "left")

        label = tk.Label(frame, text = f"{hex_code}    RGB{rgb}", font=("Consolas", 12))
        label.pack(side = "left", padx = 10)

    root. mainloop()


if __name__ == "__main__":

    generate_palette(5)
