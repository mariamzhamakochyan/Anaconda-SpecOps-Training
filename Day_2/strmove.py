def strmove(str, position):
    str1 = str[0:position]
    str2 = str[position:]
    res = str2 + str1
    return res
str = input("Enter the string: ")
position = int(input("Enter the position: "))
print(strmove(str, position))
