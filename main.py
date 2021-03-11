# Turn A: Thursday - Tuesday (5pm-7pm)
# Turn B: Saturday (8am-1pm)

# [piano[0], guitar[1], violin[2]]
subject = [[],[],[]]

class Fill:

    def __init__(self, nameVar, ageVar, groupVar, turnVar):
        students = [nameVar, ageVar, groupVar, turnVar]

        # guitar and violin have maximum places to 12 people
        if(groupVar.lower() == "piano"):
            if(len(subject[0]) < 12):
                subject[0].append(students)
            else:
                print("The piano class is already full")
        elif(groupVar.lower() == "guitar"):
            if(len(subject[1]) < 12):
                subject[1].append(students)
            else:
                print("The guitar class is already full")
        elif(groupVar.lower() == "violin"):
            subject[2].append(students)

class insertstudent:

    def __init__(self):
        self.name = input("Enter a name: ").lower()
        self.age = input("Enter an age: ")
        self.group = input("Enter a group: ").lower()
        self.turn = input("Enter a turn: ").lower()

        Fill(self.name, self.age, self.group, self.turn)

class __init__:
    insertstudent()

print(subject[0])
print(subject[1])
print(subject[2])

