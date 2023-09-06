# Take in a phrase or word, & translate it into a different language
# Giraffe Language:
#   vowels -> g
#       dog -> dgg
#       cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":                       # This "if-in" statement lets us check if a letter is in this set of letters
            if(letter.isupper()):
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter

    return translation

print(translate(input("Enter a word/phrase: ")))

