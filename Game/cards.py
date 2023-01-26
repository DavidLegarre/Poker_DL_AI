import collections
import random as rd

from bidict import bidict


card = collections.namedtuple('Card', ['rank', 'suit'])
poker_hands = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House',
               'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card']
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()
#rank_values = dict(zip(ranks, range(14)))
rank_values = bidict(dict(zip(ranks, range(14))))


class Deck:
    def __init__(self) -> None:
        self._cards = [card(rank, suit) for rank in ranks
                       for suit in suits]

    def shuffle(self):
        # Use the Fisher-Yates shuffle algorithm to shuffle the deck
        for i in range(len(self._cards)-1, 0, -1):
            # Generate a random index j such that 0 <= j <= i
            j = rd.randint(0, i)
            # Swap the cards at indices i and j
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]

    def deal_card(self, player):
        try:
            player._hand.append(self._cards.pop())
        except:
            print("Deck empty")

    def deal_hand(self, player):
        for _ in range(5):
            self.deal_card(player)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return f"{', '.join(card.rank+' of '+card.suit for card in self._cards)}"


def get_high_card(hand):
    values = [card.rank for card in hand]
    suits = [card.rank for card in hand]
    card_values = []
    for value in values:
        card_values.append(rank_values[value])

    


def royal_flush(hand):
    values = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    # Check if all cards are of the same rank
    if (not all(suit == suits[0] for suit in suits)):
        return False

    royal_flush_values = ['10', 'J', 'Q', 'K', 'A']

    if set(values) == set(royal_flush_values):
        return True
    else:
        return False


def straight_flush(hand):
    values = [card.rank for card in hand]


def compare_plays(player1, player2):
    """Compare two hands and determine a winner

    Parameters:
    player1 (Player) -- first player
    player2 (Player) -- second player

    Outputs:
    Winner (Player) -- the player with the best hand
    TODO:
    (Optional) tie (string) --
    """
