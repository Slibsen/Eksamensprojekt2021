from os import close, read
from user import User
import printOut
userFile = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"
def printFile():
    with open(userFile) as f:
        readFile = f.readlines()
    for line in readFile:
        wordInLine = line.split(":")
        print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nKodeord: {wordInLine[3]}\nProfil: {wordInLine[4]}")

choice = int(input("Vil du:\n1: Registrere bruger\n2: Have et udprint af brugere\n"
                    "3: Se profil for specifik medarbejder\nVenligst indtast 1, 2 eller 3: "))
if choice == 1:
    name = input("Indtast venligst brugerens navn: ")
    initials = input("Indtast venligst brugerens initialer (Max 4 bogstaver): ")
    if len(initials) >= 4:
        print("")
    email = input("Indtast venligst brugerens e-mail: ")
    password = input("Indtast venligst brugerens kodeord: ")
    accessCode = input("Indtast venligst brugerens profilkode (Ml. 1-6): ")
    
    employee = User(initials, name, email, password, accessCode)
    if employee.checkFile():
        print("Brugeren kan ikke oprettes, initialerne eller emailen er allerede i brug")
    else:
        print("Bruger oprettet")
        User.registerUser(employee)
    if not employee.isProfileOK():
        print("Profile ikke ok, skal være ml 1-6")
    
if choice == 2:
    printOut.printFile()
#if choice == 3:
    #EmployeeInitials = input("Skriv initialerne på medarbejderen: ")
    #User(employee).accessLevel()

