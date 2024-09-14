def isHappy(n):
    def get_sum(num):
        total=0
        while num>0:
            total += (num%10) ** 2
            num=num//10
        return total
    
    slow_runner=n
    fast_runner=get_sum(n)
    while slow_runner!=fast_runner and fast_runner != 1:
        slow_runner=get_sum(slow_runner)
        fast_runner=get_sum(get_sum(fast_runner))
    return fast_runner == 1

print(isHappy(19))