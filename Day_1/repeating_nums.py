def rep_nums(lst):
    dict = {}
    keys = dict.keys()
    for num in lst:
        if num in keys:
           dict[num] += 1
        else:
           dict.update({num:1})
    return dict
lst = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print(rep_nums(lst))

