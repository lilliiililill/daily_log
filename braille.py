# 2026.06.07
# braille.py

BRAILLE = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
    ' ': ' '
}

def to_braille(text):

    return ''.join(BRAILLE.get(ch, '?') for ch in text.lower())

while True:

    text = input("텍스트 입력 (종료: q): ")

    if text == 'q':

        break

    print(to_braille(text))
