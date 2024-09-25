import random

word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Create a variable called display and have it contain as many '_' as the number of letters in the chosen_word
guessed_letters = []

for _ in range(len(chosen_word)):
  guessed_letters.append("_")
  
#TODO-3 - Create a variable called lives at set it to 6 and create a variable called game_loop and set it to true
lives = 6
#TODO 4 - use a while loop to create the game loop for the game
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
# INSIDE THE GAME LOOP
#TODO 5 - Ask the user to enter a guess and assign it to a variable called guess.

#TODO 6 - Generate the logic to detemine if the guess is in the chosen_word or not and apply approriate logic to the result