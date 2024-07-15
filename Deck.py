import random
import sqlite3
import time

global_dbconnection = sqlite3.connect("sql.db")

class Yugioh:
    def __init__(self, name):
        database = global_dbconnection
        crsr = database.cursor()
        crsr.execute("""SELECT * FROM YuGiohDB WHERE CardName = ?""", (name,))
        card_info = crsr.fetchone()
        if card_info is None:
            print("if working")
            return
        self.name = card_info[0]
        self.id = card_info[1]
        self.card_type = card_info[2]
        self.atrribute = card_info[3]
        self.property = card_info[4]
        self.type = card_info[5]
        self.level = card_info[6]
        self.atk = card_info[7]
        self.dfs = card_info[8]
        self.link = card_info[9]
        self.pen_scale = card_info[10]
        self.description = card_info[11]


    def __repr__(self):
        return f"{self.name}"

    def change_name(self, new_name):
        database = global_dbconnection
        crsr = database.cursor()
        crsr.execute("""SELECT * FROM YuGiohDB WHERE CardName = ?""", (name,))
        card_info = crsr.fetchone()
    
        self.name = card_info[0]
        self.id = card_info[1]
        self.card_type = card_info[2]
        self.atrribute = card_info[3]
        self.property = card_info[4]
        self.type = card_info[5]
        self.level = card_info[6]
        self.atk = card_info[7]
        self.dfs = card_info[8]
        self.link = card_info[9]
        self.pen_scale = card_info[10]
        self.description = card_info[11]

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_card_type(self):
        return self.card_type
    def get_attrribute(self):
        return self.atrribute
    def get_property(self):
        return self.property
    def get_type(self):
        return self.type
    def get_level(self):
        return self.level
    def get_atk(self):
        return self.atk
    def get_dfs(self):
        return self.dfs
    def get_link(self):
        return self.link
    def get_pen_scale(self):
        return self.pen_scale
    def get_description(self):
        return self.description

    

class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []


    def add(self, card):
        new_card = Yugioh(card)
        self.cards.append(new_card)

    
    def remove(self, card):
        self.cards.remove(card)

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


#if the database search worked, return true else false
def db_good_input(name):
    database = global_dbconnection
    crsr = database.cursor()
    crsr.execute("""SELECT * FROM YuGiohDB WHERE CardName = ?""", (name,))
    card_info = crsr.fetchone()

    if card_info is None:
        return False 
    else: 
        return True
    
def User_prompt():
    menu_level = 0
    deck_list = []
    
    print("Welcome to the Deckbuilder\n" + "Made by: Christian Shepperson\n")
    while menu_level != -1:
        try:
            menu_level = int(input("MAIN MENU:\n\n" + "Build a Deck >> 1\n\n" + "Add a card to existing Deck>> 2\n\n" + "Remove a card from a Deck >> 3\n\n" + "View current Decks >> 4\n\n" + "View the cards in a Deck >> 5\n\n" + "View a cards information >> 6\n\n" + "Exit the Program >>-1\n\n" + "Input>>"))
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid Input, Please type one of the options")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(2)
            continue
        if menu_level == 1:
            deck_name = input ("Please type the name you would like the Deck to have or type exit to Return to Main menu. Any other input will be used as a name\n\n" + "Input>>")
            if deck_name == "exit":
                continue
            else:
                deck = Deck(deck_name)
                deck_list.append(deck)
                print("Deck Created! You will now return to the main menu")
                time.sleep(0.5)


    #############################################################################
        if menu_level == 2:
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    print("You do not have a deck created. Please create a deck first\n")
                    time.sleep(1)
                    break
                deck_to_add = input("What deck would you like to add a card to\n" + "Input >>")
                loaded_deck = 0
                for deck in deck_list:
                    if deck_to_add == deck.name:
                        print("Deck has been selected\n")
                        loaded_deck = deck
                        time.sleep(0.5)
                        temp = 1
                if loaded_deck == 0:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Deck not found. Input another deck name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    continue
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    break
                if loaded_deck == 0:
                    break
                card_to_add = input("Enter card by card name\n\n" + "Input >>")

                if db_good_input(card_to_add):
                    card = loaded_deck.add(card_to_add)
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("card not found!!!!!!, enter another card name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    time.sleep(1)
                    continue
                print("Card has successfully added, you will now be returned to the main menu\n\n")
                time.sleep(1)
                temp = 1
        if menu_level == 3:
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    print("You do not have a deck created. Please create a deck first\n")
                    time.sleep(1)
                    break
                deck_to_add = input("What deck would you like to Remove a card from\n" + "Input >>")
                print(deck_to_add)
                loaded_deck = 0
                for deck in deck_list:
                    if deck_to_add == deck.name:
                        print("Deck has been selected\n")
                        loaded_deck = deck
                        time.sleep(1)
                        temp = 1
                if loaded_deck == 0:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Deck not found. Input another deck name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    continue
            if loaded_deck.cards == []:
                print("This deck has no cards to remove, Add a Card first")
                time.sleep(1)
                continue
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    break
                if loaded_deck == 0:
                    break
                card_to_remove = input("Enter card to be removed\n\n" + "Input >>")
                check = 1
                for card in loaded_deck.cards:
                    if card.get_name() == card_to_remove:
                        if db_good_input(card_to_remove):
                            loaded_deck.remove(card_to_remove)
                            print("Card has been successfully removed, you will now be returned to the main menu\n\n")
                            check = 0
                            time.sleep(1)
                            break
                if check == 1:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("card not found!!!!!!, enter another card name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    time.sleep(1)
                    continue
                temp = 1
            



        if menu_level == 4:
            if len(deck_list) == 0:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("no decks created, go make a deck")
                print("!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!")
                time.sleep(1)

            print("Current Decks are:")
            for deck in deck_list:
                print("")
                print(deck.name)
                print("")
                time.sleep(0.5)
        
        if menu_level == 5:
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    print("You do not have a deck created. Please create a deck first\n")
                    time.sleep(1)
                    break
                deck_to_add = input("What Deck would you like to View the cards in?\n" + "Input >>")
                loaded_deck = 0
                for deck in deck_list:
                    if deck_to_add == deck.name:
                        print("Deck has been selected\n")
                        loaded_deck = deck
                        time.sleep(0.5)
                        temp = 1
                if loaded_deck == 0:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Deck not found. Input another deck name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    continue

            if len(deck_list) != 0:
                print("These are the cards in that deck")
                time.sleep(1)
                if loaded_deck.cards == []:
                    print("Deck is Empty, Add some cards")
                for card in loaded_deck.cards:
                    print("")
                    print(card.get_name())

        if menu_level == 6:
            card_name = input("What card would you like to view the information of?\n" + "Input >>")
            
            if db_good_input(card_name):
                database = global_dbconnection
                crsr = database.cursor()
                crsr.execute("""SELECT * FROM YuGiohDB WHERE CardName = ?""", (card_name,))
                card_info = crsr.fetchone()
                print("Here is the card Info:\n")
                print("Name: " + str(card_info[0]) + "\n")
                print("ID: " + str(card_info[1]) + "\n")
                print("Card Type: " + str(card_info[2]) + "\n")
                print("Attribute: " + str(card_info[3]) + "\n")
                print("Property: " + str(card_info[4]) + "\n")
                print("Type: " + str(card_info[5]) + "\n")
                print("Level: " + str(card_info[6]) + "\n")
                print("Atk: " + str(card_info[7]) + "\n")
                print("Def" + str(card_info[8]) + "\n")
                print("Link: " + str(card_info[9]) + "\n")
                print("Pen Scale: " + str(card_info[10]) + "\n")
                print("Description: " + str(card_info[11]) + "\n")
                time.sleep(10)
            else: 
                print("Card not found!!!!!!")
                time.sleep(1)

    print("Now Exiting Program, Goodbye!!")


# Example usage:
def main():
    User_prompt()

main()