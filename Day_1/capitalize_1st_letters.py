filename1 = input("Enter the file name to read the text: ")
file1 = open(filename1, 'r')
filename2 = input("Enter the file name to write the text: ")
file2 = open(filename2, 'w')
for line in file1:
    file2.write(line.title())
