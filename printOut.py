#Printer txt filen ud på en læsevenlig måde i terminalen
userFile = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"
def printFile():
    with open(userFile) as f:
        readFile = f.readlines()
    for line in readFile:
        wordInLine = line.split(":")
        print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nKodeord: {wordInLine[3]}\nProfil: {wordInLine[4]}")

        if int(wordInLine[4]) == 1:
            print(f"{wordInLine[1]} har det højeste sikkerhedsniveau og kan tilgå alle systemer\n")
        if int(wordInLine[4]) == 2:
            print(f"{wordInLine[1]} har et højt sikkerhedsniveau og kan tilgå de fleste systemer\n")
        if int(wordInLine[4]) == 3:
            print(f"{wordInLine[1]} har et standard sikkerhedsniveau og kan tilgå mange systemer\n")
        if int(wordInLine[4]) == 4:
            print(f"{wordInLine[1]} har et begrænset sikkerhedsniveau og kan tilgå nogle systemer\n")
        if int(wordInLine[4]) == 5:
            print(f"{wordInLine[1]} har et meget begrænset sikkerhedsniveau og kan tilgå få systemer\n")
        if int(wordInLine[4]) == 6:
            print(f"{wordInLine[1]} har ikke nogen sikkerhedsgodkendelse og kan dermed ikke tilgå nogle systemer\n")
        f.close()
