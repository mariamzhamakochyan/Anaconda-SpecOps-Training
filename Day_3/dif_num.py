num_sum = 0
sum_of_squares = 0
for i in range(1,101):
    num_sum += i
    sum_of_squares += (i ** 2)
print((num_sum**2) - sum_of_squares)
