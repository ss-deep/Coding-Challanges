'''Given an integer x, return true if x is a 
palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.'''
def isPalindrome(x):
    # num=0
    # if x < 0:
    #     return False
    # else:
    #     while x>num:
    #         num=x%10+num*10
    #         x=x//10
    # if x == num or x == num // 10:
    #     return True
    # else:
    #     return False

    strnum=str(x)
    for i in range(len(strnum)):
        if strnum[i]!=strnum[-(i+1)]:
            return False
    return True

print(isPalindrome(12521))