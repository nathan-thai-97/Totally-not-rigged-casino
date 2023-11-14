from CardManagement import CardDealing
CD = CardDealing

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
        self.blackjack_cards = CD()
        self.choice = ''

        # Assign blackjack values for the cards
        self.blackjack_cards_value = {}
        for i in self.blackjack_cards.num_card_as_string:
            self.blackjack_cards_value[i] = int(i)
        for t in ['J', 'K', 'Q']:
            self.blackjack_cards_value[t] = 10
        self.blackjack_cards_value['A'] = 11

        # Setting up initial dealing
        self.player_card_1 = self.blackjack_cards.new_card()
        print(f'Here is your first card: {self.player_card_1}')
        self.player_card_1_value = self.blackjack_cards.dealt_value

        self.dealer_card_1 = self.blackjack_cards.new_card()
        print(f'Here is the dealer first card: {self.dealer_card_1}')
        self.dealer_card_1_value = self.blackjack_cards.dealt_value

        self.player_card_2 = self.blackjack_cards.new_card()
        print(f'Here is your second card: {self.player_card_2}')
        self.player_card_2_value = self.blackjack_cards.dealt_value

        self.dealer_card_2 = self.blackjack_cards.new_card()
        self.dealer_card_2_value = self.blackjack_cards.dealt_value

        self.player_sum = self.card_sum(self.player_card_1_value, self.player_card_2_value)
        self.dealer_sum = self.card_sum(self.dealer_card_1_value, self.dealer_card_2_value)
    def card_sum(self, card_1, card_2):
        sum_card = self.blackjack_cards_value[card_1] + self.blackjack_cards_value[card_2]
        return sum_card

    def blackjack_showdown(self):
        if self.player_sum == 21:
            print('You have a BlackJack!')
            if self.dealer_sum == 21:
                print('The Dealer also have a BlackJack! Your bet is returned')
            else:
                print('You just win 1.5 times your bet! Congratulation')
        elif self.dealer_sum == 21:
            print('The Dealer have a BlackJack!')
            print('You lost your bet! Better luck next time!')
        else:
            while self.choice not in ['hit', 'stand', 'double down', 'split']:
                if self.player_card_1_value == self.player_card_2_value:
                    self.choice = input('Would you like to hit, stand, double down or split: ')
                else:
                    self.choice = input('Would you like to hit, stand, or double down: ')

    def stand(self):
        if self.player_sum > 21:
            print("You are busted!")
            print("You lost your bet! Better luck next time!")
        else:
            while self.dealer_sum <= 17:
                self.dealer_card_draw = se
    def player_choice(self):
        if self.choice is 'stand':
            player_sum = self.card_sum(self.player_card_1_value, self.player_card_2_value)
        elif self.choice is 'double down':







blackjack_game = BlackJack()
blackjack_game.blackjack_showdown()
blackjack_game.player_choice()
# print(blackjack_game.dealer_card_2)
# print(blackjack_game.blackjack_cards_value)