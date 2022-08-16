num = int(input("Enter the number, to see if it's palindrome: "))
number = num
res = 0
while num > 0:
      digit = num % 10
      res = res * 10 + digit
      num = num // 10
if number == res:
   print("True")
else:
   print("False")
