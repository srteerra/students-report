# [piano[0], guitar[1], violin[2]]
# guitar and violin have maximum places to 12 people
subject = [[],[],[]]

def InsertStudent(nameVar, ageVar, groupVar, turnVar):
    students = [nameVar, ageVar, groupVar, turnVar]

    if(groupVar.lower() == "piano"):
        subject[0].append(students)
    elif(groupVar.lower() == "guitar"):
        subject[1].append(students)
    elif(groupVar.lower() == "violin"):
        subject[2].append(students)


InsertStudent(
    input("Enter a name: "),
    input("Enter an age: "),
    input("Enter a group: "),
    input("Enter a turn: ")
)

print(subject[0])
print(subject[1])
print(subject[2])

