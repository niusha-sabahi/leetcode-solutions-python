# You are given two integer arrays 'nums1' and 'nums2', sorted in non-decreasing order, and two integers 'm' and 'n', 
# representing the number of elements in 'nums1' and 'nums2' respectively. Merge 'nums1' and 'nums2' into a single 
# array sorted in non-decreasing order. 'nums1' contains '0's in place of the items that will be added from 'nums2'.

# Runtime : Beats 88.94% of users with Python3 - GREEN
# Memory : Beats 87.15% of users with Python3 - GREEN

nums1 = [5,6,7,0,0,0,0]
m = 3

nums2 = [2,3,3,4]
n = 4        

for i in range (n):
    nums1[m+i] = nums2[i]
nums1.sort()

print("The sorted list: " , nums1)
