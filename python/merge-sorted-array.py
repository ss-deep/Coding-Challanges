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
    # j=0
    # if nums2==[]:
    #     return nums1
    # for i in range(m+n):
    #     if j<len(nums2):
    #         print("i ",i," j ",j)
    #         if nums1[i]<nums2[j] and nums1[i]!=0:
    #             continue
    #         elif nums1[i]>=nums2[j] or nums1[i]==0:
    #             print(nums1)
    #             nums1.insert(i,nums2[j])
    #             j+=1
    #             nums1.pop()
    #             print(nums1)
    # return nums1
    # i=0
    # j=0
    # while(j<n):
    #     if nums1[i]<=nums2[j] and nums1[j]<nums1[i+1]:
    #         nums1.insert(i+2,nums2[j])
    #         nums1.pop()
    #         j+=1
    #         i+=1
    #         print(f' in if num1 {nums1} i {i} j {j}')
    #     elif nums1[i]>=nums2[j]:
    #         nums1.insert(i,nums2[j])
    #         nums1.pop()
    #         j+=1
    #         i+=1
    #         print(f'in elif num1 {nums1} num2 {nums2}')
    #     else:
    #         i+=1
    # return nums1

    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
print(merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3)) #[-1,0,0,1,2,2,3,3,3]
