
import random
from typing import Any


class Book:
    def __init__(self, name, author, borrowStatus):
        self.name = name
        self.author = author
        self.borrowStatus = borrowStatus
        def borrowStatus(self):
            if self.borrowStatus == True:
                self.borrowStatus = False
            else:
                self.borrowStatus = True


class Member:
    def __init__(self,name, uniID, borrowedBooks):
        self.name = name
        self.uniID = uniID
        self.borrowedBooks = borrowedBooks


class Library:
    def __init__(self): # no arugments being passed so you can fill up library as you wish with addBook(_)
        self.members = [] 
        self.books = []
    
    def addBook(self): # Append new Book(_) class to books[_] array
        bookName = input("Enter book name to add: ")
        bookAuthor = input("Enter the Author: ")
        newBook = Book(bookName, bookAuthor, False)
        self.books.append(newBook)

    def removeBook(self): # remove Book(_) class from books[_] array
        if len(self.books) == 0:
            print("Catalog is empty...")
            return
        print("These are the books in the catalog")
        print("\t CATALOG ")
        i = 1
        for book in self.books:
            print( i, ":", book.name)
            i += 1
        bookToRemove = input("Enter title of book to Remove: ")

        while True:
            for index, book in enumerate(self.books): # enumerate throught books[_] array
                if bookToRemove == book.name: # if you find the correct book to remove
                    print(f"Removing {bookToRemove}...")
                    del self.books[index] # thanks to enumerate we know the index of where the Book(_) we want to delete is in books[_]
                    print(f"{bookToRemove} has been removed")
                    break
            if bookToRemove != book.name:
                bookToRemove = input("Enter valid title: ")
            else:
                break
    
    def borrowBook(self):
        if len(self.members) == 0:
            print("There are no members...")
            return
        memberId = int(input("Enter your member ID: ")) # borrowing will be done via member ID
        indexOfMember = 0
        while True:
            for index, member in enumerate(self.members):
                if memberId == member.uniID:
                    print(f"Member: {memberId}\nName: {member.name}\nFound")
                    indexOfMember = index
                    break
            if memberId != member.uniID:
                memberId = int(input("Enter valid member ID: "))
            else:
                break
        
        print("These are the books avilabe to borrow in the catalog")
        print("\t CATALOG ")
        i = 1
        for book in self.books:
            if book.borrowStatus == False:
                print( i, ":", book.name)
                i += 1
        if i == 1:
            print("All books are currently being borrowed or library is empty...\n")
            return
        bookToBorrow = input("Enter title of book to borrow: ")

        while True:
            for book in self.books:
                if bookToBorrow == book.name:
                    print("Adding to your account...")
                    self.members[indexOfMember].borrowedBooks.append(book.name)
                    book.borrowStatus = True
                    print("Added to account!")
            if bookToBorrow != book.name:
                bookToBorrow = input("Enter title of book to borrow: ")
            else:
                break
    
    def returnBook(self):
        if len(self.members) == 0:
            print("There are no members...")
            return
        memberId = int(input("Enter your member ID: "))
        indexOfMember = 0
        while True:
            for index, member in enumerate(self.members):
                if memberId == member.uniID:
                    print(f"Member: {memberId}\nName: {member.name}\nFound")
                    indexOfMember = index
                    break
            if memberId != member.uniID:
                memberId = int(input("Enter valid member ID: "))
            else:
                break
        i = 1
        if(len(self.members[indexOfMember].borrowedBooks) == 0):
            print("No books to return...")
            return
        for book in self.members[indexOfMember].borrowedBooks:
            print(i, ":", book)
            i += 1
        bookToReturn = input("Which book would you like to return: ")
        while True:
            for indexOfBook, book in enumerate(self.members[indexOfMember].borrowedBooks):
                if bookToReturn == book:
                  print("Removing from your account...")
                  for theBooks in self.books:
                      if theBooks.name == bookToReturn:
                          theBooks.borrowStatus = False
                  del self.members[indexOfMember].borrowedBooks[indexOfBook]
                  break
            if bookToReturn != book:
                bookToReturn = input("Enter title of book to return: ")
            else:
                break

    def addMember(self):
        memberName = input("Enter name: ")
        memberID = random.randint(0, 1000)
        print(f"Your member ID is: {memberID}")
        newMember = Member(memberName, memberID, [])
        self.members.append(newMember)

    def displayBooks(self):
        i = 0
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book.name}   By {book.author}   {book.borrowStatus}")
        
    def displayMembers(self):
        i = 0
        for i, member in enumerate(self.members):
            print(f"{i+1}. {member.name}  {member.uniID}  {member.borrowedBooks}")
        
def menu(lib):
    userChoice = 0
    while(userChoice != 10):
        print("1: Add Members \n2: Add Book\n3: Borrow Book\n4: Return Book\n5: Remove Book\n6: Display Books\n7: Display Members\n8: Exit")
        userChoice = int(input("Enter number of task to perform: "))
        while True:
            if userChoice >= 1 and userChoice < 9:
                break
            else:
                userChoice = int(input("Enter valid task (1 - 8): "))
        
        if userChoice == 1:
            print("Adding Members...")
            lib.addMember()
            print("\n")
        elif userChoice == 2:
            lib.addBook()
        elif userChoice == 3:
            lib.borrowBook()
        elif userChoice == 4:
            lib.returnBook()
        elif userChoice == 5:
            lib.removeBook()
        elif userChoice == 6:
            print("Displaying books...")
            lib.displayBooks()
            print("\n")
        elif userChoice == 7:
            print("Displaying members...")
            lib.displayMembers()
            print("\n")
        elif userChoice == 8:
            print("Ending Program...")
            exit
        menu(lib)
lib = Library()
menu(lib)