def insertion_sort(list):
    i = 1
    while i < len(list):
          j = i
          while j > 0 and list[j - 1] > list[j]:
                list[j-1], list[j] = list[j], list[j - 1] 
                j = j - 1
          i = i + 1
    return list
list = [5,4,3,2,1]
print(insertion_sort(list))   
