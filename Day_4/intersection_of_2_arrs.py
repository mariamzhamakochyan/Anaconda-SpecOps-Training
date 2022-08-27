def arrs(num1, num2):
    return list(set(num1) & set(num2))
num1 = [4,9,5]
num2 = [9,4]
print(arrs(num1, num2))
