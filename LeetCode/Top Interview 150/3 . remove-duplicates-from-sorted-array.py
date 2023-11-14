# Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates in-place such that each unique 
# element appears only once. The relative order of the elements should be kept the same. 

# -- Approach -- 
# Using the Two-Pointer System with 'replace' and 'i'.

# -- Performance At Time Of Completion --
# Runtime : Beats 73.85% of users with Python3 - GREEN
# Memory : Beats 6.49% of users with Python3 - RED (but only 0.4MB from GREEN)

nums = [0,0,1,1,1,2,2,3,3,4]
#      [0,1,2,3,4,2,2,3,3,4]
#                 r       i

replace = 1 
for i in range(1, len(nums)):  
    if nums[i] != nums[i - 1]:  
        nums[replace] = nums[i]  
        replace += 1  
print(nums)