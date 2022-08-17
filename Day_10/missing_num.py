def arr(num):
    for i in range(0,len(num)):
        swap = False
        for j in range(0, len(num) - i - 1):
            if num[j] > num[j + 1]:
               num[j], num[j+1] = num[j+1], num[j] 
               swap = True
            if swap == False:
               break  
    for n in range(num[-1]+1):
        if n not in num:
           return n 
num = [9,6,4,2,3,5,7,0,1]
print(arr(num))
