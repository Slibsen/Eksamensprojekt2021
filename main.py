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


choice = int(input("Vil du:\n1: Registrere bruger\n2: Have et udprint af brugere\nVenligt indtast 1 eller 2: "))
if choice == 1:
    name = input("Indtast venligst brugerens navn: ")
    initials = input("Indtast venligst brugerens initialer: ")
    email = input("Indtast venligt brugerens e-mail: ")
    password = input("Indtast venligst brugerens kodeord: ")
    userCode = input("Indtast venligst brugerens profilkode: ")
    if User.checkFile():
        print("Brugeren kan ikke oprettes, initialerne eller emailen er allerede i brug")
    else:
        print("Bruger oprettet")
        employee = initials
        employee = User(initials, name, password, userCode)
        User.registerUser(employee)
if choice == 2:
    print("yeehaw")
