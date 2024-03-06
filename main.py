import game

def play_coin_flip(coin_flip):
  while True:
    user_guess = input("\033[96;1mWhat's your tip? (heads/tails)\033[0m\n> ").lower()
    if (coin_flip.is_guess_valid(user_guess)):
      coin_flip.play(user_guess)
      coin_flip.check_achievements()
      print("\n")
      coin_flip.get_stats()
      return
    else:
      print("\033[91;1mInvalid tip!\033[0m")

def play_dice_roll(dice_roll):
  while True:
    user_guess = int(input("\033[96;1mWhat's your tip? (1-6)\033[0m\n> "))
    if (dice_roll.is_guess_valid(user_guess)):
      dice_roll.play(user_guess)
      print("\n")
      dice_roll.get_stats()
      return
    else:
      print("\033[91;1mInvalid tip!\033[0m")

def quit_game():
  while True:
    wants_to_quit = input("\033[96;1mAre you sure? Your results will be lost. (yes/no)\033[0m\n> ").lower()
    if (wants_to_quit == "yes"):
      print("Bye then! See you next time!")
      exit()
    elif (wants_to_quit == "no"):
      return
    else:
      print("\033[91;1mInvalid answer!\033[0m")

def main_menu():
  coin_flip = game.CoinFlip()
  dice_roll = game.DiceRoll()
  while True:
    game_type = input("\n\033[96;1mMain menu\033[0m\n\033[96;1m1. Play coin flip (2 possible options)\n2. Play dice roll (6 possible options)\033[0m\n3. Quit\n> ").lower()
    if (game_type == "1"):
      play_coin_flip(coin_flip)
    elif (game_type == "2"):
      play_dice_roll(dice_roll)
    elif (game_type == "3"):
      quit_game()
    else:
      print("\033[91;1mInvalid game number!\033[0m")

print("Welcome!")
main_menu()