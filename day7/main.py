from hangman_art_nvim import logo, stages
from hangman_words_nvim import word_list
import random

def generate_a_random_word():
  word = random.choice(word_list)
  print(word)
  return word

def generate_as_many_blank_letters_in_the_word(word):
  blank_letters = "_" * len(word)
  print(blank_letters)
  return blank_letters

def ask_user_to_guess_a_letter():
  guess = input("Guess a letter: ")
  print(guess)
  return guess

def is_the_guess_letter_in_the_word(guess, word):
  index = word.find(guess)
  if index != -1:
    return True, index
  else:
    return False, index

def replace_blank_with_letter(blank_letters, index, guess):
  blank_letters = blank_letters[:index] + guess + blank_letters[index+1:]
  return blank_letters

def lose_a_life():
  lives = len(stages)
  return lives

def are_the_blanks_filled(word):
  if "_" in word:
    return False
  else:
    return True

def have_they_run_out_of_lives(lives):
  if lives == 0:
    print("no more lives")
    return True
  else:
    print(f"lives = {lives}")
    return False

def main():
  print(logo)
  word = generate_a_random_word()
  blank_letters = generate_as_many_blank_letters_in_the_word(word)
  guess = ask_user_to_guess_a_letter()
  bool, index = is_the_guess_letter_in_the_word(guess, word)
  print(bool)
  print(index)
  if bool == True:
    blank_letters = replace_blank_with_letter(blank_letters, index, guess)
  else:
    pass
  print(blank_letters)
  lives = lose_a_life()
  print(lives)
  blanks_ = are_the_blanks_filled(word)
  print(blanks_)
  any_lives = have_they_run_out_of_lives(lives)
  print(any_lives)

if __name__ == "__main__":
  main()
