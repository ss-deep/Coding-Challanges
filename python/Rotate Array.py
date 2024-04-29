'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # for i in range(k):
    #     item=nums.pop()
    #     nums.insert(0,item)       
    ### or
    # pointer=k%len(nums)
    # nums[:]=nums[-pointer:]+nums[:-pointer]
    # return(nums)

    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]

    return nums

print(rotate([1,2,3,4,5,6,7],3)) #[5,6,7,1,2,3,4]
print(rotate([-1,-100,3,99], 2)) #[3,99,-1,-100]
print(rotate([1,2],5)) #[2,1]
# a=[1,2,3,4,5,6,7]
# print(a[-1:])