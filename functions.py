# Built-in functions/STANDARD LIBRARY FUNCTION

y=max(67,45,40,34,12)
print("the maximum value is",y)

x=min(45,12,25,13,80)
print("the minimum value is",x)

# user defined function

def name():
    print("felix")

name() #calling a function

def multiply():
    x = 20
    y = 12
    print(x*y)
multiply()


# parameter and arguments
def add(a, b):

    print(a+b)
add(45, 89)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)

employee("mark","male","CEO","Ksh560000",67)



# WRITE A PROGRAM THAT DISPLAYS DETAILS OF FIVE STUDENTS
#FULL NAME,AGE,COURSE TAKEN,GENDER

def student(FullName,Age,Coursetaken,Gender):
    print(FullName,Age,Coursetaken,Gender)

student("Felix",18,"MIT","Male")
student("John",22,"MIT","Male")
student("Alex",19,"MIT","Male")
student("Melinda ",20,"MIT","Female")
student("Alexis",19,"MIT","Female")