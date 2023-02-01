

# My own modules
from .game.gameplay import Gameplay
from model import PokerPlayer


# BATCH_SIZE is the number of transitions sampled from the replay buffer
# GAMMA is the discount factor as mentioned in the previous section
# EPS_START is the starting value of epsilon
# EPS_END is the final value of epsilon
# EPS_DECAY controls the rate of exponential decay of epsilon, higher means a slower decay
# TAU is the update rate of the target network
# LR is the learning rate of the AdamW optimizer
BATCH_SIZE = 128
EPOCHS = 3
GAMMA = 0.99
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 1000
TAU = 0.005
LR = 1e-4
N_ACTIONS = 4
MIN_BET = 50


def play_state(game):
    game.current_bid = MIN_BET

    for i, player in enumerate(game.players):
        i += 1


def train(model):
    game = Gameplay()
    for epoch in range(EPOCHS):
        game_state_0 = game.getState()
        player1, player2, current_bid = game_state_0


if __name__ == '__main__':
    model = PokerPlayer()
    train(model)
