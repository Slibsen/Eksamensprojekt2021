from user import User
import errorCatch

#Tager user inputs, som derefter kan bruges til at lave en employee instance
def userCreation():
    name = errorCatch.newName()
    initials = errorCatch.newInitials()
    email = errorCatch.newEmail()
    password = input("Indtast venligst brugerens kodeord: ")
    accessCode = errorCatch.newProfileCode()
    employee = User(initials, name, email, password, accessCode)


#Tjekker om brugeren allerede er i systemet, hvis ikke, så oprettes brugeren i txt filen
    if employee.existingUser():
        print("Brugeren kan ikke oprettes, initialerne eller emailen er allerede i brug")
    else:
        print("Bruger oprettet")
        User.registerUser(employee)