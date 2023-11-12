import random as rd

# BlackJack Rules and Play:
"""
BlackJack rules (Just the dealer and one player):
* Try to get as close but not over 21 total from 2 cards
* Face card and ten-card value as 10. Ace card can be 11 or 1
- Set up:
  + Player will place their bet from $1 to $100.
  +  The dealer will deal one card each for dealer and player face up,
     second card for dealer face down (hole card) and last card for player face up.
- PLay and Payout
  + Naturals or BlackJack: Dealer check if open card is a 10 (10, J, Q, K) or A
    > If both have, it's a tie and the bet returns to the player
    > If only player have, payout 1.5 times the bet
    > if only dealer have, bet is lost
  + The play:
    > PLayer can choose to "hit", "stand", "double down" (If both card have the same value (pair)
      they can also "split")
    > "hit" = take another card until desired (signal by "stand") or hit 21 or more
    > "stand" = don't take any card
    > "double down" bet 100% more money and take exactly one more card.
    > "split" create two hands played independently, each hand starts with one of the original cards
       that take 1 additional cards for each hand and one extra bet for the extra hand
       (total 2 hands, 4 cards, 2 bets)
  + The showdown:
    > If the player bust after "hit", bet is lost
    > After stand, the dealer reveal the hole card
    > If the dealer card results in <= 17, the dealer take card until >= 17
    > If dealer have an ace and counting it as 11 would reach 17 or more (but not over 21)
      must count ace as 11 and stand
  + The payout
    > Tie game: bet is returned to player
    > Player total is higher: dealer pays the bet amount
    > Player total is lower: bet is lost
"""


# Create a card decks


class BlackJack:
    def __init__(self):
        while True:
            try:
                self.bet = int(input("Place your bet between $1 and $100: "))
                while 100 < self.bet or self.bet < 1:
                    self.money_deposit = int(input("The bet doesn't meet our requirement, please input another "
                                                   "amount: "))
                break  # Break out of the loop when input an integer between 100 and 2000

            except ValueError:
                print("The bet doesn't meet our requirement, please input another amount:  ")


blackjack_game = BlackJack()

