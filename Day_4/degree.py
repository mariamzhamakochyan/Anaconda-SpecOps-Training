def arr(num):
    i =  max(set(num), key = num.count)
    for i in num:
        return i
num = [1,1,1,2,4,5,6]
print(arr(num))
