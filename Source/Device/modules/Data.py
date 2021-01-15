import sqlite3
import Common
import Config


class Data:
    def __init__(self):
        self.conn = sqlite3.connect(Config.SETTINGS["db"])
        self.Init()

    def __del__(self):
        self.conn.close()

    def Init(self):
        try:
            tb_word = 'CREATE TABLE IF NOT EXISTS Word(Word TEXT, Sound TEXT);'
            self.conn.execute(tb_word)
        except:
            print("Data: Create 'Word' failed.")

        try:
            tb_book = 'CREATE TABLE IF NOT EXISTS Book(Code TEXT, Name TEXT);'
            self.conn.execute(tb_book)
        except:
            print("Data: Create 'Book' failed.")

        try:
            tb_book_word = 'CREATE TABLE IF NOT EXISTS Book_Word(Code TEXT, Word TEXT);'
            self.conn.execute(tb_book_word)
        except:
            print("Data: Create 'Book_Word' failed.")
