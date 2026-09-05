# 2026.09.05
# self_detruct_dict.py

d = {i :i * i for i in range(5)}

while d:

    print(d.popitem())

print("텅")
