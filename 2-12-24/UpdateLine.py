#Update Specific line in Text File
import os.path
path = "/Users/temursayfutdinov/Documents/CompSci/Python/Nebula_Acdemy/Python_Course/2-12-24"
print("*Log File Summary*")
fileName = input("Enter file name you would like to access: ")
if os.path.isfile(fileName):
    newFile = open(path + "/" + fileName, "r")
    lines = newFile.readlines()
    for i in range(len(lines)):
        print("Line", i + 1, lines[i])

    lineNum = int(input("Enter line to change: "))
    newLineContent = input("Enter line content: ")
    lines[lineNum - 1] = newLineContent
    newFile.close()
    newFile = open(path + "/" + fileName, "w")
    newFile.writelines(lines)
else:
    print("Invalid name, These are the avilable files: ")
    print(os.listdir(path), "\n")