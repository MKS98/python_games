import random
from words import words
import string

##* returns an uppercased word that contains no - nor spaces just a valid english word 
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something for a list of words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # user`s guessed words

    lives = 7
    ## getting user input in uppercase
    while len(word_letters) > 0 and lives > 0:
        # tell user the letters he used alrdy
        print('You have', lives,'lives left and you have used these letters: ', ' '.join(used_letters))
        

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # take user input
        user_letter = input("guess a letter: ").upper()

        # if input is in alphabet but not in our used_letters, we add it to used_letters and remove it from our choosen word
        # else we just take one life
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1 # take one life away on wrong input
                print('\nYour letter,', user_letter, 'is not in the word.')

        # else if the user did input that before
        elif user_letter in used_letters:
            print("\nyou alrdy guessed that! try another letter.")

        # else if the input is not in the choosen word
        else:
            print("\ninvalid character. please try again.")
    # gets here when len(word_letters) == 0 or when lives == 0
    # if lives == 0 you lose
    if lives == 0:
        print("You died! better luck next time. the word was ", word)
    # you win hah!
    else:
        print(f"hola! you guessed right the word is {word}")


hangman()
