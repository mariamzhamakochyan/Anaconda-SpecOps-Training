number = int(input("Enter the number: "))
sum = 0
multiply = 1
for digit in str(number):
    sum += int(digit)
    multiply *= int(digit)
print(multiply - sum)
