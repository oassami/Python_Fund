lst = [15, 4, 99, 87, 40, 6, 64, 0, 66, -1, 28]

print(lst, '\n')


for j in range(len(lst)):
    min = j
    for i in range(j+1, len(lst)):
        if lst[i] < lst[min]:
            min = i
    # if j != min:
    lst[j], lst[min] = lst[min], lst[j]



print(lst)
# Testing making chages to this too!