userFile = "/Users/ellie/Desktop/IT-Arkitektur/Afleveringer/Brugerfil.txt"
def printFile():
    with open(userFile) as f:
        readFile = f.readlines()
    for line in readFile:
        wordInLine = line.split(":")
        print(f"Initialer: {wordInLine[0]}\nNavn: {wordInLine[1]}\nEmail: {wordInLine[2]}\nKodeord: {wordInLine[3]}\nProfil: {wordInLine[4]}")
        f.close()