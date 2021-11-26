import printOut
import createUser

choice = int(input("Vil du:\n1: Registrere bruger\n2: Have et udprint af brugere\n"
                    "Venligst indtast 1 eller 2: "))
if choice == 1:
    createUser.userCreation()
    
if choice == 2:
    printOut.printFile()


