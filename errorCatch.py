#Recursive funktion, prompter brugeren til at indtaste en kode mellem 1-6, og fortsætter med at prompte indtil at brugeren
#har indtastet en gyldig værdi. Returner derefter den nye kode, som bruges i userCreation
def newProfileCode(): 
    newAccessCode = int(input("Profilkode skal være mellem 1-6, prøv igen: "))

    if newAccessCode > 6 or newAccessCode < 0:
        newProfileCode()
    else:
        return int(newAccessCode)

#Recursive funktion - prompter brugeren til at indtaste initialer mellem 1-4 bogstaver
#Recursive hvis længden overskrider 4 eller er under 1. Eller hvis initialerne består af tal. 
#Returner gyldig værdi til userCreation
def newInitials():
    initials = input("Prøv igen: ")

    if len(initials) > 4 or len(initials) < 1:
        print("Initialerne skal bestå af max 4 og mindst 1 bogstav.")
        newInitials()
    elif containsDigit(initials):
        print("Initialerne må ikke indeholde tal.")
        return newInitials() #Her er jeg nødt til at bruge return statement af funktionen, 
        #da den ellers returner en tom string, hvis brugeren først har indtastet initialerne med et tal 
    else:
        return str(initials)

#Recursive funktion - Tjekker for gyldig email. Denne funktion kunne indeholde flere elementer, men jeg valgte at tjekke
#om emailen indeholder @.
#Returner gyldig værdi til userCreation
def newEmail():
    email = input("Denne email findes ikke, prøv igen: ")
    if "@" not in email:
        newEmail()
    else:
        return str(email)

def containsDigit(string):
    for char in string:
        if char.isdigit():
            return True