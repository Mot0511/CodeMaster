import sqlite3
import os

runners_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'runners.db')

def getRunners():
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    query = "SELECT * FROM runners"
    res = cur.execute(query).fetchall()
    conn.close()

    return res

def addRunner(ext, runner):
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    cur.execute("INSERT INTO runners (ext, runner) VALUES (?, ?)", [ext, runner])
    conn.commit()
    conn.close()

def updateExt(ext, runner):
    print(ext)
    print(runner)
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    cur.execute(f"UPDATE runners SET ext='{ext}' WHERE runner='{runner}'")
    conn.commit()
    conn.close()

def updateRunner(ext, runner):
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    cur.execute(f"UPDATE runners SET runner='{runner}' WHERE ext='{ext}'")
    conn.commit()
    conn.close()

def deleteRunner(ext, runner):
    conn = sqlite3.connect(runners_path)
    cur = conn.cursor() 
    cur.execute(f"DELETE FROM runners WHERE ext='{ext}' AND runner='{runner}'")
    conn.commit()
    conn.close()