import collections
import random as rd

from bidict import bidict


card = collections.namedtuple('Card', ['rank', 'suit'])
poker_hands = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House',
               'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card']
# rank_values = dict(zip(ranks, range(14)))
# rank_values = bidict(dict(zip(ranks, range(14))))


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

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

    def get_card_rank(self, card):
        return self.ranks.index(card.rank)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return f"{', '.join(card.rank+' of '+card.suit for card in self._cards)}"


def get_high_card(hand):
    max = 0

    for card in hand:
        if Deck.get_card_rank(card) > max:
            max = card

    return max


def royal_flush(hand):
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    # Check if all cards are of the same rank
    if (not all(suit == suits[0] for suit in suits)):
        return False

    royal_flush_values = ['10', 'J', 'Q', 'K', 'A']

    if set(ranks) == set(royal_flush_values):
        return True
    else:
        return False


def straight_flush(hand):
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    if (not all(suit == suits[0] for suit in suits)):
        return False

    ranks_values = [Deck.get_card_rank(rank) for rank in ranks]
    ranks_values = sorted(ranks_values)
    prev_rank = 0

    for rank in ranks_values[1:]:
        if rank - prev_rank != 1:
            return False
        prev_rank = rank

    return True


def four_of_a_kind(hand):
    ranks = [card.rank for card in hand]

    counter = collections.Counter(ranks)

    for rank in ranks:
        if counter[rank] == 4:
            return True

    return False


def full_house(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [2, 3]:
        return True
    return False


def flush(hand):
    suits_counts = list(collections.Counter(
        card.suit for card in hand).values())
    if suits_counts == [5]:
        return True
    return False


def straight(hand):
    ranks_values = [Deck.get_card_rank(card.rank) for card in hand]
    ranks_values.sort()
    for i in range(1,len(ranks_values)):
        if ranks_values[i] - ranks_values[i-1] != 1:
            return False
    return True

def three_of_a_kind(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1,1,3]:
        return True
    return False

def two_pair(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1,2,2]:
        return True
    return False
    
def one_pair(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1,1,1,2]:
        return True
    return False

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
