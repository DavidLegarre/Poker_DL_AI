import collections
import random as rd


# Card = collections.namedtuple('Card', ['rank', 'suit'])


class Card:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    poker_hands = ["High Card", "One Pair", "Two Pair", "Three of a Kind",
                   "Straight", "Flush", "Full House", "Four of a Kind",
                   "Straight Flush", "Royal Flush"]

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
        except IndexError:
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
        return f"{','.join(str(card) for card in self._cards)}"

    def __str__(self) -> str:
        return f"{', '.join(str(card) for card in self._cards)}"


def get_high_card(hand):
    max = Card("2", "spades")

    for card in hand:
        # if Deck.ranks.index(card.rank) > Deck.ranks.index(max.rank):
        if card > max:
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

    ranks_values = [Deck.ranks.index(rank) for rank in ranks]
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
    # ranks_values = [Deck.get_card_rank(card.rank) for card in hand]
    ranks_values = [Deck.ranks.index(card.rank) for card in hand]
    ranks_values.sort()
    for i in range(1, len(ranks_values)):
        if ranks_values[i] - ranks_values[i-1] != 1:
            return False
    return True


def three_of_a_kind(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1, 1, 3]:
        return True
    return False


def two_pair(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1, 2, 2]:
        return True
    return False


def one_pair(hand):
    rank_counts = collections.Counter(card.rank for card in hand)
    count_list = list(rank_counts.values())
    count_list.sort()

    if count_list == [1, 1, 1, 2]:
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

    hand1 = player1._hand
    hand2 = player2._hand

    # This is done in order to later in development
    # add more players to the table
    hands = [hand1, hand2]
    plays = []

    for hand in hands:
        if royal_flush(hand):
            hand_i = Deck.poker_hands.index('Royal Flush')
        elif straight_flush(hand):
            hand_i = Deck.poker_hands.index('Straight Flush')
        elif four_of_a_kind(hand):
            hand_i = Deck.poker_hands.index('Four of a Kind')
        elif full_house(hand):
            hand_i = Deck.poker_hands.index('Full House')
        elif flush(hand):
            hand_i = Deck.poker_hands.index('Flush')
        elif straight(hand):
            hand_i = Deck.poker_hands.index('Straight')
        elif three_of_a_kind(hand):
            hand_i = Deck.poker_hands.index('Three of a Kind')
        elif two_pair(hand):
            hand_i = Deck.poker_hands.index('Two Pair')
        elif one_pair(hand):
            hand_i = Deck.poker_hands.index('One Pair')
        else:
            hand_i = Deck.poker_hands.index('High Card')

        plays.append(hand_i)

    print(plays)

    print(f"Player 1:\n {player1}")
    print(f"Player 2:\n {player2}")

    print(f"Player 1 has {Deck.poker_hands[plays[0]]}")
    print(f"Player 2 has {Deck.poker_hands[plays[1]]}")

    if plays[0] > plays[1]:
        print("Hand 1 wins\n")
        return player1
    elif plays[0] < plays[1]:
        print("Hand 2 wins\n")
        return player2
    else:
        # TODO: There's the issue of what happens if two hands tie
        high_card1 = get_high_card(hand1)
        high_card2 = get_high_card(hand2)
        print("Tie")
        print(f"Player 1 has high card {high_card1}")
        print(f"Player 2 has high card {high_card2}")
        if high_card1 > high_card2:
            print("Hand 1 wins\n")
            return player1
        else:
            print("Hand 2 wins")
            return player2
