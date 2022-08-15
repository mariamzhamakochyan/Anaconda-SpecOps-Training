def square(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num ** 2)
    for i in range(0, len(new_lst)):
        for j in range(i + 1, len(new_lst)):
            if new_lst[i] > new_lst[j]:
               new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst
lst = [1, -2, 8, 9, 4, 3, 11]
print(square(lst)) 
               
