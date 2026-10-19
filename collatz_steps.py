# 2026.10.19
# collatz_steps.py

def collatz_steps(n: int) -> int:

    if n <= 0:

        raise ValueError("양수만 입력 가능")

    steps = 0

    while n != 1:

        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1

    return steps

if __name__ == "__main__":

    print(collatz_steps(27))
