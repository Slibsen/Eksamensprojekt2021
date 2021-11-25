from os import read


userFile = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"
class User:

    def __init__(self, initials, name, email, password, accessCode):
        self.initials = initials
        self.name = name
        self.email = email
        self.password = password
        self.accessCode = accessCode
        self.file = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"


    def checkFile(self):
        with open(self.file) as f:
            searchFile = f.readlines()
            for line in searchFile:
                if self.initials in line:
                    return True
                if self.email in f.read():
                    return True
            return False
    
    def registerUser(self):
        openFile = open(self.file, "a")
        add_to_file = f"{self.initials}:{self.name}:{self.email}:{hash(self.password)}:{self.accessCode}\n" #Hash funktionen forklaring: 
        openFile.writelines(str(add_to_file))
        openFile.close()

def printFile():
    with open(userFile) as f:
        readFile = f.readlines()
    for line in readFile:
        wordInLine = line.split(":")
        print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nKodeord: {wordInLine[3]}\nProfil: {wordInLine[4]}")

def getAccessLevel(initials):
    with open(userFile) as f:
        readFile = f.read()
    for line in readFile:
        wordInLine = line.split(":")
        if initials == wordInLine[0]:
            print(f"Profilkoden for denne medarbejder er: {wordInLine[4]}")
            f.close()
        else:
            print("Medarbejderen er ikke i systemet")

choice = int(input("Vil du:\n1: Registrere bruger\n2: Have et udprint af brugere\n"
                    "3: Se profil for specifik medarbejder\nVenligst indtast 1, 2 eller 3: "))
if choice == 1:
    name = input("Indtast venligst brugerens navn: ")
    initials = input("Indtast venligst brugerens initialer: ")
    email = input("Indtast venligt brugerens e-mail: ")
    password = input("Indtast venligst brugerens kodeord: ")
    accessCode = input("Indtast venligst brugerens profilkode: ")
    employee = initials
    employee = User(initials, name, email, password, accessCode)
    if employee.checkFile():
        print("Brugeren kan ikke oprettes, initialerne eller emailen er allerede i brug")
    else:
        print("Bruger oprettet")
        User.registerUser(employee)
if choice == 2:
    printFile()
if choice == 3:
    EmployeeInitials = input("Skriv initialerne på medarbejderen: ")
    getAccessLevel(EmployeeInitials)

