sum = 0
for i in range(3, 1001):
    if i % 3 == 0 or i % 5 == 0:
       sum += i
print(sum)
