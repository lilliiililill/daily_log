# 2026.08.14
# common_trace.py

a = "algorithm"
b = "logarithm"

result = ""

for ch in a:

    if ch in b and ch not in result:

        result += ch

print(result)
