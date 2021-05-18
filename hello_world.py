# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Omar"
print("Hello", name, "!")	# with a comma
print("Hello "+ name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 23
str_name = str(name)
print("Hello", name, "!")	# with a comma
print("Hello "+ str_name + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
food_one = "burgers"
food_two = "pizza"
print("I love to eat {} and {}.".format(food_one, food_two)) # with .format()
print(f"I love to eat {food_one} and {food_two}.") # with an f string

if name is 23:
    print("WOW - is")

if name == 23:
    print("WOW - =")

for i in range(0,10,1):
    print(i)

for i in range(0,10): # same as
    print(i)

for i in range(10): # same as
    print(i)

cars = ['honda', 'toyota', 'chevy']
for car in cars:    # for every element in the array, do this
    print(car)

# disctionary
flowers={
    'daisy': 'white',
    'dandelion': 'yellow',
    'rose': 'red'
}
print(flowers['rose'])
for flower, color in flowers.items():
    print(flower, color)
for color in flowers:
    print(flowers[color])

# function
def add(x,y):
    return x+y

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)
print('')


x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   


capitals={
    'USA': 'Washington',
    'UK': 'London',
    'Germany': 'Berlin'
}
# another way to iterate through the keys
for key in capitals.keys():
     print("Using capitals.keys()", key)
#to iterate through the values
for val in capitals.values():
     print("Using capitals.values", val)
#to iterate through both keys and values
for key, val in capitals.items():
     print("Using Keys & Values", key, " = ", val)


# While Loops
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# While Loops with Else
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# for loop with break
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

# for loop with continue
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

# while loop with break
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

# 3/18/2021
# Create a function that takes a word as parameter and outputs the score of that work in scrabble
# 1 Point E, A, I, O, N, R, T, L, S, U
# 2 Points D, G
# # 3 Points B, C, M, P
# 4 Points F, H, V, W, Y
# 5 Points K
# # 8 Points J, X
# 10 Points Q, Z


# Ternary Operator

# traditional
stacks = 3
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
# ternary
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')


# Lambda (an element in a list:)
# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
my_list[2](5)

# Lambda (passed to another function as a callback)
# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# Lambda (stored in a variable)
add10 = lambda x: x + 10 # store lambda expression in a variable
add10(2)  # returns 12
add10(98) # returns 108

# Lambda (returned by another function)
def incrementor(num):
    start = num
    return lambda x: num + x


# Sequences (Slicing)
my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed

# Here are a few commonly used built-in functions for sequences:
# - max(sequence) returns the largest value in the sequence
# - sum(sequence) returns the sum of all values in sequence
# - map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# - min(sequence) returns the lowest value in a sequence.
# - sorted(sequence) returns a sorted list of the sequence's values

