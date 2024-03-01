import game

def main():
  print("Welcome!")
  coin_flip = game.Game("coin flip", ["heads", "tails"])
  dice_roll = game.Game("dice roll", range(1, 7))
  while True:
    game_type = input("Which guessing game do you want to play? Coin flip (2 possible options) or dice roll (6 possible options)? ").lower()
    if (game_type == "coin flip"):
      while True:
        user_guess = input("What's your tip? (heads/tails) ").lower()
        if (coin_flip.is_guess_valid(user_guess)):
          coin_flip.play(user_guess)
          print("\n")
          coin_flip.get_stats()
          break
        else:
          print("Invalid tip!")
    elif (game_type == "dice roll"):
      while True:
        user_guess = int(input("What's your tip? (1-6) "))
        if (dice_roll.is_guess_valid(user_guess)):
          dice_roll.play(user_guess)
          print("\n")
          dice_roll.get_stats()
          break
        else:
          print("Invalid tip!")
    else:
      print("Invalid game name!")
      continue

    while True:
      wants_to_go_again = input("Do you want to go again? (go/quit) ").lower()
      if (wants_to_go_again == "go"):
        print("\n")
        break
      elif (wants_to_go_again == "quit"):
        exit()
      else:
        print("Invalid answer!")
    
main()