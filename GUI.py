import sys

from PyQt5.QtCore import QObject, QUrl, pyqtSlot, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebKitWidgets import QWebView

from routes import app
from GetHands import monitor

class HandsThread(QThread):
  def __init__(self, function):
    QThread.__init__(self)
    self.function = function

  def __del__(self):
    self.wait()

  def run(self):
    self.function()

class FlaskThread(QThread):
  def __init__(self, application):
    QThread.__init__(self)
    self.application = application

  def __del__(self):
    self.wait()

  def run(self):
    self.application.run(port=5000)

class Window(QWidget):
  def __init__(self):
    super(Window, self).__init__()
    self.setWindowTitle('The HUD')
    view = QWebView(self)
    layout = QVBoxLayout(self)
    layout.addWidget(view)
    view.load(QUrl('http://localhost:5000'))

class Application():
  def __init__(self):
    self.app = QApplication(sys.argv)
    webapp = FlaskThread(app)
    webapp.start()
    #HandsThread(monitor).start()
    self.app.aboutToQuit.connect(webapp.terminate)
    self.window = Window()
    self.window.show()
    self.timer = QTimer()
    self.timer.timeout.connect(self.tick)
    self.timer.start(1000)
    self.app.exec_()
  def tick(self):
    monitor()
