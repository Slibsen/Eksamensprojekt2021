from user import User
import errorCatch

def userCreation():
    name = input("Indtast venligst brugerens navn: ")
    initials = input("Indtast venligst brugerens initialer (Max 4 bogstaver): ")
    email = input("Indtast venligst brugerens e-mail: ")
    password = input("Indtast venligst brugerens kodeord: ")
    accessCode = int(input("Indtast venligst brugerens profilkode (Ml. 1-6): "))
    employee = User(initials, name, email, password, accessCode)

#If/elif statements tjekker for relevante inputs errors
    if employee.initialsOutOfBounds() and employee.profileOutOfBounds() and employee.invalidEmail():
        employee = User(errorCatch.newInitials(), name, errorCatch.newEmail(), password, errorCatch.newProfileCode())

    elif employee.initialsOutOfBounds() and employee.profileOutOfBounds():
        employee = User(errorCatch.newInitials(), name, email, password, errorCatch.newProfileCode())

    elif employee.initialsOutOfBounds() and employee.invalidEmail():
        employee = User(errorCatch.newInitials(), name, errorCatch.newEmail(), password, accessCode)

    elif employee.invalidEmail() and employee.profileOutOfBounds():
        employee = User(initials, name, errorCatch.newEmail(), password, errorCatch.newProfileCode())

    elif employee.initialsOutOfBounds():
        employee = User(errorCatch.newInitials(), name, email, password, accessCode)

    elif employee.profileOutOfBounds():
        employee = User(initials, name, email, password, errorCatch.newProfileCode())
    
    elif employee.invalidEmail():
        employee = User(initials, name, errorCatch.newEmail(), password, accessCode)

    if employee.existingUser():
        print("Brugeren kan ikke oprettes, initialerne eller emailen er allerede i brug")
    else:
        print("Bruger oprettet")
        User.registerUser(employee)