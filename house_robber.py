# 2026.10.23
# house_robber.py

def rob(nums):

    if not nums:

        return 0

    if len(nums) == 1:

        return nums[0]

    prev2, prev1 = 0, 0

    for num in nums:

        current = max(prev1, prev2 + num)

        prev2 = prev1
        prev1 = current

    return prev1

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
