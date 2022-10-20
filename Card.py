from itertools import product

class Card:
    SUIT_CHOICES = ["Hearts", "Diamonds", "Spades", "Clubs"]
    VALUE_CHOICES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit} {self.value}"


if __name__ == '__main__':
    deck = []
    # for suit, value in product(Card.SUIT_CHOICES, Card.VALUE_CHOICES):
    #     deck.append(Card(suit, value))

    for suit in Card.SUIT_CHOICES:
        for value in Card.VALUE_CHOICES:
            deck.append(Card(suit, value))

    print(deck)