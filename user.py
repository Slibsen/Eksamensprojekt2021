class User:
    def __init__(self, initials, name, email, password, accessCode):
        self.initials = initials
        self.name = name
        self.email = email
        self.password = password
        self.accessCode = accessCode
        self.file = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"

#Tjekker om brugeren allerede er i txt filen
    def existingUser(self):
        with open(self.file) as f:
            searchFile = f.readlines()
            for line in searchFile:
                wordInLine = line.split(":")
                if str(self.initials) == wordInLine[0]:
                    return True
                if self.email == wordInLine[2]:
                    return True
            f.close()
            return False

#Registrere brugeren i txt filen
#Hash funktionen: Omdanner password til en integer værdi. Funktionen indeholder også en salt key, som gør at selvom
#flere brugere har samme password, vil de ikke have samme hashkode. 
    def registerUser(self):
        openFile = open(self.file, "a")
        add_to_file = f"{self.initials}:{self.name}:{self.email}:{hash(self.password)}:{self.accessCode}\n" 
        openFile.writelines(str(add_to_file))
        openFile.close()
