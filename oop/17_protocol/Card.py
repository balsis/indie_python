class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.cards):
            raise StopIteration
        card = self.cards[self.count]
        self.count += 1
        return card


deck = Deck()
for card in deck:
    print(card)
