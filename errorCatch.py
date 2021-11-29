#Recursive funktion, prompter brugeren til at indtaste en kode mellem 1-6, og fortsætter med at prompte indtil at brugeren
#har indtastet en gyldig værdi. Returner derefter den nye kode, som bruges i userCreation
def newProfileCode(): 
    newAccessCode = int(input("Indtast profilkode (1-6): "))

    if newAccessCode > 6 or newAccessCode < 1:
        print(f"{newAccessCode} er ikke en gyldig værdi.")
        return newProfileCode()
    else:
        return int(newAccessCode)

#Recursive funktion - prompter brugeren til at indtaste initialer mellem 1-4 bogstaver
#Recursive hvis længden overskrider 4 eller er under 1. Eller hvis initialerne består af tal. 
#Returner gyldig værdi til userCreation
def newInitials():
    initials = input("Indtast initialer: ")

    if len(initials) > 3 or len(initials) < 1:
        print("Initialerne skal bestå af max 4 og mindst 1 bogstav.")
        return newInitials()
    elif containsDigit(initials):
        print("Initialerne må ikke indeholde tal.")
        return newInitials() #Jeg nødt til at bruge return statement af alle funktionerne, 
        #da den ellers ender med at returnere None i txt filen
    else:
        return str(initials)

#Recursive funktion - Tjekker for gyldig email. Denne funktion kunne indeholde flere elementer, men jeg valgte at tjekke
#om emailen indeholder @.
#Returner gyldig værdi til userCreation
def newEmail():
    email = input("Indtast ny e-mail: ")
    if "@" not in email:
        print(f"{email} er ikke en gyldig e-mail.")
        return newEmail()
    else:
        return str(email)

#Recursive funktion - Tjekker om navnet indeholder tal.
def newName():
    name = input("Indtast navn: ")
    if containsDigit(name):
        print("Navnet kan ikke indeholde tal.")
        return newName()
    else:
        return str(name)

#Tjekker om en string indeholder et tal, så man kan give en error meddelelse i tilfælde af at
#f.eks. navn eller initialer indeholder tal 
def containsDigit(string):
    for char in string:
        if char.isdigit():
            return True