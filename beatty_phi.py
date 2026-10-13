# 2026.10.14
# beatty_phi.py

def beatty_phi(n = 20):

    phi = (1 + 5 ** 0.5) / 2
    return [int(i * phi) for i in range(1, n + 1)]

print(beatty_phi())
