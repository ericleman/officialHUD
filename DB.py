import sqlite3
import os

DB_PATH=os.getcwd()+'/HUD.db'


class DB():
  def __init__(self):
    if not os.path.isfile(DB_PATH): 
      self.createDB()

  def createDB(self):
    if os.path.isfile(DB_PATH): os.remove(DB_PATH)
    query = open('schema.sql', 'r').read()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executescript(query)
    conn.commit()
    c.close()
    conn.close()

  def sql(self,query):
    tmp=None
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
      c.execute(query)
      conn.commit()
      tmp=c.fetchall()
    except:
      print("Error in SQL Query")
    conn.close()
    return tmp

if __name__== "__main__":
  db=DB()

