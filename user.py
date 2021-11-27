import errorCatch
class User:
    def __init__(self, initials, name, email, password, accessCode):
        self.initials = initials
        self.name = name
        self.email = email
        self.password = password
        self.accessCode = accessCode
        self.file = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"

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
            
    def registerUser(self):
        openFile = open(self.file, "a")
        add_to_file = f"{self.initials}:{self.name}:{self.email}:{hash(self.password)}:{self.accessCode}\n" #Hash funktionen forklaring: 
        openFile.writelines(str(add_to_file))
        openFile.close()

    def profileOutOfBounds(self):
        if self.accessCode < 6 and self.accessCode > 0:
            return False
        else: 
            return True
    
    def initialsOutOfBounds(self):
        if len(self.initials) <= 4 and len(self.initials) > 0 and not errorCatch.containsDigit(self.initials):
            return False
        else:
            return True
    
    def invalidEmail(self):
        if "@" in self.email:
            return False
        else:
            return True 
