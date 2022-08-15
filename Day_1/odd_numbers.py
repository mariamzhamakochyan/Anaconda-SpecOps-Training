first_num = int(input("Enter the first number: "))
last_num = int(input("Enter the last number: "))
odd_count = 0
for i in range(first_num, last_num + 1):
    if i % 2 != 0:
       odd_count += 1
print(odd_count)
