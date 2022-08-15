sum = 0
num1 = 0
filename = input("Enter the file name: ")
file = open(filename, 'r')
file = file.read()
file = file.split()
for num in file:
    num1 = str(num)
    sum += int(num1)
print(sum)
