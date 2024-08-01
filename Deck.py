
from Yugioh import Yugioh



class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.card_count = 0


    def add(self, card):
        new_card = Yugioh(card)
        self.cards.append(new_card)
        self.card_count += 1

    
    def remove(self, card):
        self.cards.remove(card)
        self.card_count -= 1

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def print_contents(self):
        for card in self.cards:
            print(card)

    def print_deck(self):
        for i in self.cards:
            print(i)

    def print_size(self):
        print(len(self.cards))