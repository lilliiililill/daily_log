# 2026.10.04
# count_value_changes.py

def count_changes(nums):

    count = 0

    for i in range(1, len(nums)):

        if nums[i] != nums[i - 1]:

            count += 1

    return count


print(count_changes([3, 3, 1, 1, 5, 2, 2, 7]))
