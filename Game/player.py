
class Player:
    def __init__(self, money, name) -> None:
        self._money = money
        self._name = name
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

    def __str__(self):
        return f"{', '.join(card.rank+' of '+card.suit for card in self._hand)}"
        #return f"{', '.join(str(card) for card in self._hand)}"
    
    def __repr__(self) -> str:
        return f"Player {self._name}"

