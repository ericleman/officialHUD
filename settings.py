from DB import DB
from flask import Markup

db=DB()

def get_parameters():
  settings=db.sql("select parameter,display, value from settings")
  html=''
  for setting in settings:
    html += '<label><span class="field">'+setting[1] + ':</span><input type="text" class="input-field" name="'+setting[0] +'" value="'+ ('' if setting[2] is None else setting[2]) +'"><br>'
  return Markup(html)

def set_parameters(settings):
  for setting in settings:
    db.sql("update settings set value ='"+settings[setting][0]+"' where parameter='"+setting+"'")

