# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    play_won=True
    for i in secret_word:
        if i not in letters_guessed:
          play_won=False
    return play_won      

    
    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    word_pogress=""
    for i in secret_word:
        if i in letters_guessed:
          word_pogress=word_pogress+i
        else:
            word_pogress=word_pogress+"*"
    return word_pogress          


    
    


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    Lowercase_letters=string.ascii_lowercase
    available_letters=""
    for i in Lowercase_letters:
        if i not in letters_guessed:
            available_letters=available_letters+i
    return available_letters        
    # FILL IN YOUR CODE HERE AND DELETE "pass" 


def helper_function (secret_word,letters_guessed):
    choose_from=""
    for i in secret_word:
        if i in get_available_letters(letters_guessed):
            choose_from=choose_from+i
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter
def total_score(count,secret_word,letters_guessed):
    length_of_secret_word=len(secret_word)
    unique_letters=""
    for i in secret_word:
        if i not in unique_letters :
            unique_letters=unique_letters+i

    total=(count+(4*len(unique_letters)))+(3*length_of_secret_word)
    return total

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("welcome to hangman")
    print(f"Iam thinking of a word with {len(secret_word)} letters")
    print("---------")
    letters_guessed = []
    count=10
    vowels=["a","e","i","o","u"]
    while (has_player_won(secret_word,letters_guessed)==False):
     print(f"you have {count} guessses left")
     print(f"available letters : {get_available_letters(letters_guessed)}")
     guess=input("please guess a letter")
     guess_lower=guess.lower()
     if guess_lower.isalpha() or guess_lower == "!":
         if guess_lower == "!":
             with_help=True
             letters_guessed.append(helper_function(secret_word,letters_guessed))
             print(f"your hint letter is:{get_word_progress(secret_word,letters_guessed)}")
             print("-------")
             count=count-3
         elif guess_lower in secret_word and guess_lower not in letters_guessed and guess_lower not in vowels:
             letters_guessed.append(guess_lower)
             print(f"Good guess:{get_word_progress(secret_word,letters_guessed)}")
             print("-------")
             
         elif guess_lower  in letters_guessed:
             print(f"this letter has been guessed before please guess again:{get_word_progress(secret_word,letters_guessed)}")
         elif guess_lower in vowels:
             if guess_lower in secret_word:
                 letters_guessed.append(guess_lower)
                 print(f"Good guess:{get_word_progress(secret_word,letters_guessed)}")
                 print("-------")
                 
             else:   
                  letters_guessed.append(guess_lower)
                  print(f"oops that letter is not in my word :{get_word_progress(secret_word,letters_guessed)}")
                  print("as the letters was a vowels 2 guesses hase been deducted ")
                  print("-------")
                  count=count-2                     
         else:
            letters_guessed.append(guess_lower)
            print(f"oops that letter is not in my word:{get_word_progress(secret_word,letters_guessed)}")
            print("-------")
            count=count-1      
     else:
        print(f"Oops! That is not a valid letter. Please input a letter the alphabet:{get_word_progress(secret_word,letters_guessed)}")   
        print("-------------")
     if count == 0:
        print(f"Sorry, you ran out of guesses. The word was{secret_word}")
        break  
    if has_player_won(secret_word,letters_guessed):
       print("congratulation,you won")
       print(f"your total score is{total_score(count,secret_word,letters_guessed)}")
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     #secret_word = choose_word(wordlist)
     secret_word = "wildcard"
     with_help = False
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    

