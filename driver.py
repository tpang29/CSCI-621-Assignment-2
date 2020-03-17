import recursiveDescentParser as rdp
import inputUtils as utils

if __name__ == "__main__":

    runProgram = True

    while runProgram:
        fileName = utils.verifyInputFile()
        fileHandle = open(fileName, 'r')

        for line in fileHandle:
            rdp.rdparser(line)

        runProgram = utils.checkToContinue()