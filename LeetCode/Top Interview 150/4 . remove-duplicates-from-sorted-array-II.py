# Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates in-place such that each unique 
# element appears upto twice. The relative order of the elements should be kept the same. 

# -- Performance At Time Of Completion --
# Runtime : Beats 61.96% of users with Python3 - GREEN
# Memory : Beats 57.57% of users with Python3 - GREEN

nums = [0,0,1,1,1,1,2,3,3]

i = 0
while i in range (len(nums)-2):
    if ((nums[i+1] == nums[i]) and (nums[i+2] == nums[i])):
        nums.pop(i+2)
    else:
        i += 1
print(nums)