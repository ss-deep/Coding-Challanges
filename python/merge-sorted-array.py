# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    j=0
    if nums2==[]:
        return nums1
    for i in range(m+n):
        print("i ",i," j ",j)
        if nums1[i]<nums2[j] and nums1[i]!=0:
            
            continue
        elif nums1[i]>=nums2[j] or nums1[i]==0:
            print(nums1)
            nums1.insert(i,nums2[j])
            j+=1
            nums1.pop()
            print(nums1)
    return nums1
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
