from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            card = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.count += 1
            self.cards.append(card)

    def remove(self, name: str):
        if name == "":
            raise ValueError("Card cannot be an empty string!")
        card = [c for c in self.cards if c.name == name][0]
        self.cards.remove(card)
        self.count -= 1

    def find(self, name: str):
        card = [card for card in self.cards if card.name == name][0]
        return card
