def selection_sort(list):
    for i in range(len(list)):
        min_index = list[i]
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
               min_index = list[j]
               if min_index != list[i]:
                  list[i], list[j] = list[j], list[i]
    return list
list = [5,4,3,2,1]
print(selection_sort(list))
