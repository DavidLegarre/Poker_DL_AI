from deck import *

class Gameplay:
    def __init__(self, num_players, deck):
        self.num_players = num_players
        self.deck = deck
        self.players = []




def main():
    game = Gameplay(2,Deck())
    print(game.deck)
    print(len(game.deck))


if __name__=='__main__':
    main()