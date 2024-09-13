'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    i=0
    prefix=""
    str=strs[0]
    for i in range(1,len(strs)):
        # print("str",str, "strs[i]",strs[i],"prefix",prefix)
        if len(str)>0:
            for j in range(len(strs[i])):
                # print("str",str, "strs[i]",strs[i])
                # print("strs[i]",strs[i],"str[j]",str)
                if j<len(str) and str[j]==strs[i][j]: # and :
                    prefix=prefix+strs[i][j]
                    # print(prefix)
                else:
                    # print("else")
                    break
        str=prefix
        prefix=""
    return str
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["aaa","aa","aaa"]))
