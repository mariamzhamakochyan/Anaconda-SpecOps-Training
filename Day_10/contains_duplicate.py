def arr(nums):
    res = []
    for i in nums:
        if i not in res:
           res.append(i)
    if len(res) == len(nums):
       return False
    else:
       return True
nums = [1,2,3,4]
print(arr(nums))
        
