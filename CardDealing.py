import random as rd


class CardDecks:
    def __init__(self):
        self.card_left = None
        self.num_card_as_string = [str(num) for num in (range(2, 11))]
        self.letter_card = ['J', 'K', 'Q', 'A']
        self.card_value = self.letter_card + self.num_card_as_string
        self.suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.card = []
        for i in self.suit:
            for a in self.card_value:
                self.card.append(f'{a} of {i}')

# Everytime I call the method to deal a card. it must check if the card was already dealt
# Create a class to deal a card and save the card to a list of card dealt.
# Every next card dealt need to be checked against the list of card dealt.


class CardDealing(CardDecks):
    def __init__(self):
        super().__init__()
        self.card_dealt_list = []
        self.dealt_value = ""
        self.dealt_suit = ""
        self.card_dealt = ''

    def new_card(self):
        def random_dealt():
            self.dealt_value = rd.choice(self.card_value)
            self.dealt_suit = rd.choice(self.suit)
            self.card_dealt = f'{self.dealt_value} of {self.dealt_suit}'
            return self.card_dealt

        random_dealt()
        while self.card_dealt in self.card_dealt_list:
            random_dealt()
        else:
            self.card_dealt_list.append(self.card_dealt)
            return self.card_dealt


    def new_deck(self):
        self.card_dealt_list = []


Player_cards = CardDealing()
Player_card_1 = Player_cards.new_card()
Player_card_1_value = Player_cards.dealt_value

print(Player_card_1_value)

