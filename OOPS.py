# Class is the blueprint of an object


# class Car:
#     name = "Audi"
#     wheels = 4
#     door = 4
#     engine = "2500cc"
#     Type = "Petrol"

# c = Car()
# c.door=2
# print(c.door)
# print(c.engine)

# class Phone:
#     model = "Redmi Note 9 pro max"
#     RAM = "8GB"
#     ROM = "256GB"
    # It wont work if you don't give self parameter
#     def calling(self,name):
#         print("calling to ",name)
#     def camera(self):
#         print("open camera")
#     def close(self):
#         print("Close the last open app")
 
# p = Phone()
# p.camera()
# p.calling("sarthak")
# p.close()

# class Car:
#     def work(self,press):
#         if press ==1:
#             print("Car is start")
#         elif press==2:
#             print("Car is moving")
#         elif press==0:
#             print("Car is stopped")
            
# c = Car()
# c.work(1)

# class Phone:
#     def calling(self,press):
#         if press==1:
#             print("calling mom")
#         elif press ==2:
#             print("calling dad")
#         elif press ==3:
#             print("calling brother")

#     def working(self,press):
#         if press==1:
#             print("Open camera")
#         elif press ==2:
#             print("Open photo")
#         elif press ==3:
#             print("open pubG")

# phone1 = Phone()
# phone1.calling(1)

# phone2 = Phone()
# phone2.working(1)

# class Student:
#     def avg_score(self,maths,english,hindi,science):
#         self.maths = maths
#         self.english = english
#         self.hindi  = hindi 
#         self.science = science
#         return (self.maths+self.english+self.hindi+self.science)/4
    
# s = Student()
# print(s)
# print(s.avg_score(44,45,48,49))

# create a class marksheet :
# create a instance only to asign subjects and mention 4 subjects
# add another instance named it total_score
# add another instance named it min_score
# add another instance named it max_score


# class Marksheet:
#     def subject(self,maths,english,hindi,science):
#           self.maths = maths
#           self.english = english
#           self.hindi  = hindi 
#           self.science = science

#     def total_score(self):
#           return (self.maths+self.english+self.hindi+self.science)
    
#     def min_score(self):
#           return min(self.maths,self.english,self.hindi,self.science)

#     def max_score(self):
#           return max(self.maths,self.english,self.hindi,self.science)

# m1 = Marksheet()
# m1.subject(98,87,97,76)
# print(m1.total_score())
# print(m1.min_score())
# print(m1.max_score())

# create a class college:
#     add instance name it "details" like:np. of class,location,no. of teacher
# add instance name it return no of classes 
# add instance name it return no of teachers
# add instance name it return location of college

# class College:
#     def details(self,no_of_class,location,no_of_teacher):
#         self.no_of_class = no_of_class
#         self.loc = location
#         self.no_of_teacher = no_of_teacher

#     def classes(self):
#         return self.no_of_class
#     def location(self):
#         return self.loc
#     def teachers(self):
#         return self.no_of_teacher
    
# class1 = College()
# class1.details(12,"Nepal",20)
# print(class1.classes())
# print(class1.location())
# print(class1.teachers())

# class Cylinder:
#     def details(self,r,h):
#         self.pie = 3.14159
#         self.r = r
#         self.h = h 
#     def TSA(self):
#         return 2*self.pie*self.r*(self.r+self.h)  
#     def volume(self):
#         return self.pie*self.r*self.r*self.h  

# c1 = Cylinder()
# c1.details(7,20)
# print(c1.TSA())

# create class for cone 
# instance = TSA = pie *r(r+l)
# instance = CSA = pie *r*l

# class Cone:
#       def details(self,r,l):
#         self.pie = 3.14159
#         self.r = r
#         self.l = l
#       def TSA(self):
#         return self.pie*self.r*(self.r+self.l)  
#       def CSA(self):
#         return self.pie*self.r*self.l 

# c1 = Cone()
# r = int(input("Enter value of r"))
# h = int(input("Enter value of h"))
# c1.details(r,h)
# c1.details(7,10)
# return(c1.CSA())
                    # Constructor 
# class Car:
#   def __init__(self,hp,name,door,type):
#     self.hp = hp
#     self.name = name
#     self.door = door
#     self.type = type 

#   def details(self):
#     print("hp of the car is ",self.hp)  
#     print("name of the car is ",self.name)  
#     print("no. of door of the car is ",self.door)  
#     print("type of the car is ",self.type)  

# c1 = Car(25000,"BMW",4,"Petrol")
# c1.details()

# class Bank:
#     def __init__(self,amount):
#         self.amount = amount
#     def debit(self,cur_amount):
#         self.amount-=cur_amount
#         print("{} is debited from your bank account".format(cur_amount))
#         print("your bank balance is {}".format(self.amount))
#     def credit(self,cur_amount):
#         self.amount+=cur_amount
#         print("{} is credited from your bank account".format(cur_amount))
#         print("your bank balance is {}".format(self.amount))
        
# account1 = Bank(0)
# account1.credit(500)
# account1.debit(00)

# Questions 
# Q.1 Define a python class student with attributes name,age and grade and a method is_passing() to check if the student's grade is passing (>=60). 

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade 
    def is_passing(self):
        if(self.grade>=60):
            print("{} of age {} passed with marks {}".format(self.name,self.age,self.grade))
        else:
            print("{} of age {} failed with marks {}".format(self.name,self.age,self.grade))

student1 = Student("Bivek",20,99)
student1.is_passing()
student1 = Student("Abhideep",17,35)
student1.is_passing()