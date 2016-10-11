students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
fullName = ""

for student in students:
    for name in student.values():
        fullName += name + " " #ooh clever, i see what you did there
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
	# fullName = student.values()
	# print "{} {}".format(fullName[0],fullName[1]) #this works
	print fullName[0], fullName[1]
	#you could also do it this way and then it's all in one line
	# fullName = ""

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

#Leo,
#Really nice job here! You're printing the key and avoiding repeating your code. To make your print statement a little prettier you could make a variable like "length" and outsource the addition of lengths I suppose, but that's just about all I can think of to nitpick. Ooh wait, actually to make it exactly like the specifications you can use .upper() to uppercase all the letters.
#Well done!
