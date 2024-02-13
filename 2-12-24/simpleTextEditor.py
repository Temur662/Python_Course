#Simple Text Editor
import os.path
path = "/Users/temursayfutdinov/Documents/CompSci/Python/Nebula_Acdemy/Python_Course/2-12-24"
def menu():
    choice = input("To Create new text file( Enter 1 ) \nTo read a existing text file( Enter 2 )\nExit( Enter 3 ) \nChoice: ")
    while(int(choice) < 0 and int( choice > 4)):
        choice = input("To Create new text file( Enter 1 ) \n To read a existing text file( Enter 2 )\n Exit( Enter 3 ) \nChoice: ")
        if( int( choice ) == 3):
            break
    if( int( choice ) == 1):
        fileName = input("Enter File Name: ")
        fileInput = input("Enter Content of text file: ")
        newFile = open(path + "/" + fileName, "w")
        newFile.write(fileInput)
        choice = 0
        newFile.close()
        menu()

    if( int( choice ) == 2):   
        fileName = input("Enter file name you would like to access: ")
        if os.path.isfile(fileName):
            newFile = open(path + "/" + fileName, "r")
            print(newFile.read(), "\n")
            choice = 0
            newFile.close()
            menu()
        else:
            print("Invalid name, These are the avilable files: ")
            print(os.listdir(path), "\n")
            choice = 0
            newFile.close()
            menu()

            

print("*Simple Text Editor*")
menu()

