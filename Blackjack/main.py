# Simple blackjack application
#
import random
import os
from art import logo
# J,Q,K = 10 (will replace with Dictionary maybe)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#clear function of console
def clear():
    os.system('cls' if os.name=="nt" else 'clear')
#dealing cards player/dealer
def deal_card(deal_play):
  deal_play.append(random.choice(cards))
  
#main function of game  
def blackjack():
  black_jack = True
  dealer = []
  player = []
  sum_player = 0
  sum_dealer = 0
  while black_jack:
    play = input("Do you want to play Blackjack ? 'y' or 'n' ").lower()
    clear()
    print(logo)
    continue_deal = True
    if play == "y":
      deal_card(player)
      deal_card(player)
      sum_player = sum(player)
      print(f"Your first 2 cards are: {player}, and the sum is {sum_player}.")
      deal_card(dealer)
      deal_card(dealer)
      sum_dealer = sum(dealer)
      print(f"Computer's first cards is [{dealer[0]}]")
      while sum_dealer < 17:
        deal_card(dealer)
        sum_dealer = sum(dealer)
      while continue_deal:
        continue_black_jack = input("Do you want to continue to deal? 'y' or 'n' ").lower()
        if continue_black_jack == "y":
          deal_card(player)
          sum_player= sum(player)
          if (sum_player >= 20) and (11 in player):
            elf = player.index(11)
            player[elf] = 1
            sum_player = sum(player)
            if sum_player >= 22:
              print(f"Your cards are: {player}, and the final score is {sum_player}. Unfortuntalley you flopped!")
              black_jack = False
              continue_deal = False
            else:
              print(f"   Your cards are: {player}, and the sum is {sum_player}.")
          else:
            if sum_player >= 22:
              print(f"Your cards are: {player}, and the final score is {sum_player}. Unfortuntalley you flopped!")
              black_jack = False
              continue_deal = False
            else:
              print(f"   Your cards are: {player}, and the sum is {sum_player}.")
        else:
          print(f"   Your cards are: {player}, final score is {sum_player}.")
          continue_deal = False
      else:
        if (sum_player>sum_dealer)&((sum_dealer<22)&(sum_player<22)):
          print(f"   Final dealer hands are: {dealer}, final score is: {sum_dealer}.")
          print("\n   Congrats you won!:)")
          black_jack = False
        elif (sum_player<sum_dealer)&((sum_dealer<22)&(sum_player<22)):
          print(f"   Final dealer hands are: {dealer}, final score is: {sum_dealer}.")
          print("\n   Dealer won!:(")
          black_jack = False
        elif (sum_player==sum_dealer)&((sum_dealer<22)&(sum_player<22)) :
          print(f"   Final dealer hands are: {dealer}, final score is {sum_dealer}.")
          print("\n   It's a tie!:|")
          black_jack = False
        elif (sum_player >= 22):
          black_jack = False
        elif (sum_dealer >= 22):
          print(f"   Final dealer hands are: {dealer}, final score is {sum_dealer}.")
          print(f"\n   Dealer flopped, final score is {sum_dealer}. You won!:)")
          black_jack = False
        black_jack = False 
        blackjack()
    else:
      black_jack = False

blackjack()