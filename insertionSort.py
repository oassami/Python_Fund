lst = [15, 4, 99, 87, 40, 6, 64, 0, 66, -1, 28]
print(lst, '\n')

def shift(crnt, tmpList):
    j = crnt - 1
    while tmpList[crnt] < tmpList[j]:
        tmpList[crnt], tmpList[j] = tmpList[j], tmpList[crnt]
        if j == 0:
            break
        j -= 1
        crnt -= 1
    return tmpList

for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        lst = shift(i, lst)
    print('iteration #', i, lst)

