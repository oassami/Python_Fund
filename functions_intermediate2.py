#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

print('\n-------- END OF #1 ------------------------\n')

#2. Iterate Through a List of Dictionaries
def iterateDictionary(studentsList):
    for student in studentsList:
        fName_lName = ''
        for key, val in student.items():
            fName_lName += key + ' - ' + val + ', '
        print(fName_lName[:len(fName_lName)-2])
    return

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(students) 

print('\n-------- END OF #2 ------------------------\n')


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for indx in some_list:
        for key, val in indx.items():
            if key == key_name:
                print(val)
    return
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print('\n-------- END OF #3 ------------------------\n')

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key.upper())
        for indx in val:
            print(indx)
        print('\n')
    return

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

print('\n-------- END OF #4 ------------------------\n')
