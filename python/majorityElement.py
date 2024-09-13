'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


def majorityElement(nums):
    count=0
    target=None 
    for num in nums:
        if count==0:
            target=num
        count+=1 if num==target else -1
    return target

print(majorityElement([2,2,1,1,1,1,1,2,2]))