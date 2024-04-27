# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i=0
    j=len(nums)-1
    if nums==[]:
        return 0
    while i<=j:
        if nums[j]==val:
            j-=1
            nums.pop()
        elif nums[i]==val:
            nums[i]=nums[j]
            i+=1
            j-=1
            nums.pop()
        else: 
            i+=1
    print(nums)

removeElement([0,1,2,2,3,0,4,2], 2)
removeElement([3,2,2,3], 3)
removeElement([1], 1)
removeElement([3,3], 3)

'''
c=0
for i in range(len(n)):
    if n[i]!=val:
        n[c]=n[i]
        c=c+1
return c

or

i = 0
n = len(nums)
while i < n:
    if nums[i] == val:
        nums[i] = nums[n - 1]
        n -= 1
    else:
        i += 1
return n

'''