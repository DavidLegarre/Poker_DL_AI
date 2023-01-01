import random

DECK = (
    ("A", "Spades"),
    ("2", "Spades"),
    ("3", "Spades"),
    ("4", "Spades"),
    ("5", "Spades"),
    ("6", "Spades"),
    ("7", "Spades"),
    ("8", "Spades"),
    ("9", "Spades"),
    ("10", "Spades"),
    ("J", "Spades"),
    ("Q", "Spades"),
    ("K", "Spades"),
    ("A", "Hearts"),
    ("2", "Hearts"),
    ("3", "Hearts"),
    ("4", "Hearts"),
    ("5", "Hearts"),
    ("6", "Hearts"),
    ("7", "Hearts"),
    ("8", "Hearts"),
    ("9", "Hearts"),
    ("10", "Hearts"),
    ("J", "Hearts"),
    ("Q", "Hearts"),
    ("K", "Hearts"),
    ("A", "Clubs"),
    ("2", "Clubs"),
    ("3", "Clubs"),
    ("4", "Clubs"),
    ("5", "Clubs"),
    ("6", "Clubs"),
    ("7", "Clubs"),
    ("8", "Clubs"),
    ("9", "Clubs"),
    ("10", "Clubs"),
    ("J", "Clubs"),
    ("Q", "Clubs"),
    ("K", "Clubs"),
    ("A", "Diamonds"),
    ("2", "Diamonds"),
    ("3", "Diamonds"),
    ("4", "Diamonds"),
    ("5", "Diamonds"),
    ("6", "Diamonds"),
    ("7", "Diamonds"),
    ("8", "Diamonds"),
    ("9", "Diamonds"),
    ("10", "Diamonds"),
    ("J", "Diamonds"),
    ("Q", "Diamonds"),
    ("K", "Diamonds")
)

CARD_TO_SCORE = {
    "2" : 1,
    "3" : 2, 
    "4" : 3, 
    "5" : 4, 
    "6" : 5, 
    "7" : 6, 
    "8" : 7, 
    "9" : 8, 
    "9" : 9, 
    "10" : 10, 
    "J" : 11, 
    "Q" : 12, 
    "K" : 13, 
    "A" : 14, 
}

# The ranks and suits of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

class Card: 
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards

    def add_card(self,card):
        self.cards.append(card)
    
    def remove_card(self, card):
        try:
            self.cards.remove(card)    
        except:
            print(f"This hand does not have {card}")

    def __repr__(self):
        return f"{', '.join(str(card) for card in self.cards)}"


class Player:
    def __init__(self, money):
        self.money = money
        self.hand = Hand([])


class Deck:
    def __init__(self):
        self.deck = self.generate_deck()
        self.deck = self.shuffle(self.deck)

    def generate_deck(self):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(rank,suit))
        return deck

    def shuffle(self, deck):
        # Use the Fisher-Yates shuffle algorithm to shuffle the deck
        for i in range(len(deck)-1, 0, -1):
            # Generate a random index j such that 0 <= j <= i
            j = random.randint(0, i)
            # Swap the cards at indices i and j
            deck[i], deck[j] = deck[j], deck[i]

        return deck

    def deal_card(self, player):
        try:
            player.hand.add_card(self.deck.pop())
        except:
            print("Deck is empty")

    def return_card(self, card):
        self.deck.append(card)

    def deal_hand(self,player):
        for i in range(5):
            self.deal_card(player)

    def __repr__(self):
        return f"{', '.join(str(card) for card in self.deck)}"

    def __len__(self):
        return len(self.deck)