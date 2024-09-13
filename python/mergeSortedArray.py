'''Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''

def mergeSortedArray(num1, m, num2, n):
    p1=m-1
    p2=n-1

    for p in range(m+n-1,-1,-1):
        if p2<0:
            break
        elif p1>=0 and num1[p1]>num2[p2]:
            num1[p]=num1[p1]
            p1-=1
        else:
            num1[p]=num2[p2]
            p2-=1
    return num1

print(mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))