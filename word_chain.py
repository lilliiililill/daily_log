# 2026.06.14
# word_chain.py

words = input("단어들을 공백으로 입력: ").split()

valid = all(
    a[-1] == b[0]
    for a, b in zip(words, words[1:])
)

print("성공!" if valid else "실패!")
