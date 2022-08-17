i = 3
factors = []
number = 600851475143
while i < number:
      if number % i != 0:
         i += 2
      else: 
         number = number / i
         factors.append(i)
while number >= i:
      if number % i != 0:
         i += 2
      else: 
         number = number / i
         factors.append(i)
print(max(factors))
     
