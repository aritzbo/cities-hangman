# HANGMAN
# The puzzle hides a word from you, which you try to guess letter by letter. If you fail, you'll be “hanged”. If you win, you'll survive

import random
def menu():
    print("H A N G M A N")
    return input('\nType "play" to play the game, "exit" to quit: ')

def hangman():
    # The game randomly chooses a string from the list, in this case city names with rather variable lengths
    choosen = list(random.choice(["prague", "riga", "barcelona", 
                                  "munich", "bordeaux", "montreal",
                                  "bratislava", "antofagasta", "bern"]))
    hidden = list('-' * len(choosen))          # The hidden string is created using the length of the randomly selected word and replacing each character with dashes
    already_typed = []                         # An empty list where all the input will be appended to, simplyfying the way to detect duplicates
    attempts = 0
    
    while attempts < 8:
        print(''.join(hidden))
        guess = input("Input a letter: ")
        if len(guess) == 1:
            if guess.islower() and guess.isalpha():
                if guess in already_typed:
                    print("You've already guessed this letter")
                else:
                    if guess in choosen:
                        for i in range(len(choosen)):
                            if choosen[i] == guess:
                                hidden[i] = guess
                    else:
                        print("That letter doesn't appear in the word")
                        attempts += 1          # Each time the user inputs a letter that doesn't appear in the word, the attempt counter will increase by 1
            else:
                print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")
        if choosen == hidden:
            print("You guessed the word!\nYou survived!")
        elif attempts == 8:
            print("You lost!")
        already_typed.append(guess)
        print()
        
while  menu() == "play":
    hangman()
    break
