
# Given an array 'nums', return the majority element. The majority element is the element that appears more than 
# ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# -- Performance At Time Of Completion --
# Runtime : Beats 95.56% of users with Python3 - GREEN
# Memory : Beats 32.72% of users with Python3 - RED (but only 0.12MB from GREEN)

def majorityElement(nums):
    if len(nums) == 1:
        return nums[0]

    nums.sort()
    majority_frequency = len(nums)/2
    current_integer = nums[0]
    pointer_frequency = 1
    majority_element = -1
    for n in range (1, len(nums)):
        if nums[n] == current_integer:
            pointer_frequency += 1
            if pointer_frequency > majority_frequency:
                majority_element = current_integer
                break
        else:
            current_integer = nums[n]
            pointer_frequency = 1
    return majority_element

print(majorityElement([2,2,1,1,1,2,2]))