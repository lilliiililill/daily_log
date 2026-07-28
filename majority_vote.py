# 2026.07.29
# majority_vote.py

def majority_candidate(numbers: list[int]) -> int | None:

    """과반수 후보를 O(n) 시간, O(1) 공간으로 찾는다."""

    candidate = None
    count = 0

    for number in numbers:

        if count == 0:

            candidate = number

        count += 1 if number  == candidate else -1

    # 실제 과반수인지 검증

    if candidate is not None and numbers.count(candidate) > len(numbers) // 2:

        return candidate

    return None

numbers = [3, 3, 4, 4, 4, 4, 4, 2, 8, 9, 9, 4, 4]
result = majority_candidate(numbers)

print("과반수 원소:", result)
