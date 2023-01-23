from cards import Deck, compare_plays
from player import Player
from enum import Enum

MONEY = 1000
NUM_PLAYERS = 2

class Gameplay:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.players = []

        # Initialize players
        for _ in range(num_players):
            self.players.append(Player(MONEY))
            self.deck.deal_hand(self.players[-1])

    # Playing settings

    class Actions(Enum):
        raise_bet = "1"
        fold = "2"
        check = "3"
        call = "4"

    def turn(self, i, player, current_bid):
        print(f"Player {i} turn:\n")
        print(f"Player {i}'s hand: {player._hand}\n")
        print(f"1) Raise bet\t 2) Fold\t 3) Check\t 4) Call")
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
                    print("You can't check when your bet is not equal to the current bid")
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
            for i,player in enumerate(self.players):
                i+=1
                current_bid, player_action = self.turn(i, player, current_bid)
                if player_action is self.Actions.fold.value:
                    winner = [player for player in self.players
                              if  not player._folded][0]
                    self.wins(winner, current_bid)
                    ended_turns += 1
                    print(winner)

                if (ended_turns == self.num_players - 1):
                    playing=False
                    break
                
        return 0




def main():
    game = Gameplay(NUM_PLAYERS)
    player1 = game.players[0]
    player2 = game.players[1]
    game.play()


if __name__=='__main__':
    main()
    
