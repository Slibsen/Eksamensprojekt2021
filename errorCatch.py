def newProfileCode():
    newAccessCode = int(input("Profilkode skal være mellem 1-6, prøv igen: "))

    if newAccessCode > 6 or newAccessCode < 0:
        newProfileCode()
    else:
        return int(newAccessCode)

def newInitials():
    initials = input("Initialerne skal bestå af max 4 og mindst 1 bogstav. Prøv igen: ")

    if len(initials) > 4 or len(initials) < 0:
        newInitials()
    else:
        return str(initials)

def newEmail():
    email = input("Denne email findes ikke, prøv igen: ")
    if "@" not in email:
        newEmail()
    else:
        return str(email)
