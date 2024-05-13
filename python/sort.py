'''You will be given an array of integers to sort. Sorting must first by frequency of occurrence, then by value. For instance, given an array 
[4,5,6,5,4,3] there is one each of 6’s and 3’s and there are two 4’s and 5’s. The sorted list is [3,6,4,4,5,5]
example:
nums=[4,5,6,5,4,3]  output=[3,6,4,4,5,5]

'''

def sort_list(nums):
    dic={}
    for i in range(len(nums)):
        dic[nums[i]]=dic.get(nums[i],0)+1
        print(dic)


print(sort_list([4,5,6,5,4,3]))