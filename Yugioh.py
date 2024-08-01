
import sqlite3

global_dbconnection = sqlite3.connect("sql.db")



class Yugioh:
    def __init__(self, name):
        database = global_dbconnection
        crsr = database.cursor()
        crsr.execute("SELECT * FROM YuGiohDB WHERE CardName LIKE ?", (name+'%',))
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
        return f"Yugioh(name={self.name}, id={self.id}, card_type={self.card_type})"

    def change_name(self, new_name):
        database = global_dbconnection
        crsr = database.cursor()
        crsr.execute("SELECT * FROM YuGiohDB WHERE CardName LIKE ?", (name+'%',))
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