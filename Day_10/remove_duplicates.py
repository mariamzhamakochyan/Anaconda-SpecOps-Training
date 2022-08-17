def duplicate(nums):
    list1 = []
    list2 = [] 
    list = []
    for i in nums:
        if i not in list1:
           list1.append(i)
        else:
           list2.append('-')
    list = list1 + list2
    return list
nums = [1,1,1,2,2,2,3,3,4]
print(duplicate(nums))
