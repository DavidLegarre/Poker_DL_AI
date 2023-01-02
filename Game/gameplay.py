from deck import *
from enum import Enum

MONEY = 1000
NUM_PLAYERS = 2

class Gameplay:
    def __init__(self, num_players, deck):
        self.num_players = num_players
        self.deck = deck
        self.players = []
        for _ in range(num_players):
            self.players.append(Player(MONEY))
            self.deck.deal_hand(self.players[-1])

    def find_player(self,player_to_find):
        return self.players[self.players.index(player_to_find)]

    def show_hand(self, player):
        print(self.find_player(player).hand)

    # Playing settings

    class Actions(Enum):
        raise_bet = "1"
        fold = "2"
        check = "3"
        call = "4"

    def play(self):
        for i,player in enumerate(self.players):
            i+=1
            current_bid = 0

            print(f"Player {i} turn:\n")
            print(f"Player {i}'s hand: {player.hand}\n")
            print(f"1) Raise bet\t 2) Fold\t 3) Check\t 4) Call")
            action = input("")
            turn_playing = True
            while turn_playing:
                match action:
                    case self.Actions.raise_bet.value:
                        amount = int(input("Raising bet by: "))
                        current_bid = amount
                        player.raise_bet(amount)
                        turn_playing = False
                    case self.Actions.fold.value:
                        player.folded = True
                        turn_playing = False
                    case self.Actions.check.value:
                        if player.bet == current_bid:
                            turn_playing = False
                        print("You can't call when your bet is not equal to the current bid")
                    case self.Actions.call.value:
                        player.bet = current_bid
                        turn_playing = False
                    case _:
                        print("Wrong input, try again.")
        return 0


def main():
    game = Gameplay(NUM_PLAYERS,Deck())
    player1 = game.players[0]
    player2 = game.players[1]
    game.play()


if __name__=='__main__':
    main()