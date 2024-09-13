'''Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

def arrayIntersection(num1,num2):
    #-----------------OR----------------
    # return list(set(num1) & set(num2))
    result=[]
    set1=set(num1)
    set2=set(num2)
    map={}
    for num in num1:
        map[num]=map.get(num,0)+1
    for num in num2:
        if num in map and map[num]>=1:
            result.append(num)
            map[num]=0
    return result


print(arrayIntersection([1,2,3,4,5],[3,4,5,6]))
print(arrayIntersection([1,2,2,1],[2,2]))