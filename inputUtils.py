import os.path

def getUserInput():
    exists = False
    readInput = True
    while not exists and readInput:
        fileHandle = input("Enter file name or 'q' to exit: ")

        if fileHandle == 'q':
            readInput = False
            return None, readInput
        else:
            print("Invalid file name")
            exists = os.path.isfile(fileHandle)
    
    return fileHandle, readInput