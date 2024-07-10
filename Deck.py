import random
import sqlite3
class Yugioh:
    def __init__(self, name):
        self.name = name
        self.level
        self.atk
        self.dfs
        self.atr
        self.rank


    def __repr__(self):
        return f"{self.name}"

    def change_name(self, new_name):
        self.name = new_name
    

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []


    def add(self, card):
        self.cards.append(card)
    
    def remove(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Example usage:
if __name__ == "__main__":
    deck = Deck()
    deck.add("Ash Blossom")