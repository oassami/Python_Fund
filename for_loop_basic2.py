#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(a):
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = "big"
    return a
x = biggie_size([-1, 3, 5, -5])
print(x)

#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(a):
    count = 0
    for i in range(len(a)):
        if a[i] > 0:
            count += 1
    a[len(a)-1] = count
    return a
x = count_positives([1,6,-4,-2,-7,-2])
print(x)

#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum
x = sum_total([6,3,-2])
print(x)

#4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum / len(a)
x = average([1,2,3,4])
print(x)

#5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(a):
    return len(a)
x = length([37,2,1,-9])
print(x)

#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have 
# the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(a):
    if len(a) == 0:
        return False
    min = a[0]
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min
x = minimum([37,2,1,-9])
print(x)
x = minimum([])
print(x)

#7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function 
# return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(a):
    if len(a) == 0:
        return False
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max
x = maximum([37,2,1,-9])
print(x)
x = maximum([])
print(x)

#8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum 
# and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(a):
    newDict = {}
    sumTotal = 0
    average = 0
    minimum = a[0]
    maximum = a[0]
    length = len(a)
    for i in range(len(a)):
        sumTotal += a[i]
        if a[i] < minimum:
            minimum = a[i]
        if a[i] > maximum:
            maximum = a[i]
    average = sumTotal / length
    newDict['sumTotal'] = sumTotal
    newDict['average'] = average
    newDict['minimum'] = minimum
    newDict['maximum'] = maximum
    newDict['length'] = length
    return newDict
x = ultimate_analysis([37,2,1,-9])
print(x)

#9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(a):
    for i in range(int(len(a)/2)):
        temp = a[i]
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = temp
    return a
x = reverse_list([3,1,8,10,-5,6,23])
print(x)
