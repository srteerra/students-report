# Turn A: Thursday - Tuesday (5pm-7pm)
# Turn B: Saturday (8am-1pm)

# [piano[0], guitar[1], violin[2]]
subject = [[],[],[]]

class Fill:

    def __init__(self, nameVar, ageVar, groupVar, turnVar):
        students = [nameVar, ageVar, groupVar, turnVar]

        # guitar and violin have maximum places to 12 people
        if(groupVar.lower() != "piano" and groupVar.lower() != "guitar" and groupVar.lower() != "violin"):
            print("You have a mistake in the group you selected, please enter a valid group")
            insertstudent()
        else:
            if(groupVar.lower() == "piano"):
                if(len(subject[0]) < 12):
                    subject[0].append(students)
                else:
                    print("The piano class is already full")
                    menu()
            elif(groupVar.lower() == "guitar"):
                if(len(subject[1]) < 12):
                    subject[1].append(students)
                else:
                    print("The guitar class is already full")
                    menu()
            elif(groupVar.lower() == "violin"):
                subject[2].append(students)

            cont = input("Add another student? [Y/N]: ")
            if(cont.upper() == "Y"):
                insertstudent()
            elif(cont.upper() == "N"):
                menu()
            else:
                print("Your selection is not valid")
                menu()

class insertstudent:

    def __init__(self):
        self.name = input("Enter a name: ").lower()
        self.age = input("Enter an age: ")
        self.group = input("Enter a group: ").lower()
        self.turn = input("Enter a turn: ").lower()

        Fill(self.name, self.age, self.group, self.turn)

class allstudents:

    def __init__(self):
        print(*subject[1], sep = "\n")
        print(*subject[2], sep = "\n")
        print(*subject[0], sep = "\n")

        cont = input("Continue? [Y]: ")
        if(cont.upper() == "Y"):
            menu()
        else:
            menu()

class groupreport:

    def __init__(self):

        print("--------------------------+")
        if(len(subject[0]) >= 3):
            pianoStatus = " [Open] "
        else:
            pianoStatus = " [Cancelled] "
        print("\nPiano Students:", len(subject[0]), pianoStatus)
        print(*subject[0], sep = "\n")
        print("--------------------------+")
        if(len(subject[1]) >= 5):
            guitarStatus = " [Open] "
        else:
            guitarStatus = " [Cancelled] "
        print("\nGuitar Students:", len(subject[1]), guitarStatus)
        print(*subject[1], sep = "\n")
        print("--------------------------+")
        if(len(subject[2]) >= 5):
            violinStatus = " [Open] "
        else:
            violinStatus = " [Cancelled] "
        print("\nViolin Students:", len(subject[2]), violinStatus)
        print(*subject[2], sep = "\n")
        print("--------------------------+")

        cont = input("Continue? [Y]: ")
        if(cont.upper() == "Y"):
            menu()
        else:
            menu()

class turnreport:

    def __init__(self):
        

        cont = input("Continue? [Y]: ")
        if(cont.upper() == "Y"):
            menu()
        else:
            menu()


class menu:

    def __init__(self):
        print("---------- Menu ----------\n")
        print("[1] Add new student")
        print("[2] Show all the students")
        print("\n---Reports:")
        print("[3] Generate a report of Group")
        print("[4] Generate a report of Turn")
        print("[5] Generate a report of Students")

        selection = input("\nEnter your option: ")

        if(selection == "1"):
            insertstudent()
        elif(selection == "2"):
            allstudents()
        elif(selection == "3"):
            groupreport()
        elif(selection == "4"):
            turnreport()

class __init__:
    menu()

