def arr(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
           even.append(i)
        else:
           odd.append(i)
    return even + odd
nums = [1,4,2,7,3]
print(arr(nums))
