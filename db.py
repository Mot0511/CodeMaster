import sqlite3
import os

runners_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'runners.db')

def initDB():
    pass

def getRunners():
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    query = "SELECT * FROM runners"
    res = cur.execute(query).fetchall()
    conn.close()

    return res

def updateRunners(runners):
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    cur.execute("DELETE FROM runners")
    for runner in runners:
        cur.execute("INSERT INTO runners (ext, runner) VALUES (?, ?)", [runner[0], runner[1]])
    conn.commit()

    conn.close()