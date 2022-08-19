def arr(nums):
    unique = []
    result = 0
    for num in nums:
        if num not in unique:
            unique.append(num)
        else:
            unique.remove(num)
    result = unique[0]
    return result
nums = [2,2,1]
print(arr(nums))
