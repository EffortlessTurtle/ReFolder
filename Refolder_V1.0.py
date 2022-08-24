#NOTE: This is a program designed to refolder files that are within an appointed directory. It will go to a directory, read a single file, make a folder with the file's name
#then move that file into that folder, it is very no frills
#DO NOT USE IF YOU WANT MULTIPLE FILES INTO ONE FOLDER!


#Imports
import shutil
import os
import sys
import os.path
import pathlib
#Classes

#Methods
def ReFolder():
    #finds file name, makes folder based on name and then move fileTS to folder 
    findSrc = input("Which containing folder do you want to RE-folder the files? (Q to quit) ")            
    if findSrc == "Q" or findSrc == "q":
        sys.exit                    
    #Check validity of path
    valChk = os.path.lexists(str(findSrc))
    if valChk == True:
        print("Path Valid, refoldering")
    elif valChk == False:
        print("PATH INVALID, restart the program")
    src = findSrc
    #for loop returns a list, need to initialize another list to keep file list
    fileList = []
    #Gets list of files without some other stuff os.walk outputs
    for files in os.walk(src):
        for file in files:
            fileList = file
    #print(fileList) #Test print to ensure list isn't contained within for loop
    for file in fileList:
        #print("file name: " + file + "; " + pathlib.Path(file).suffix) #Test print to ensure can go through list and fild file extension
        foldering = file.replace(pathlib.Path(file).suffix,'')
        #print(f"foldering name: {foldering} ; file name: {file}") #Test print, ensure aren't changing file name(can't move file and expect to work without ext)
        filFolder = f"{src}\{foldering}"
        oldFilLoc = f"{src}\{file}"
        #print(filFolder) #Check to ensure folder name correct
        if not os.path.isdir(filFolder):   
            os.makedirs(filFolder)
        shutil.move(oldFilLoc, filFolder)
        
#Main
def main():
    ReFolder()
    
main()

#Credit - EffortlessTurtle
