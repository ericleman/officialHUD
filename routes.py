from flask import Flask, render_template, request

from settings import get_parameters, set_parameters

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Settings', methods=['POST', 'GET'])
def settings():
    if request.method=='POST':
      set_parameters(dict(request.form))
      return render_template('index.html')
    else:
      return render_template('settings.html',get_parameters=get_parameters)

@app.route('/HUD')
def hud():
    return render_template('hud.html')

@app.route('/Stats')
def stats():
    return render_template('stats.html')