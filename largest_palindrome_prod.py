def is_palindrome(num):
    while True:
        str(num) == str(num)[::-1]
def largest_palindrome(top, bot):
    for i  in range(top, bot, -1):
        for j in range(top, bot, -1):
                num = i *j
                if is_palindrome(num):
                   return num
print(largest_palindrome(999,100))

