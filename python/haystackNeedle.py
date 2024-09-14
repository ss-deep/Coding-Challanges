def haystackNeedle(haystack, needle):
    index=-1
    m=len(haystack)
    n=len(needle)
    for i in range(m):
        # print("i=",i,"haystack[i:n]=",haystack[i:i+n])
        if haystack[i:i+n] == needle:
            return i
    return -1

print(haystackNeedle("heloll", "ll"))
print(haystackNeedle("sadbutsad", "sad"))