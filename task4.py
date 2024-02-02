# HANGMAN GAME.....

import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while incorrect_attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word: " + current_display)
        
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_attempts += 1
                print(f"Wrong guess! {max_attempts - incorrect_attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if incorrect_attempts == max_attempts:
        print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)

if __name__ == "__main__":
    hangman()