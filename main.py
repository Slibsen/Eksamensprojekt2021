import printOut
import createUser
def main():
    choice = int(input("Vil du:\n1: Registrere bruger\n2: Se et udprint af alle brugere\n"
                    "Venligst indtast 1 eller 2: "))
    if choice == 1:
        createUser.userCreation()
    
    if choice == 2:
        printOut.printFile()
    
    if choice != 1 and choice != 2:
        print("\nIkke gyldigt svar. Indtast venligst en af de viste svarmuligheder\n")
        main()


if __name__ == "__main__":
    main()

