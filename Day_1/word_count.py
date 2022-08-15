filename = input("Enter the file name: ")
file = open(filename, 'r')
file = file.read()
file = file.split()
dict = {}
keys = dict.keys()
for word in file:
    if word in keys:
       dict[word] += 1
    else:
       dict.update({word:1})
print(dict)
