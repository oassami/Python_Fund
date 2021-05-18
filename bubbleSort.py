lst = [15, 4, 99, 87, 40, 48, 6, 64, 66, 28]
print(lst, '\n')
for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst, '\n')
