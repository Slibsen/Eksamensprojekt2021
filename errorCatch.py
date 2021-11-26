def newProfileCode():
    newAccessCode = int(input("Profilkode skal være mellem 1-6, prøv igen: "))

    if newAccessCode > 6 or newAccessCode < 0:
        newProfileCode()
    else:
        return int(newAccessCode)

def newInitials():
    initials = input("Initialerne må kun bestå af 4 bogstaver. Prøv igen: ")

    if len(initials) > 4 or len(initials) < 0:
        newInitials()
    else:
        return str(initials)