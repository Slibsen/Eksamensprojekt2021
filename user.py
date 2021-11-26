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

    def accessLevel(self):
        print(self.accessCode)

def getAccessLevel(initials):
    with open(userFile) as f:
        readFile = f.readlines()
    for line in readFile:
        wordInLine = line.split(":")
        try:
            if initials in wordInLine[0]:
                print(f"Profilkoden for denne medarbejder er: {wordInLine[4]}")
            if wordInLine[4] == 1:
                print("Dette er højeste niveau, medarbejderen har adgang til alle systemer")
            if wordInLine[4] == 2:
                print("Brugeren har adgang til de fleste systemer")
            if wordInLine[4] == 3:
                print("Brugeren har adgang til mange af systemerne")
            if wordInLine[4] == 4:
                print("Brugeren har adgang til nogle systemer")
            if wordInLine[4] == 5:
                print("Brugeren har adgang til få systemer")
            if wordInLine[4] == 6:
                print("Brugeren har ikke adgang til nogle af systemerne")
        except:
            print("Medarbejderen er ikke i systemet")
