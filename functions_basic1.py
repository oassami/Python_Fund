#1
def a():
    return 5
print(a())
# output: 5

print("--- #1 is Complete ---") # code separator

#2
def a():
    return 5
print(a()+a())
# output: 10

print("--- #2 is Complete ---") # code separator

#3
def a():
    return 5
    return 10
print(a())
# output: 5

print("--- #3 is Complete ---") # code separator


#4
def a():
    return 5
    print(10)
print(a())
# output: 5

print("--- #4 is Complete ---") # code separator


#5
def a():
    print(5)
x = a()
print(x)
# output: 5, nothing to print (x has no value)

print("--- #5 is Complete ---") # code separator


#6
def a(b,c):
    print(b+c)
# print(a(1,2) + a(2,3))
# Output: 3, 5, error (function doesn't return anything to add)

print("--- #6 is Complete ---") # code separator

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# output: "25"

print("--- #7 is Complete ---") # code separator

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# output: 100, 10

print("--- #8 is Complete ---") # code separator

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# output: 7, 14, 21

print("--- #9 is Complete ---") # code separator

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# output: 8

print("--- #10 is Complete ---") # code separator

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# output: 500, 500, 300, 500

print("--- #11 is Complete ---") # code separator

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# output: 500, 500, 300, 500

print("--- #12 is Complete ---") # code separator

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# output: 500, 500, 300, 300

print("--- #13 is Complete ---") # code separator

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# output: 1, 3, 2

print("--- #14 is Complete ---") # code separator

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# output: 1, 3, 5, 10

print("--- #15 is Complete ---") # code separator

