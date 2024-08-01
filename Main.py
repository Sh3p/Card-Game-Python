import random
import sqlite3
import time
import json
from pathlib import Path
from Deck import Deck

MAX_MAIN_DECK_SIZE = 60
MAX_EXTRA_DECK_SIZE = 15

global_dbconnection = sqlite3.connect("sql.db")
    



#if the database search worked, return true else false
def db_good_input(name):
    database = global_dbconnection
    crsr = database.cursor()
    crsr.execute("SELECT * FROM YuGiohDB WHERE CardName LIKE ?", (name+'%',))
    card_info = crsr.fetchone()

    if card_info is None:
        return False 
    else: 
        return True

def write_dict(card):
        return {
            'name' : card.name       
}

def save_deck(deck_name, deck):
    file = Path(str(deck_name) + '.json')
    if file.exists() == False:
        diction = []
        for card in deck.cards:
            diction.append(write_dict(card))
        with open(file, 'w') as f:
                json.dump(diction, f)
                return True
    else: 
        ans = input("File already exists would you like to overwrite the file? Answer yes to overwrite any other answer will not overwrite file\n Input >> ")
        if ans == "yes":
            diction = []
            for card in deck.cards:
                diction.append(write_dict(card))
            with open(file, 'w') as f:
                json.dump(diction, f)
                return True
    return False

def load_deck(deck_name):
    file = Path(str(deck_name) + '.json')
    if file.exists() == False:
        print("file does not exist")
        time.sleep(2)
        return
    with open(file, 'r') as f:
        data = json.load(f)
    loaded_deck = Deck(deck_name)
    for cards in data:
        loaded_deck.add(cards["name"])

    return loaded_deck

def text_box(card):

   return print(f"------------------\n|   {card}      |\n------------------")

 
def User_prompt():
    menu_level = 0
    deck_list = []
    
    print("Welcome to the Deckbuilder\n Made by: Christian Shepperson\n")
    while menu_level != -1:
        try:
            menu_level = int(input("MAIN MENU:\n\n Build a Deck >> 1\n\n Add a card to existing Deck>> 2\n\n Remove a card from a Deck >> 3\n\n View current Decks >> 4\n\n View the cards in a Deck >> 5\n\n View a cards information >> 6\n\n Save a deck to file >> 7\n\n Load a deck from a file >> 8\n\n Exit the Program >>-1\n\n Input>> "))
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid Input, Please type one of the options")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(2)
            continue
        if menu_level == 1:
            deck_name = input ("Please type the name you would like the Deck to have or type exit to Return to Main menu. Any other input will be used as a name\n\n Input>> ")
            if deck_name == "exit":
                continue
            else:
                name_check = ""
                for deck in deck_list:
                    if deck_name == deck.name:
                        name_check = deck_name
                        print("Deck already Exists, Pick a different name!!")
                        time.sleep(3)
                if deck_name == name_check:
                    continue     
                deck = Deck(deck_name)
                deck_list.append(deck)
                print("Deck Created! You will now return to the main menu")
                time.sleep(1)


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
                card_to_add = input("Enter card by card name \n\n" + "Input >> ")
                if db_good_input(card_to_add):
                    try:
                        copies = int(input("Enter how many copies you would like to add.\n\n Input >> "))
                    except ValueError:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("Invalid Input, Please type a number")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        time.sleep(1)
                        continue
                    for x in range(0,copies):
                        loaded_deck.add(card_to_add)
                else:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("card not found!!!!!!, enter another card name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    time.sleep(1)
                    continue
                print("Card has successfully added, you will now be returned to the main menu\n\n")
                time.sleep(1)
                temp = 1
    ##################################################################################################################
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
                card_to_remove = input("Enter card to be removed\n\n" + "Input >> ")
                copies = int(input("How many copies would you like to remove \n\n Input >> "))
                copies_removed = 0
                check = 1
                for card in loaded_deck.cards:
                    if card.get_name() == card_to_remove:
                        if db_good_input(card_to_remove):
                            loaded_deck.remove(card)
                            check = 0
                            copies_removed += 1
                            if copies_removed == copies:
                                print("Card(s) has been successfully removed, you will now be returned to the main menu\n\n")
                                time.sleep(1)
                                break
                if check == 1:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("card not found!!!!!!, enter another card name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    time.sleep(1)
                    continue
                temp = 1
            


    ############################################################################################################################
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
                time.sleep(1)
    #############################################################################################################################
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
                    
                    text_box(card.get_name())
                    time.sleep(0.3)
    #######################################################################################################################
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
                print("Def: " + str(card_info[8]) + "\n")
                print("Link: " + str(card_info[9]) + "\n")
                print("Pen Scale: " + str(card_info[10]) + "\n")
                print("Description: " + str(card_info[11]) + "\n")
                time.sleep(10)
            else: 
                print("Card not found!!!!!!")
                time.sleep(1)
    #######################################################################################################################
        if menu_level == 7:
            temp = 0
            while temp != 1:
                if len(deck_list) == 0:
                    print("You do not have a deck created. Please create a deck first\n")
                    time.sleep(1)
                    break
                deck_to_add = input("What deck would you like to save\n Input >>")
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
                if save_deck(loaded_deck.name, loaded_deck) == True:
                    print("Deck Saved by Deck Name")
                    time.sleep(2)
                else:
                    print("!!!!!!!!!!!!!!!")
                    print("file not saved!")
                    print("!!!!!!!!!!!!!!!")
                    time.sleep(2)

    ##########################################################################################################                
        if menu_level == 8:
            temp = 0
            file_exists = "foobar"
            while temp != 1:
                deck_to_load = input("What deck would you like to load\n Input >>")
                #check if deck exists
                for decks in deck_list:
                    if decks.name == deck_to_load:
                        file_exists = input("Deck already exists, would you like to overwrite the deck?\n Input >> ")
                        if file_exists == "yes":
                            deck_list.remove(decks)
                            break
                        else:
                            print("enter another file name")
                            file_exists = "no"
                            break
                if file_exists == "no":

                    print("nothing happened, returning to main menu")
                    time.sleep(2)
                    break

                loaded_deck = load_deck(deck_to_load)
                if loaded_deck is None:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("File not found. Enter another file name")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    continue
                else:
                    deck_list.append(loaded_deck)
                    print("Deck loaded into deck list")
                    time.sleep(2)
                    temp = 1
               



    print("Now Exiting Program, Goodbye!!")


# Example usage:
def main():
    User_prompt()

main()