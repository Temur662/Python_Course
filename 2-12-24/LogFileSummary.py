#Log File Summary
import os.path
path = "/Users/temursayfutdinov/Documents/CompSci/Python/Nebula_Acdemy/Python_Course/2-12-24"
print("*Log File Summary*")
fileName = input("Enter file name you would like to access: ")
if os.path.isfile(fileName):
    newFile = open(path + "/" + fileName, "r")
    for count, line in enumerate(newFile):
        pass
    print(newFile.read(), "\n")
    print("Number of lines: ", count + 1)
else:
    print("Invalid name, These are the avilable files: ")
    print(os.listdir(path), "\n")
  