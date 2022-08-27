def palindrome(str):
    new_str = ""
    for i in str:
        if i.isalpha():
           new_str += i
        elif i.isdigit():
           new_str += i
    new_str = new_str.lower()
    if new_str == new_str[::-1]:
       return True
    else:
       return False
str = input("Enter your string: ")
print(palindrome(str))
