import os.path

def getUserInput():
    exists = False
    readInput = True
    while not exists and readInput:
        response = input("Enter file name or 'q' to exit: ")

        if response == 'q':
            readInput = False
            return None, readInput
        else:
            exists = os.path.isfile(response)
            if not exists:
                print("Invalid file name")
    
    return response, readInput