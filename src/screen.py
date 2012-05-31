import sys
import datetime
import time
from PyQt4 import QtCore, QtGui

class Main(QtGui.QMainWindow):
  def __init__(self):    
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)        
    self.b = QtGui.QPushButton("exit", self, clicked=self.close)
    QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
    
  def lockScreen(self):
    result = false
    return result
  
  def showNowHour(self):
    now = datetime.datetime.now()
    now = now.strftime("%H")    
    return now
  def showNowMinute(self):
    now = datetime.datetime.now()
    return now.strftime("%M")
  
if __name__ == "__main__":
  app=QtGui.QApplication(sys.argv)
  myapp=Main()
  #myapp.showFullScreen();  
  myapp.show()
  # 1 minute delay 
  #QtCore.QTimer.singleShot(10000, app.quit)
  while True:
    time.sleep(2)
    print "alive"
    print myapp.showNowHour()
    print myapp.showNowMinute()
    
  sys.exit(app.exec_())

