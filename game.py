import random

class Game:
  def __init__(self, game_type, choices):
    self._guesses = 0
    self._correct_guesses = 0
    self._game_type = game_type
    self._choices = choices

  def is_guess_valid(self, guess):
    return guess in self._choices

  def play(self, guess):
    outcome = random.choice(self._choices)
    print("The outcome is: " + str(outcome))
    self._guesses += 1
    if (guess == outcome):
      print("Congratulations! You nailed it!")
      self._correct_guesses += 1
    else:
      print("Incorrect tip. Maybe next time.")

  def get_stats(self):
    print("Correct tips in " + self._game_type + ": " + str(self._correct_guesses) + "/" + str(self._guesses))