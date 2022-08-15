filename = input("Enter the filename: ")
file = open(filename, 'r')
file = file.read()
file = file.split()
count = 0
for word in file:
    count += len(word)
print(count)
