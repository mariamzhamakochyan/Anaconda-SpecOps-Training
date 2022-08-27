def strStr(haystack, needle):
    if needle not in haystack:
       return -1
    else:
       return haystack.index(needle)
haystack = 'hello'
needle = 'll'
print(strStr(haystack, needle))
