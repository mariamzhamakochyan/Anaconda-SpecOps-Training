filename1 = input("Enter the file name with names: ")
file1 = open(filename1, 'r')
filename2 = input("Enter the file name to write changed names: ")
file2 = open(filename2, 'w')
file1 = file1.read()
name = file1.split()
file2 = file2.write(file1.title())
