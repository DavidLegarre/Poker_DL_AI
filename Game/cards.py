import collections
import random as rd


Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

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


def compare_plays(self, player1, player2):
    """Compare two hands and determine a winner

    Parameters:
    player1 (Player) -- first player
    player2 (Player) -- second player

    Outputs:
    Winner (Player) -- the player with the best hand
    TODO:
    (Optional) tie (string) --
    """


