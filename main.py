# [piano[], guitar[], violin[]]
# guitar and violin have maximum places to 12 people
subject = [[] , [] , []]

class Student:
    def __init__(self, name, age, group, turn):
        self.name = name
        self.group = group
        self.age = age
        self.turn = turn

    def enter(self):
        self.name = print("Enter a new student: ")
        self.age = print("Enter the age of the student: ")
        self.group = print("Enter the group of the student: ")
        self.turn = print("Enter the turn of the student: ")

newstudent = input("Enter a new student: ")

