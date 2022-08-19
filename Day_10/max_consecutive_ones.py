def arr(nums):
    count = 0
    max_cons = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            max_cons = max(max_cons, count)
            count = 0
    return max(max_cons, count)
nums = [1,1,0,1,1,1]
print(arr(nums))
