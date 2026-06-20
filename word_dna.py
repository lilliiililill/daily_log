# 2026.06.21
# word_dna.py

text = input("문장 입력: ").split()

mapping = {}
dna = []
next_code = "A"

for word in text:

    if word not in mapping:

        mapping[word] = next_code

        next_code = chr(ord(next_code) + 1)

    dna.append(mapping[word])

print("DNA 패턴:", "".join(dna))
print("사전:", mapping)
