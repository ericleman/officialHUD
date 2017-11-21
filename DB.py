import sqlite3
import os, sys

DB_PATH=os.getcwd()+'/HUD.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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

  def advancedSQL(self,query,keys):
    tmp=None
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    c = conn.cursor()
    try:
      c.execute(query)
      conn.commit()
      tmp=c.fetchall()
    except:
      print("Error in SQL Query")
    conn.close()
    res={}
    for record in tmp:
      key=()
      value={}
      for v in record:
        if v in keys:
          key=key+(record[v],)
        else:
          value[v]=record[v]
      res[key]=value
    return res


if __name__== "__main__":
  reCreate=False
  for arg in sys.argv[1:]:
    if arg == "new":
      reCreate=True
  db=DB()
  if reCreate:
    db.createDB()
  test=db.advancedSQL("select * from handsfiles",['filename','room'])
  print(test)

