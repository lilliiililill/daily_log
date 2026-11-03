# 2026.11.04
# move_zeros.py

def move_zeros(nums):

    non_zero = 0

    for i in range(len(nums)):

        if nums[i] != 0:

            nums[non_zero] = nums[i]
            non_zero += 1


    for i in range(non_zero, len(nums)):

        nums[i] = 0

    return nums


nums = [0, 1, 0, 3 ,12]

print(move_zeros(nums))
