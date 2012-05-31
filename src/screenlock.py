import sys
import datetime
import time
from PyQt4 import QtCore, QtGui

### Timezone
class Main(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(Main, self).__init__(parent)
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)        
    ### Gui
    self.b = QtGui.QPushButton("exit", self, clicked=self.close)
    ### Timer
    #self.timer=QtCore.QTimer()
    #self.timer.setInterval(20)
    #self.timer.timeout.connect(self.showsize)
    #self.timer.start()
    
  def showsize(self):
    print "Timer: "
    self.timer.stop();
    
  def showDateTime(self):
    print "Datetime: "
    now = datetime.datetime.now()
    print now
    print now.ctime()
    print now.isoformat()
    print now.strftime("%Y%m%dT%H%M%S")

if __name__ == "__main__":
  app=QtGui.QApplication(sys.argv)
  myapp=Main()
  #myapp.showFullScreen();
  myapp.showDateTime()
  myapp.show()
  # 1 minute delay 
  #QtCore.QTimer.singleShot(10000, app.quit)
  while True:
    time.sleep(5) # 20 seconds
    print "alive"
    
  sys.exit(app.exec_())

