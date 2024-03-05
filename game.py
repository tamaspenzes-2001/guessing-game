import random

class Game:
  def __init__(self):
    self._guesses = 0
    self._correct_guesses = 0
    self._score = 0
    self._unlocked_achievements = []

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
        print("\033[93;1mScore: " + str(self._score) + "\033[0m")

class CoinFlip(Game):
  def __init__(self):
    Game.__init__(self)
    self._choices = ["heads", "tails"]
    self._achievements = ["Junior coin flipper", "Medior coin flipper", "Senior coin flipper", "Champion coin flipper"]

  def checkAchievements(self):
    if (self._score >= 100 and not self._achievements[0] in self._unlocked_achievements):
      achievement = self._achievements[0]
    elif (self._score >= 200 and not self._achievements[1] in self._unlocked_achievements):
      achievement = self._achievements[1]
    elif (self._score >= 300 and not self._achievements[2] in self._unlocked_achievements):
      achievement = self._achievements[2]
    elif (self._score >= 400 and not self._achievements[3] in self._unlocked_achievements):
      achievement = self._achievements[3]
    else:
      return
    self._unlocked_achievements.append(achievement)
    print("\033[92;1mCongrats! Achievement unlocked: " + achievement + "\033[0m")
    if (len(self._achievements) == len(self._unlocked_achievements)):
      print("\033[93;1mYou unlocked all coin flip achievements!\033[0m")

  def get_stats(self):
    print("\033[93;1mCorrect tips in coin flip: " + str(self._correct_guesses) + "/" + str(self._guesses) + "\033[0m")

class DiceRoll(Game):
  def __init__(self):
    Game.__init__(self)
    self._choices = range(1, 7)
    self._achievements = ["Junior dice roller", "Medior dice roller", "Senior dice roller", "Champion dice roller"]

  def checkAchievements(self):
    if (self._score >= 60 and not self._achievements[0] in self._unlocked_achievements):
      achievement = self._achievements[0]
    elif (self._score >= 120 and not self._achievements[1] in self._unlocked_achievements):
      achievement = self._achievements[1]
    elif (self._score >= 180 and not self._achievements[2] in self._unlocked_achievements):
      achievement = self._achievements[2]
    elif (self._score >= 240 and not self._achievements[3] in self._unlocked_achievements):
      achievement = self._achievements[3]
    else:
      return
    self._unlocked_achievements.append(achievement)
    print("\033[92;1mCongrats! Achievement unlocked: " + achievement + "\033[0m")
    if (len(self._achievements) == len(self._unlocked_achievements)):
      print("\033[93;1mYou unlocked all dice roll achievements!\033[0m")

  def get_stats(self):
    print("\033[93;1mCorrect tips in dice roll: " + str(self._correct_guesses) + "/" + str(self._guesses) + "\033[0m")