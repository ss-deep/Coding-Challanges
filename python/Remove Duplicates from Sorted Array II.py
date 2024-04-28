'''Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 '''
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """    
    counter=1
    i=0
    j=1
    while j<len(nums):
        if nums[i]==nums[j]:
            if counter<2:
                i+=1
                nums[i]=nums[j]
                j+=1
                counter=2
            else:
                j+=1
        else:
            i+=1
            nums[i]=nums[j]
            j+=1
            counter=0
    return i+1
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(removeDuplicates([1,1,1,2,2,3]))


'''
two_occ = False
        if nums == []:
            return 0
        j = 1
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1] and not(two_occ):
                two_occ = True
                nums[j]=nums[i]
                j += 1
            elif nums[i] != nums[i-1]:
                nums[j]=nums[i]
                j += 1
                two_occ=False
        return j

----or----   

count = 1
        for i in range(1, len(nums)):
            if count == 1 or nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count +=1
        return count
        
        '''