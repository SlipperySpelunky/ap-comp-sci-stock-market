import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

guessed_letters = []

for _ in range(len(chosen_word)):
    guessed_letters.append("_")

lives = 6

while True:
    display = " ".join(guessed_letters)
    print(display)

    guess = input("Guess a letter in the word: ")

    is_guess_in_word = False

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guessed_letters[i] = guess
            is_guess_in_word = True
    
    if is_guess_in_word == False:
        lives -= 1

        if lives == 0:
            print(f"You lost! The word was {chosen_word}")
            break
        else:
            print(f"{guess} is not in the word. {lives} lives left")

    if "".join(guessed_letters) == chosen_word:
        print(f"You won! | {chosen_word}")
        break
