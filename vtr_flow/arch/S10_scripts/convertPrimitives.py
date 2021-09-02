primitivesFile = open("primitive.txt", "r")  # open file of interest
xmlPrimitivesFile = open("stratix10Primitives.xml", "a")  # open file to append, not overwrite

name = ""
primitiveModule = ""
inputPorts = []
outputPorts = []
primitivesList = ["fourteennm_ram_block"] # this can be generalized later on

# for the cases where inputs are formatted as: 
#       input input1,input2;
# instead of 
#       input input1;
#       input input2;
def getMultipleInputs(inputsStr) -> list[str]:   
    commaExists = True
    inputsArr = []
    while commaExists == True:
        if inputsStr.find(",") != -1:
            commaExists == True
            endIndex = inputsStr.find(",")
            inputName = ""
            for i in range(endIndex):
                inputName = inputName + inputsStr[i]  # will copy the name of the input port
            inputsArr.append(inputName)

            # remove from inputsStr
            inputsStr = inputsStr.replace(inputName+",","")
        else:
            inputsArr.append(inputsStr)  # no comma left
            commaExists = False 
    return inputsArr

# this will read from listOfPrimitives.txt to generate a list
# def getPrimitivesList(): 
#     primitiveFileList = open("listOfPrimitives.txt", "r")
#     for line in primitiveFileList:
#         primitivesList.append(line)
    

# getPrimitivesList()  # generates the list

# generate a string that holds the module
# for p in range(len(primitivesList)):
#    moduleToFind = "module " + primitivesList[p]  # ie module fourteennm_ff or fourteennm_ram_block
#     for lines in primitivesFile:
#        currLine = str(lines)  # just in case
#         if len(currLine) > 0:
#             if currLine.find(moduleToFind) != -1:
#                 while(currLine != "endmodule"):
#                     primitiveModule = primitiveModule + currLine
#                 primitiveModule = primitiveModule + "endmodule\n"

# these three lines of code are for later 
# pTextFile = open("primitive.txt", "w")  # overwrite previous module
# pTextFile.write(primitiveModule)
# pTextFile.close()


#reopen pTextFile for reading 
#pTextFile = open("primitive.txt", "r")  # overwrite previous module

# get info on primitive
for lines in primitivesFile:
    currLine = str(lines)  # just in case
    if len(currLine.split()) > 0:

        # remove all [...] elements
        hasBrackets = True # default
        wordList = currLine.split()
        while hasBrackets == True:
            for w in range(len(wordList)):
                if wordList[w].find("[") != -1: # if it is there
                    wordList.remove(wordList[w])
                    hasBrackets = True
                    break
                elif wordList[w].find("]") != -1: # if it is there
                    wordList.remove(wordList[w])
                    hasBrackets = True
                    break
                elif wordList[w].find("-") != -1: # if it is there
                    wordList.remove(wordList[w])
                    hasBrackets = True
                    break
                else:
                    hasBrackets = False  # if it doesnt exist

        firstWord = wordList[0]  
        if firstWord == "module":
            name = wordList[1]
        elif firstWord == "input":
            if wordList[1].find(",") != -1:
                iArr =  getMultipleInputs(wordList[1])  # inputs Array
                for inputIndex in range(len(iArr)):
                    finalPortName = iArr[inputIndex].replace(";","")
                    inputPorts.append(finalPortName)
            else:
                finalPortName = wordList[1].replace(";","")
                inputPorts.append(finalPortName)
        elif firstWord == "output":
            if wordList[1].find(",") != -1:
                oArr =  getMultipleInputs(wordList[1])  # outputs Array
                for outputIndex in range(len(oArr)):
                    finalPortName = oArr[outputIndex].replace(";","")
                    outputPorts.append(finalPortName)
            else:
                finalPortName = wordList[1].replace(";","")
                outputPorts.append(finalPortName)

# create model
xmlPrimitivesFile.write("\n\n\n<model" + " name=\"" + name + "\"" + ">")
xmlPrimitivesFile.write("\n  <inputPorts>")
for inport in range(len(inputPorts)):
    xmlPrimitivesFile.write("\n    <port name=\"" + inputPorts[inport] + "\" "+ "/>" )
xmlPrimitivesFile.write("\n  </inputPorts>")

xmlPrimitivesFile.write("\n  <outputPorts>")
for outport in range(len(outputPorts)):
    xmlPrimitivesFile.write("\n    <port name=\"" + outputPorts[outport] + "\" "+ "/>" )
xmlPrimitivesFile.write("\n  </outputPorts>")

xmlPrimitivesFile.write("\n</model>")

# end of program, close all opened files
primitivesFile.close()
xmlPrimitivesFile.close()
# pTextFile.close()