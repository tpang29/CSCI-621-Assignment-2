import recursiveDescentParser as rdp
import inputUtils as inp

if __name__ == "__main__":

    runProgram = True

    while runProgram:
        fileName = inp.verifyInputFile()
        fileHandle = open(fileName, 'r')

        for line in fileHandle:
            rdp.rdparser(line)

        runProgram = inp.checkToContinue()