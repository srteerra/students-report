# [piano[0], guitar[1], violin[2]]
# guitar and violin have maximum places to 12 people
subject = [[],[],[]]

def InsertStudent(nameVar, ageVar, groupVar, turnVar):
    students = [nameVar, ageVar, groupVar, turnVar]

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

InsertStudent(
    input("Enter a name: ").lower(),
    input("Enter an age: "),
    input("Enter a group: ").lower(),
    input("Enter a turn: ").lower()
)

print(subject[0])
print(subject[1])
print(subject[2])

