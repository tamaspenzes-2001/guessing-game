import game

def main():
  print("Welcome!")
  coin_flip = game.CoinFlip()
  dice_roll = game.DiceRoll()
  while True:
    game_type = input("\033[96;1mWhich guessing game do you want to play?\n1. Coin flip (2 possible options)\n2. Dice roll (6 possible options)\033[0m\n> ").lower()
    if (game_type == "1"):
      while True:
        user_guess = input("\033[96;1mWhat's your tip? (heads/tails)\033[0m\n> ").lower()
        if (coin_flip.is_guess_valid(user_guess)):
          coin_flip.play(user_guess)
          coin_flip.checkAchievements()
          print("\n")
          coin_flip.get_stats()
          break
        else:
          print("\033[91;1mInvalid tip!\033[0m")
    elif (game_type == "2"):
      while True:
        user_guess = int(input("\033[96;1mWhat's your tip? (1-6)\033[0m\n> "))
        if (dice_roll.is_guess_valid(user_guess)):
          dice_roll.play(user_guess)
          print("\n")
          dice_roll.get_stats()
          break
        else:
          print("\033[91;1mInvalid tip!\033[0m")
    else:
      print("\033[91;1mInvalid game number!\033[0m")
      continue

    while True:
      wants_to_go_again = input("\033[96;1mDo you want to go again? (go/quit)\033[0m\n> ").lower()
      if (wants_to_go_again == "go"):
        print("\n")
        break
      elif (wants_to_go_again == "quit"):
        print("Bye! See you next time!")
        exit()
      else:
        print("\033[91;1mInvalid answer!\033[0m")
    
main()