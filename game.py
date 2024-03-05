import random

class Game:
  def __init__(self, game_type, choices):
    self._guesses = 0
    self._correct_guesses = 0
    self._score = 0
    self._game_type = game_type
    self._choices = choices

  def is_guess_valid(self, guess):
    return guess in self._choices

  def play(self, guess):
    outcome = random.choice(self._choices)
    print("\033[93;1mThe outcome is: " + str(outcome) + "\033[0m")
    self._guesses += 1
    if (guess == outcome):
      print("\033[92;1mCongratulations! You nailed it!\033[0m")
      self._correct_guesses += 1
      self._score += 20
      print("\033[93;1mScore: " + str(self._score) + "\033[0m \033[92;1m(+20)\033[0m")
    else:
      print("\033[91;1mIncorrect tip. Maybe next time.\033[0m")
      if (self._score > 0):
        self._score -= 10
        print("\033[93;1mScore: " + str(self._score) + "\033[0m \033[91;1m(-10)\033[0m")
      else:
        print("\033[93;1mScore: " + str(self._score))

  def get_stats(self):
    print("\033[93;1mCorrect tips in " + self._game_type + ": " + str(self._correct_guesses) + "/" + str(self._guesses) + "\033[0m")