import random
from words import word_list


def get_word():
  word = random.choice(word_list)
  return word.upper()


def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters=[]
  guessed_words=[]
  tries = 6
  print("Lets play HANGMAN")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess= input("Please guess a letter: ").upper()
    if len(guess)==1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed the letter",guess)
      elif guess not in word:
        print(guess, "is not in the word.")
        tries-=1
        guessed_letters.append(guess)
      else:
        print("Good job," ,guess, "is the word")
        guessed_letters.append(guess)
        word_as_list= list(word_completion)
        indices= [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index]=guess
        word_completion="".join(word_as_list)
        if "_" not in word_completion:
          guessed= True 
    else:
      print("The guess is not valid.")

    print(display_hangman(tries))
    print(word_completion)
    print("\n")
  if guessed:
    print("Congrats, you win")
  else:
    print("you lost")
    print("The word is "+ word)
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    if input("Play Again? (Y/N) ").upper() == "Y":
      word = get_word()
      play(word)
    else:
      print("The game ends")


if __name__ == "__main__":
    main()