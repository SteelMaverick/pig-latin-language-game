# Pig Latin Language Game v1

# Displays welcome message upon running program and informs user who the program's developer is
print("Welcome to my pig latin converter!")
print("My name is Steel Maverick")

# First iteration through program
# Asks user if they want program to read a text file for convenience
choice = input("Do you want to translate a text file for convenience? Y/N ")
choiceCapital = choice[0]
choiceCapital = choiceCapital.capitalize()
escaped = False
userInput = ""

# Check if user wants to use a text file or not. Validate their input
if choiceCapital.startswith('Y'):
    # Read and store contents of a valid text file user enters
    print("\nWarning: Make sure text file is in the same directory as program file!")
    print("To not use a text file, hit enter")
    textFileName = input("Enter name of the file (filename).txt: ")
    if textFileName != "":
        fileContent = open(textFileName, "r")
        userInput = fileContent.read()
    # If nothing was entered, user has changed their mind
    else:
        escaped = True
# Checks for unacceptable input
elif not choice.isalpha():
    print("\nSorry, this input is not valid as it contains numbers or symbols. Ending program")
    exit()
elif choice == "":
    print("\nNothing was entered, ending program")
    exit()
elif not choiceCapital.startswith('N'):
    print("\nNot a valid input, ending program")
    exit()

# If they choose to not use a text file or change their mind, ask user to type in a word or phrase instead
if choiceCapital == 'N' or escaped:
    userInput = input("Enter a word, phrase or sentence to convert to pig latin: ")

# Simplify user input by breaking down sentences into words
userInputWordList = userInput.split()

# Defined suffix values to add on to English words as well as some global variables for program to use
consonantSuffix = "ay"
vowelSuffix = "way"
indexCount = 0
continueProgram = True

# Program continuously runs until user has finished
while continueProgram:
    # Check user input to see if it contains numbers or symbols. If so, end the program and tell them input not valid.
    for tempWord in userInputWordList:
        word = tempWord
        if not word.isalpha():
            print("\nSorry, this input is not valid as it contains numbers or symbols, ending program")
            exit()

    # Check user input to see if entry is blank. If so, end the program and tell them nothing was entered.
    if userInput == "":
        print("\nNothing was entered for the program to translate, ending program")
        exit()

    # New translation
    pigLatinTranslation = []

    # Reset decision to back out from entering a text file
    escaped = False

    # Check each word to see if it starts with a vowel
    for tempWord in userInputWordList:
        word = tempWord
        wordLength = len(word)
        if word.startswith('a') or word.startswith('e') or word.startswith('i') or word.startswith('o') or word.startswith('u'):
            # If it starts with a vowel, take the start of the letter and append 'way' to it.
            suffix = word[0] + vowelSuffix
            # Remove the first letter and append the suffix to the end. Add the translation to the list
            cut = word[1:]
            # Check the word's length to decide how to append the suffix
            if wordLength > 1:
                pigLatinWord = cut + "-" + suffix + " "
            else:
                pigLatinWord = suffix + " "
            # Add the translated word to the pig latin word list
            pigLatinTranslation.append(pigLatinWord)
        # If it starts with a consonant, find the cluster length
        else:
            for tempLetter in word:
                letter = tempLetter
                if letter.startswith('a') or letter.startswith('e') or letter.startswith('i') or letter.startswith('o') or letter.startswith('u'):
                    break
                else:
                    indexCount += 1
            # Grab the cluster length and append 'ay' to it
            consonantCluster = word[0:indexCount]
            suffix = consonantCluster + consonantSuffix
            # Remove the cluster and append suffix to it. Add the translated word to the list
            cut = word[indexCount:]
            # Check the word's length to decide how to append the suffix
            if wordLength > 1:
                pigLatinWord = cut + "-" + suffix + " "
            else:
                pigLatinWord = suffix + " "

            # Add the translated word to the pig latin word list
            pigLatinTranslation.append(pigLatinWord)
            # Reset the cluster length for the next word
            indexCount = 0

    # Print out the pig latin translation and compare it to the English version
    print("\nEnglish: " + userInput)
    print("Translation: " + ''.join(pigLatinTranslation))

    # Ask user if they want to translate more words into Pig Latin
    choice = input("\nDo you want to do another translation? Y/N ")
    choiceCapital = choice.capitalize()

    # Check if user wants to continue using program
    if choiceCapital.startswith('Y'):
        # Asks user if they want program to read a text file
        choice = input("Do you want to translate a text file? Y/N ")
        choiceCapital = choice.capitalize()

        # Check if user wants to use a text file or not. Validate their input
        if choiceCapital.startswith('Y'):
            # Read and store contents of a valid text file user enters
            print("\nWarning: Make sure text file is in the same directory as program file!")
            print("To not use a text file, hit enter")
            textFileName = input("Enter name of the file (filename).txt: ")
            if textFileName != "":
                fileContent = open(textFileName, "r")
                userInput = fileContent.read()
            # If nothing was entered, user has changed their mind
            else:
                escaped = True
        # Checks for unacceptable input
        elif not choice.isalpha():
            print("\nSorry, this input is not valid as it contains numbers or symbols. Ending program")
            exit()
        elif choice == "":
            print("\nNothing was entered, ending program")
            exit()
        elif not choiceCapital.startswith('N'):
            print("\nNot a valid input, ending program")
            exit()

        # If they choose to not use a text file, ask user to type in a word or phrase instead
        if choiceCapital == 'N' or escaped:
            userInput = input("Enter a word, phrase or sentence to convert to pig latin: ")
            # Checks for unacceptable input

    else:
        # End program
        continueProgram = False

    # Simplify user input by breaking down sentences into words
    userInputWordList = userInput.split()

# End of program
print("Bye")
