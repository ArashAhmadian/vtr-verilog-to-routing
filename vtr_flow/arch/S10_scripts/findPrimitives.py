# based on looking at the vqm files, the stratix10 primitives start with 'fourteennm', 
# so stratixiv_ram_block is fourteennm_ram_block

netlistFile = open("fourteennm_atoms.sv", "r")  # open netlist
netlistListFile = open("listOfPrimitives.txt", "a")  # open file to append, not overwrite

primitives = []

for lines in netlistFile:
    currLine = str(lines)  # just in case
    if len(currLine.split()) > 0: 
        if currLine.split()[0] == "module":
            primitives.append(currLine.split()[1])

# remove any duplicates
primitives = list(dict.fromkeys(primitives))

netlistListFile.write("\n")
for p in range(len(primitives)):
    netlistListFile.write("\n"+primitives[p])


# close files at end of program
netlistFile.close()
netlistListFile.close()