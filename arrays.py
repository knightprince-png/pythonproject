
courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accssing an element
print(courses[2])

#lopping through an array
for a in courses:
    print("course is",a)

#Adding a new element into an array
courses.append("laravel")
print(courses)

#deleting an element from an array
courses.remove("Cybersecurity")
print(courses)