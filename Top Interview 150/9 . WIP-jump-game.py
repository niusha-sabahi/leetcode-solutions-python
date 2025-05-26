# Theory - problem is can we jump over every 0 we encounter in list? 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        else:
            left_0 = len(nums)
            leap = 0
            for i in range(len(nums), 0, -1): # loops through each digit backwards to find 0s
                if i > left_0:
                    continue     # for skipping 0 ... 0  if you get trapped between them                   
                    if nums[i] == 0:
                        j = 1
                        while True: # iterate through each digit left of current 0 to see if we can jump the wall
                            if nums[i-j] > j+leap: # we can jump ! (or sometimes skip a 0 ... 0 if needed)
                                leap = 0
                                break
                            elif nums[i-j] == 0: # this 0 ... 0 clause cannot be jumped over, so we use leap to hope previous clause can skip it
                                right_0 = i
                                left_0 = i-j
                                leap = j+2
                                break
                            elif i+j > len(nums): # if we end up going past the first digit, proves we can jump over 0 :(
                                return False
                            else:
                                j+=1
            return True