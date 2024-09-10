'''Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
Example 1:
Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:
Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.
'''
def averageValue(nums):
    avg=0
    count=0
    for i in nums:
        if i%3==0 and i%2==0:
            avg+=i
            count+=1
    if count==0:
        return 0
    else:
        return (avg//count) #converts to integer
    
print(averageValue([1,3,6,10,12,15]))
print(averageValue([9,3,8,4,2,5,3,8,6,1]))