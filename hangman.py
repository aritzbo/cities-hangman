import random

def menu():
    print("H A N G M A N")
    return input('\nType "play" to play the game, "exit" to quit: ')

def hangman():
    choosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))   # A random word from the list is choosen
    hidden = list('-' * len(choosen))                                           # Replace such word with dashes, in order to start guessing through several attempts
    already_typed = []
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
                        attempts += 1
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
