def arr(target, n):
    lst = []
    n = target[-1] +1
    for i in range(1, n):
        if i in target:
           lst.append("Push")
        else:
           lst.append("Push")
           lst.append("Pop")
    return lst
n = int(input("Enter a number: "))
target = [1,3]
print(arr(target, n))
