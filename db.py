import sqlite3


conn = sqlite3.conenct('data/memory.db')
cur = conn.cursor()

def set