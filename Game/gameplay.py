from enum import Enum
from collections import Counter
import os

from cards import Deck, compare_plays
from player import Player

MONEY = 1000
MAX_TURNS = 50
NUM_PLAYERS = 2
# Define the base bet to start a game
MIN_BET = 50


def clear():
    # Clear the console
    os.system('cls')


class Gameplay:
    def __init__(self, num_players):
        self.num_players = num_players
        names = ["Alice", "Bob"]
        self.current_bid = 0
        self.deck = Deck()
        self.deck.shuffle()
        print(self.deck)
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

    def turn(self, i, player, current_bid, action=0, debug=True):
        if debug:
            print(f"Player {i} turn:\n")
            print(f"The current bid is: {current_bid}\n")
            print(f"Player {i} current bid is {player._bet}\n")
            print(f"Player {i}'s hand:\n {player}\n")
            print("1) Raise bet\t 2) Fold\t 3) Check\t 4) Call")
        while True:
            if debug:
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
                        if not debug:
                            action = self.Actions.call.value
                        continue
                case self.Actions.call.value:
                    player._bet = current_bid
                case _:
                    print("Wrong input, try again.")
            break

        return current_bid, action

    def wins(self, winner, current_bid):
        for player in self.players:
            player.pay(current_bid)
            player.reset_bet()
            winner.get_payed(current_bid)

        winner.reset_bet()

    def play(self, debug=True):
        self.current_bid = MIN_BET
        ended_turns = 0

        # self.deck.shuffle()
        # clear()
        if debug:
            clear()

        for i, player in enumerate(self.players):
            i += 1
            self.current_bid, player_action = self.turn(
                i, player, self.current_bid)

            # If any player folds the other one wins
            if player_action is self.Actions.fold.value:
                winner = [player for player in self.players
                          if not player._folded][0]
                self.wins(winner, self.current_bid)
                ended_turns += 1
                print(winner)
                break

            # Avoid skipping turn when player 1 decides to check
            if ((i == 1) and (player_action is self.Actions.check.value)):
                continue

            bets = list(
                Counter(player._bet for player in self.players).values())

            if bets[0] == len(self.players):
                # For now only 2 players are allowed
                winner = compare_plays(self.players[0], self.players[1])
                winner_i = self.players.index(winner)
                if debug:
                    print(f"Player {winner_i+1} has won the round")
                self.wins(winner, self.current_bid)

        if debug:
            print("New Game? Y/N")
            option = input("")
            while True:
                match option.lower():
                    case "y":
                        return True
                    case "n":
                        print("Well played!")
                        print("Goodbye!")
                        return False
                    case _:
                        print("Wrong input try again (Y/N):")
                        option = input("")

    def isKeepPlaying(self):
        for player in self.players:
            if player._money <= 0:
                return False
        return True

    def getState(self):
        state = []
        for player in self.players:
            state.append(player)
        state.append(self.current_bid)

        return state


def main():
    game = Gameplay(NUM_PLAYERS)
    turns = 0
    playing = True
    while (
        (turns < MAX_TURNS or
         not game.isKeepPlaying()) and
        playing
    ):
        playing = game.play()
        turns += 1


if __name__ == '__main__':
    main()
