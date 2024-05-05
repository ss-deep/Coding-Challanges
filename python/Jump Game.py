'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump 
length at that position.
Return true if you can reach the last index, or false otherwise.
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.'''

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # counter=0
    # for i in range(len(nums)-1):
    #     counter=max(counter,nums[i])
    #     counter-=1
    #     if counter<0:
    #         return False
    # return True

    
    currmax = 0
    for i in range(len(nums)):
        if i > currmax:
            return False
        currmax = max(currmax, i + nums[i])
    return True


print(canJump([2,3,1,1,4]))#true
print(canJump([3,2,1,0,4]))#false
print(canJump([0]))#true
print(canJump([1]))#true
print(canJump([2,0,0]))#true
print(canJump([2,5,0,0])) #true
print(canJump([0,2,3])) #false
print(canJump([1,2])) #true
print(canJump([1,0,1,0])) #false
#[2,3,1,0,4,2,3,3,5,0,0,0,2,1]


