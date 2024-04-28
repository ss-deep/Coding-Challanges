'''
Given an array nums of size n, return the majority element.
eg : Input: nums = [3,2,3]
Output: 3
eg : Input: nums = [2,2,1,1,1,2,2]
Output: 2'''
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_dict={}
    for i in nums:
        # 2 - 1, 
        nums_dict[i]=nums_dict.get(i,0) + 1
        if nums_dict.get(i) > len(nums) / 2:
            return i

        # if i in nums_dict:
        #     nums_dict[i]+=1
        # else:
        #     nums_dict[i]=1

        # print(nums_dict)
        # if nums_dict[i]>len(nums)/2:
        #     return i
    
# nums = [3,2,3,2]
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([6,5,5]))
print(majorityElement([1]))

