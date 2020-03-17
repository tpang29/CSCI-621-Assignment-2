# DECLARE VARIABLES
inputIndex = 0
dValue = 0
eValue = 0
nextSymbol = ""
userInput = ""
EOL = False
succeeded = True

# RESET VARIABLES
def resetVariables():
    global userInput, inputIndex, nextSymbol, dValue, eValue, succeeded, EOL
    inputIndex = 0
    dValue = 0
    eValue = 0
    nextSymbol = ""
    userInput = ""
    EOL = False
    succeeded = True

# GET_NEXT_SYMBOL
def getNextSymbol():
    global inputIndex, nextSymbol, userInput, EOL

    # while inputIndex < len(userInput) - 1 and userInput[inputIndex] == " ": # original code
    while inputIndex < len(userInput) - 1 and userInput[inputIndex] == " ": # handles input file where each line ends in new line char
        inputIndex += 1
    
    # if inputIndex < len(userInput) - 1: # original code
    if inputIndex < len(userInput) - 1: # handles input file where each line ends in new line char
        nextSymbol = userInput[inputIndex]
        inputIndex += 1
    else:
        EOL = True
        return

# RDPARSER
def rdparser(inputLine):
    global succeeded, userInput
    # while (True):
    resetVariables()
    succeeded = True
    # getInputLine()
    userInput = inputLine
    getNextSymbol()
    elist()
    if succeeded:
        print("success")
    else:
        print("failure")

# ELIST
def elist():
    e()
    if succeeded:
        elistTail()

# ELIST_TAIL
def elistTail():
    global inputIndex, userInput, succeeded, eValue
    if EOL:
        print(eValue)
    else:
        if nextSymbol == ",":
            print(eValue, end=" ")
            getNextSymbol()
            elist()
        else:
            succeeded = False

# E
def e():
    nValue = 0
    nValue = n(nValue)
    if succeeded:
        etail(nValue)

# ETAIL
def etail(nValue):
    global inputIndex, userInput, eValue, succeeded
    if not (nextSymbol == "," or EOL):
        if nextSymbol == "^":
            getNextSymbol()
            e()
            eValue = nValue ** eValue
        else:
            succeeded = False
    else:
        eValue = nValue

# N
def n(nValue):
    d()
    if succeeded:
        nValue = (nValue * 10) + dValue
        return ntail(nValue)

# NTAIL
def ntail(nValue):
    global inputIndex, userInput, nextSymbol
    if not ((nextSymbol == "^" or nextSymbol == ",") or EOL):
        nValue = n(nValue)
    return nValue

# D
def d():
    global dValue, nextSymbol, succeeded
    if nextSymbol.isdigit():
        dValue = int(nextSymbol)
        getNextSymbol()
    else:
        succeeded = False

# Part of pseudocode but removed to input utilities module
# # GET_INP_LINE
# def getInputLine():
#     global userInput
#     userInput = input("Enter input line: ")