'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 '''

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # i=0
    # j=0
    # while j<len(nums):
    #     if nums[i]==nums[j]:
    #         j+=1
    #     else:
    #         i+=1
    #         nums[i]=nums[j]
    #         j+=1
    # return len(nums[0:i+1])

    i=0
    for j in range(0,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))