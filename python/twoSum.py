def twoSum(nums, sum):
    map={}
    for i in range(len(nums)):
        # num2=sum-nums[i]
        # if num2 in map:
        #     return [map[num2],i]
        # else:
        #     map[nums[i]]=i
        if nums[i] in map:
            return [map[nums[i]],i] 
        else:
            map[sum-nums[i]]=i
    
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))