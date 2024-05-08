'''Write a function that takes in a string. It should return a string where consecutive repeating characters have been 
truncated. For example:
"aaaabbbbbbcccc" => "abc"
"caaaat" => "cat"
'''

# def find(nums,val):
#     max=0
#     for num in nums:
#         if num<val and max<num:
#             max=num
#     return max



# print(find([1,2,30,3,10,70],80))

def truncate(s):
    newstr=s[0]
    for l in s:
        if newstr[-1]!=l:
            newstr+=l

    return newstr
print(truncate('aaaabbbbbbcccc'))