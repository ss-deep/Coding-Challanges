def palindrome(num):
    strnum=str(num)
    for i in range(len(strnum)):
        if strnum[i]!=strnum[-(i+1)]:
            return False
    return True
print(palindrome(132321))
print(palindrome(-121))