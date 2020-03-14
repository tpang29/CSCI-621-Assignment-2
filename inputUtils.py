import os.path

def verifyInputFile():
    fileHandle = input("Enter file name: ")
    exists = os.path.isfile(fileHandle)
    while not exists:
        fileHandle = input("Invalid file name\nEnter file name: ")
        exists = os.path.isfile(fileHandle)
    
    return fileHandle

def checkToContinue():
    runProgram = True
    isValidResposne = False

    while not isValidResposne:
        response = input("Do you wish to continue? Enter 'y' or 'n': ")
        
        if response == "y":
            isValidResposne = True
            runProgram = True
        elif response == "n": 
            isValidResposne = True
            runProgram = False
        else: 
            isValidResposne = False
            runProgram = False
    
    return runProgram