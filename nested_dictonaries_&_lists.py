
# Update Values in Dictionaries and Lists
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
x[1][0]= 15
students[0].update({'last_name':'Bryant'})
sports_directory['soccer'][0]= "Andres"
z[0].update({'y': 30})

# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for person in some_list:
        for key, val in person.items():
            print(key, "-" ,val)
iterateDictionary(students)


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for flnames in some_list:
        print (flnames[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)



# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for dojoinfo in some_dict:
        print(len(dojo[dojoinfo]))
        print(dojoinfo)
        print(dojo[dojoinfo])
printInfo(dojo)