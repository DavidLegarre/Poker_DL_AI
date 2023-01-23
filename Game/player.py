
class Player:
    def __init__(self, money) -> None:
        self._money = money
        self._hand = []
        self._bet = 0
        self._folded = False

    # Player Actions
    def call(self, amount):
        self._bet += amount

    def raise_bet(self, amount):
        self._bet += amount

    def reset_bet(self):
        self._bet = 0

    def get_payed(self, amount):
        self._money += amount

    def pay(self, amount):
        self._money -= amount

