def arr(nums):
    sum = 0
    list = []
    for i in nums:
        if nums.count(i) == 1:
           sum += i
    return sum
nums = [1,2,3,4,5]
print(arr(nums))

