theMap = {
    "Lobby": {
        "Description" : "This is the lobby",
        "Rooms" : ["Pirate Cove", "Samurai Dojo"]
    },
    "Pirate Cove":{
        "Description": "You are in Pirate Cove",
        "Rooms" : ["Lobby"],
        "Puzzle": "Who has 2 legs and 2 arms? ",
        "Answer" : ["2 Pirates"],
        "Completed" : False
    },
    "Samurai Dojo":{
        "Description" : "You are in a Samaurais Dojo",
        "Rooms" : ["Lobby"],
        "Puzzle": "A ninja comes out of the shadows and is looking for a fight what do you do? ",
        "Answer": ["Fight", "Run"],
        "Completed": False
    }
}

character ={
    "Name": "",
    "HP": 100,
    "Attack": 10,
    "Location": "Lobby",
    "levelsDone": 0
}

gameOver = False
def lobby():
    if(character["levelsDone"] == 2):
        print("You have earned your freedom congratulations")
        gameOver = True
        return
    if character["Name"] == "":
        playerNamer = input("Hi welcome to Temur's game, Enter your player name: ")
        character["Name"] = playerNamer

    print(f"Hi {character["Name"]} You are currently in {character["Location"]}")
    playerLocChoice = input(f"You see {theMap["Lobby"]["Rooms"][0]} and {theMap["Lobby"]["Rooms"][1]}, Where would you like to go?: ")
    while True:
     if playerLocChoice == theMap["Lobby"]["Rooms"][0] or playerLocChoice == theMap["Lobby"]["Rooms"][1]:
         break
     else:
        playerLocChoice = input(f"Choose a valid room ({theMap["Lobby"]["Rooms"][0]}, {theMap["Lobby"]["Rooms"][1]}): ")
    character["Location"] = playerLocChoice
    if character["Location"] == "Pirate Cove":
       pirateCove()
    if character["Location"] == "Samurai Dojo":
       samuraiDojo()

    
def pirateCove():
   if( theMap["Pirate Cove"]["Completed"] == True):
       print("Argh you have already completed this misson you scally wag go away")
       character["Location"] = "Lobby"
       lobby()
       return
   print("Welcome to Pirate Cove: ")
   print("Blackbeard has a question: ", theMap["Pirate Cove"]["Puzzle"])
   playerChoice = input("Answer the riddle: ")
   while True:
        if playerChoice in theMap["Pirate Cove"]["Answer"] or playerChoice == "Quit":
            break
        else:
            playerChoice = input("Try again! (type in Quit to give up and walk the plank): ")
    
   if playerChoice == theMap["Pirate Cove"]["Answer"][0]:
        print("Arghh matey nice one, you can go back to the lobby\n Blackbeard gives you a token")
        theMap["Pirate Cove"]["Completed"] = True 
        character["Location"] = "Lobby"
        character["levelsDone"] = character["levelsDone"] + 1
        lobby()
        return
   if playerChoice == "Quit":
       print("Back to the lobby")
       character["Location"] = "Lobby"
       lobby()
       return

def samuraiDojo():
    if( theMap["Samurai Dojo"]["Completed"] == True):
        print("You have already completed this level well done young master but you must go back to the lobby")
    
    print("Welcome to master Kanji Dojo")
    print(theMap["Samurai Dojo"]["Puzzle"])

    playerChoice = input("How do you approach? (Fight) or (Run): ")
    while True:
        if playerChoice == "Fight" or playerChoice == "Run":
            break
        else:
            playerChoice = input("How do you approach? (Fight) or (Run): ")


    if playerChoice == "Fight":
        print("The ninja throws a shurken star at you")
        playerFightChoice = input("(Catch) or (Dodge): ")
        while True:
            if playerFightChoice == "Catch" or playerFightChoice == "Dodge":
                break
            else:
                playerFightChoice = input("(Catch) or (Dodge): ")
        if playerFightChoice == "Catch":
            print("Have you lost your mind? Obvisouly that wont work")
            character["Location"] = "Lobby"
            lobby()
            return
        if playerFightChoice == "Dodge":
            print("Nice, you dodged the shurken star, now its your turn")
            playerFightChoice = input("(Throw) a shurken star or (Punch) Him: ")

            while True:
                if playerFightChoice != "Throw" or playerFightChoice != "Punch":
                    break
                else:
                    playerFightChoice = input("(Throw) or (Punch)")
            if playerFightChoice == "Throw":
                print("You dont have any stars to throw, *The Ninja slices away*")
                character["Location"] = "Lobby"
                lobby()
                return
            if playerFightChoice == "Punch":
                print("Nice!, You knocked him out!\n Master Kanji gives you a token")
                theMap["Samurai Dojo"]["Completed"] = True
                character["Location"] = "Lobby"
                character["levelsDone"] = character["levelsDone"] + 1
                lobby()
                return
    if playerChoice == "Run":
        print("You have failed come back when you are ready to face the challenge")
        character["Location"] = "Lobby"
        lobby()
        return

lobby()
