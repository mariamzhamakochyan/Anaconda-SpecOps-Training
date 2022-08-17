def bubble_sort(list):
    for i in range(0, len(list)):
        swap = False
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
               list[j], list[j + 1] = list[j + 1], list[j]
               swap = True
        if swap == False:
           break
    return list
list = [1,9,5,6,0,2]
print(bubble_sort(list))
