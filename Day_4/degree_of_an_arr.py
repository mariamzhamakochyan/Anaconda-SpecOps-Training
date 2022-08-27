
'''Not correct'''

def degree(nums):
    i =  max(set(nums), key = nums.count)
    first = nums.index(i)
    nums_ = str(nums)[::-1]
    nums_ = int(nums_)
    last = len(nums) - nums_.index(i) 
    res = last - first
    return res
nums = [1,1,1,2,4,5,6]
print(degree(nums))
