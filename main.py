import game

def play_coin_flip(coin_flip):
  while True:
    user_guess = input("\033[96;1mWhat's your tip? (heads/tails)\033[0m\n> ").lower()
    if (coin_flip.is_guess_valid(user_guess)):
      coin_flip.play(user_guess)
      coin_flip.check_achievements()
      return
    else:
      print("\033[91;1mInvalid tip!\033[0m")

def play_dice_roll(dice_roll):
  while True:
    user_guess = int(input("\033[96;1mWhat's your tip? (1-6)\033[0m\n> "))
    if (dice_roll.is_guess_valid(user_guess)):
      dice_roll.play(user_guess)
      coin_flip.check_achievements()
      return
    else:
      print("\033[91;1mInvalid tip!\033[0m")

def get_stats(coin_flip, dice_roll):
  coin_flip.get_stats()
  dice_roll.get_stats()

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
    print("\n\033[96;1mMain menu")
    print("1. Play coin flip (2 possible options)")
    print("2. Play dice roll (6 possible options)")
    print("3. See stats\033[0m")
    print("4. Quit")
    game_type = input("> ").lower()
    match game_type:
      case "1": play_coin_flip(coin_flip)
      case "2": play_dice_roll(dice_roll)
      case "3": get_stats(coin_flip, dice_roll)
      case "4": quit_game()
      case _: print("\033[91;1mInvalid game number!\033[0m")

print("Welcome!")
main_menu()