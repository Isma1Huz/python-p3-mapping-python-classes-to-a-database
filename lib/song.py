from config import CONN, CURSOR
import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):  # Updated method name to cls
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
        
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid  # Updated this line

# Create the table
Song.create_table()

# Now you can insert and retrieve data
hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()

# Retrieve data
songs = CURSOR.execute('SELECT * FROM songs')
for row in songs:
    print(row)
