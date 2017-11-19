from time import sleep
from DB import DB
import os
from datetime import datetime

db=DB()

def getHands():
  for room in ["Winamax"]: ## TO DO: implement all rooms
    hands_dir = ["/home/eric/Documents/Winamax Poker/accounts/CookandPoker/history/"] ## TO DO: get hands_dir from DB
    filesDBsql = db.sql("select filename, modified from handsfiles where room = '"+room+"'")
    filesDB={f[0]:f[1] for i,f in enumerate(filesDBsql)}
    for filename in os.listdir(hands_dir):
      if filename[-3:] == 'txt':
        print(filename)
        lastmodified=datetime.fromtimestamp(os.stat(hands_dir+"/"+filename).st_mtime).strftime('%Y-%m-%d %H:%M:%S.%f')
        print(lastmodified)
        if (filename not in filesDB or filesDB[filename] != lastmodified):
          print("executing file: "+filename)
          readFile(os.stat(hands_dir,filename))
          if filename not in filesDB:
            db.sql("INSERT INTO handsfiles VALUES (?,?,?)", (filename,room,lastmodified))
          else:
            db.sql("UPDATE handsfiles set modified = ? where filename = ? and room=?", (lastmodified,filename,room))


def readFile(hands_dir,filename):
  pass

if __name__== "__main__":
  getHands()