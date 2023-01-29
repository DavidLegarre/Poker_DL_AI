from enum import Enum
from collections import Counter
from cards import Deck, compare_plays
from player import Player

MONEY = 1000
NUM_PLAYERS = 2


class Gameplay:
    def __init__(self, num_players):
        self.num_players = num_players
        names = ["Alice", "Bob"]
        self.deck = Deck()
        self.deck.shuffle()
        print(self.deck.poker_hands)
        self.players = []

        # Initialize players
        for _ in range(num_players):
            self.players.append(Player(MONEY, names[_]))
            self.deck.deal_hand(self.players[-1])

    # Playing settings

    class Actions(Enum):
        raise_bet = "1"
        fold = "2"
        check = "3"
        call = "4"

    def turn(self, i, player, current_bid):
        print(f"Player {i} turn:\n")
        print(f"The current bid is: {current_bid}\n")
        print(f"Player {i} current bid is {player._bet}\n")
        print(f"Player {i}'s hand:\n {player}\n")
        print("1) Raise bet\t 2) Fold\t 3) Check\t 4) Call")
        action = input("")
        match action:
            case self.Actions.raise_bet.value:
                amount = int(input("Raising bet by: "))
                current_bid = amount
                player.raise_bet(amount)
            case self.Actions.fold.value:
                player.folded = True
            case self.Actions.check.value:
                if player._bet != current_bid:
                    print(
                        "You can't check when your bet is not equal\
                         to the current bid"
                    )
            case self.Actions.call.value:
                player._bet = current_bid
            case _:
                print("Wrong input, try again.")

        return current_bid, action

    def wins(self, winner, current_bid):
        for player in self.players:
            player.pay(current_bid)
            player.reset_bet()
            winner.get_payed(current_bid)

        winner.reset_bet()

    def play(self):
        current_bid = 0
        playing = True
        ended_turns = 0

        self.deck.shuffle()

        while playing:
            for i, player in enumerate(self.players):
                i += 1
                current_bid, player_action = self.turn(i, player, current_bid)
                if player_action is self.Actions.fold.value:
                    winner = [player for player in self.players
                              if not player._folded][0]
                    self.wins(winner, current_bid)
                    ended_turns += 1
                    print(winner)
                    playing = False
                    break

                bets = list(
                    Counter(player._bet for player in self.players).values())
                if bets[0] == len(self.players):
                    # For now only 2 players are allowed
                    winner = compare_plays(self.players[0], self.players[1])
                    winner_i = self.players.index(winner)
                    print(f"Player {winner_i} has won the round")
                    self.wins(winner, current_bid)

        return 0


def main():
    game = Gameplay(NUM_PLAYERS)
    game.play()


if __name__ == '__main__':
    main()
