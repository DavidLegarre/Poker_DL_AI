from torch import nn
from torch.nn import functional as F

INPUT_SIZE = 7


class PokerPlayer(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.input = nn.Linear(8, 64)
        self.net1 = nn.Sequential(
            nn.LazyLinear(128),
            nn.LazyLinear(256)
        )
        self.net2 = nn.Sequential(
            nn.LazyLinear(128),
            nn.LazyLinear(64)
        )
        self.out = nn.LazyLinear(4)

    def forward(self, X):
        X = F.relu(self.input(X))
        X = F.relu(self.net1(X))
        X = F.relu(self.net2(X))
        X = F.softmax(self.out(X))
        return X
