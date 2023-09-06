# Guessing game where a user has to guess a word in a certain amount of tries

secret = "giraffe"
guess = ""
guessCount = 0
guessLimit = 5
outOfGuesses = False

while(guess != secret) and (not(outOfGuesses)):
    if(guessCount < guessLimit):
        guess = input("Enter guess: ")
        guessCount += 1
    
    else:
        outOfGuesses = True

if(outOfGuesses):
    print("\nYou Lose\n")
else:
    print("\nYou win!\n")
