#My first Hangman game in Python

import random

lettersTaken = []
wordList = ["cat", "flower", "dog", "carrot"]

#word is a variable for displaying the word
word = []
wordDisplay = ""
hangmanDisplay = ["  ______",
                  "  |    | ",
                  "  |    O ",
                  "  |   /|\\",
                  "  |   / \\",
                  "  |       ",
                  " --------",
                  " |      |"
                   ]


tries = 0
triesLimit = len(hangmanDisplay)

def Hangman():

    print("Welcome to hangman! Guess the correct word")
    winFlag = False
    chosenWord = wordList[random.randint(0, len(wordList)-1)]
    for c in range(0, len(chosenWord)):
        word.append("_")

    wordDisplay = ""
    for l in word:
        wordDisplay += l
    print(wordDisplay)
    print("")
    
    tries = 0
    while tries < triesLimit:
        letter = input("Letter: ")

        #Find letters and display the word
        if letter in chosenWord:
                
            for l in range(0, len(chosenWord)):
                if  letter == chosenWord[l]:
                    word[l] = letter
                        
            if letter not in lettersTaken:
                lettersTaken.append(letter)
        
        else:
            tries += 1
            if letter not in lettersTaken:
                lettersTaken.append(letter)

        
        #display the hangman
        stage = len(hangmanDisplay) - tries
        i = 0
        while i < tries:
            print(hangmanDisplay[stage])
            stage += 1
            i += 1
            

        #Display letters taken
        wordDisplay = ""
        for l in word:
            wordDisplay += l
        print(wordDisplay)
        print(lettersTaken)
        print("")

        if "_" not in word:
            winFlag = True
            break;
    #Check win conditions
    if winFlag:
        print("Congrats! You won!")
    
    else:
        print("You lost")
        print("The word was "+chosenWord + ".")
    
Hangman()
