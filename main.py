from hangman.config import word_list, hangman_stage

import random

def get_word():
    word = random.choice(word_list)
    return word.lower()

def display_hangman(incorrect_guesses):
    print(hangman_stage[incorrect_guesses])

def is_letter(guess):
    if len(guess) == 1:
        return True
    return False

print("\n")
print(">>>>>> Welcome to the game where you try to save hangman from irreparable injury by guessing a mystery word! Let's begin!<<<<<<")
print("\n")

def play():
    word = get_word()
    hidden_word = "_" * len(word)
    display_word = " ".join(hidden_word)
    print(f"Here is the mysterious word: {display_word}")
    incorrect_guesses = 0
    incorrect_words_list = []
    letters_list = []
    while incorrect_guesses < len(hangman_stage)-1:
        display_word = " ".join(hidden_word)
        display_hangman(incorrect_guesses)
        guess = input('Guess a word or a letter: ').lower()
        if not guess.isalpha():
            print("Sorry, we didn't recognise that - please enter a letter or a word.")
        elif is_letter(guess):
            if guess in letters_list:
                print(f"You have already guessed {guess}. Your word is still {display_word}. Try another letter!")
                continue
            letters_list.append(guess)
            if guess in word:
                new_word = ""
                for index in range(len(word)):
                    if guess == word[index]:
                        new_word += guess
                    else:
                        new_word += hidden_word[index]
                hidden_word = new_word
                if new_word == word:
                    print(f"That's it! The word was '{word}'. Well done, you saved hangman! :)")
                    return
                else:
                    display_word = " ".join(new_word)
                    print(f"That's correct! Now your word is: {display_word}. Try another letter!")
            else:
                incorrect_guesses += 1
                display_hangman(incorrect_guesses)
                print(f"The hidden word does not contain {guess}. Your word is still {display_word}. Try another letter!")
        else:
            if guess == word:
                print(f"That's correct! The word is '{word}'. Well done, you saved hangman! :)")
                return
            elif guess in incorrect_words_list:
                print(f"You have already guessed '{guess}'. Try another word or letter!")
            elif len(guess) == len(word):
                incorrect_guesses += 1
                incorrect_words_list.append(guess)
                display_hangman(incorrect_guesses)
                words_list = ", ".join(incorrect_words_list)
                print(f"Nice try, but '{guess}' is not the word. Words guessed are: {words_list}. Current word: {display_word} Try again!")
            else:
                incorrect_guesses += 1
                incorrect_words_list.append(guess)
                display_hangman(incorrect_guesses)
                words_list = ", ".join(incorrect_words_list)
                print(f"The hidden word has {len(word)} letters. Words guessed are: {words_list}. Current word: {display_word} Try again!")
        pretty_list = ", ".join(letters_list)
        print(f"Letters guessed are: {pretty_list}.")
    print(f"Oops - you're out of guesses! The word was '{word}'. Hangman couldn't be saved this time :(")

play()
input("Press enter to quit.")