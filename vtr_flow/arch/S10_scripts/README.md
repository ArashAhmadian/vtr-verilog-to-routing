This folder has the files and scripts used for getting the S10 primitives.

listOfPrimitives.txt has all the primitives found in fourteennm_atoms.sv (the S10 atoms file, comparable to stratixiv_atoms.v). It was written to by the findPrimitives.py script. Basic information like inputs and outputs were there, but the rest of it was encrypted. It could be that logic is similar to the stratixiv primitives, but still need to confirm that. 

convertPrimitives.py is a script that will take a module from fourteennm_atoms.sv and convert it to the argcitecture modeling language. At the moment it can only convert one module at a time, but could later on be generalized to convert any number of primitives. The primitive of interest is placed in primitive.txt, and the result is appeneded into stratix10Primitives.xml.

