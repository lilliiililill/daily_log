# 2026.10.03
# count_local_peaks.py

def count_peaks(nums):

    return sum(

        nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
        for i in range(1, len(nums) - 1)

    )

print(count_peaks([1, 4, 2, 5, 3, 6, 1]))
