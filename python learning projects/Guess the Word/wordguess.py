class Player:

  def __init__(self, name):
    self.name = name
    self.word = ""
    self.guesses = 0
    self.incorrect_letters = []
    self.correct_letters = []
    self.guess = ""

  def createWord(self):
    self.word = input(f"{self.name}, enter a word: ").lower()
    print(f"There are {len(self.word)} letters in the word")

  def askLetter(self, player):
    while self.guesses != len(player.word):
      self.guess = input(f"{self.name}, make a guess: ").lower()


      for char in player.word:
        if char in self.guess:
          print(f"Correct answer! There are {player.word.count(self.guess)} {self.guess}'s in the word!'")      
          self.correct_letters.append(self.guess * player.word.count(self.guess))
          self.guesses += 1
          break
      else:
        print(f"Incorrect. Try again. You have {self.guesses} guesses left")
        self.guesses += 1
        self.incorrect_letters.append(self.guess)
         

    for letter in self.correct_letters:
      result = "".join(set(self.correct_letters))
      print(result)
      print("Here are all of the letters you got right in your tries")
      print(f"There are {len(player.word)} letters in the word")
      break
  
  def askFinalWord(self, player):
    final_guess = input("Enter the word: ")
    if final_guess == player.word:
      print("You got it!")
      play_again = input("Play again? Y/N: ").lower()
      if play_again == "y":
        game()
      else:
        print("Exiting...")
    else:
      print(f"You lost! The word was {player.word}")
      play_again = input("Play again? Y/N: ").lower()
      if play_again == "y":
        game()
      else:
        print("Exiting...")


def game():
  p1 = Player(input("Player 1 name: "))
  p2 = Player(input("Player 2 name: "))

  p1.createWord()

  p2.askLetter(p1)
  p2.askFinalWord(p1)

game()
