# Given an integer array 'nums', rotate the array to the right by 'k' steps, where 'k' is non-negative.

# -- Performance At Time Of Completion --
# Runtime : Beats 79.71% of users with Python3 - GREEN
# Memory : Beats 41.08% of users with Python3 - RED (but only 0.14MB from GREEN)

nums = [1,2,3,4,5,6,7,8,9]
k = 3

k = k % len(nums)
if k > 0 and len(nums) > 1:
    nums[:k-1], nums[k:] = nums[-k:], nums[:-k]

print(nums)