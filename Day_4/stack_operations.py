def stack(target, n):
    list = []
    for i in range(1, n + 1):
        if i > target[-1]:
           break
        list.append("Push")
        if i not in target:
           list.append("Pop")
    return list
target = [1,2]
n = 4
print(stack(target, n))
