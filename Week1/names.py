students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
fullName = ""

for student in students:
    for name in student.values():
        fullName += name + " "
    print fullName
    fullName = ""

#Or

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
fullName = ""
print "\nMethod 2:"
for student in students:
    fullName = student.values()
    print "{} {}".format(fullName[0],fullName[1])
    fullName = ""

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
print ""
for key,data in users.items():
    print key
    index = 1
    for value in data:
        print "{} - {} {} - {}".format(index, value["first_name"], value["last_name"], len(value["first_name"]) + len(value["last_name"]))
        index += 1
