# 2026.09.19
# collatz.py

def collatz(n):

    steps = [n]

    while n != 1:

        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps.append(n)

    return steps


num = int(input("숫자를 입력하세요: "))
result = collatz(num)

print(" -> ".join(map(str, result)))
print(f"총 {len(result) - 1}단계 만에 1이 되었습니다.")
