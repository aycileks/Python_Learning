# GlobalAIHub Python Introduction Project

myName = "John"
mySurname = "Doe"
entryChances = 3
courses = ["Python", "C++", "JavaScript", "Basic", "Pascal"]
listGradeDic = {}


def status(co, les):
    if co <= 3 and 3 <= les <= 5:
        stat = "Ok"
    else:
        stat = "NOk"
        print("You failed the class...")
    return stat


while entryChances > 0:
    name = str(input("Please enter your name : "))
    surname = str(input("Please enter your surname : "))
    if name == myName and surname == mySurname:
        print("Welcome, {}.".format(name))
        print("\nAvailable courses are: ")
        i = 0
        while i < len(courses):
            print(i + 1, " ", courses[i])
            i += 1
        course = int(input("How many courses (max 3) would you like to take? : "))
        lesson = int(
            input("How many lessons (min 3, max 5) would you like to take? : ")
        )
        if status(course, lesson) == "Ok":
            courseSelect = int(
                input("Please choose the number of the course you take : ")
            )
            scoreMid = int(input("Please enter your mid-term exam score : "))
            scoreFin = int(input("Please enter your final exam score : "))
            scorePro = int(input("Please enter your project score : "))
            print(
                "The calculation is based on the formula Midterm = %30 + Final = %50 + Project = %20"
            )
            listGradeDic = {
                "Mid-term": scoreMid,
                "Final": scoreFin,
                "Project": scorePro,
            }
            average = (
                listGradeDic["Mid-term"] * 0.3
                + listGradeDic["Final"] * 0.5
                + listGradeDic["Project"] * 0.2
            )
            print("Your average is : ", average)
            if average >= 90:
                print("Congrats! Your grade is AA")
                exit(0)
            elif average >= 70 and average < 90:
                print("Your grade is BB")
                exit(0)
            elif average >= 50 and average < 70:
                print("Your grade is CC")
                exit(0)
            elif average >= 30 and average < 50:
                print("Your grade is DD")
                exit(0)
            elif average < 90:
                print("Your grade is FF")
                print("You failed the class...")
                exit(0)
        else:
            status
            exit(0)
    else:
        entryChances -= 1
        print(name + " " + surname + " is not an authorised user! Please try again.")
print("You have reached your max attemts! Please try again later.")
exit(0)
