import threading
#==========================================
class TaskThread(QtCore.QThread):

    setTime = QtCore.pyqtSignal(int,int)
    iteration = QtCore.pyqtSignal(threading.Event, int)

    def run(self):

        self.setTime.emit(0,300)
        for i in range(300):
            time.sleep(0.05)
            event = threading.Event()
            self.iteration.emit(event, i)
            event.wait()

#==========================================
class MainWindow(QtGui.QMainWindow):

    _uiform = None

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self._uiform = Ui_MainWindow()
        self._uiform.setupUi(self)
        self._uiform.runButton.clicked.connect(self.startThread)


    def startThread(self):
        self._uiform.progressBar.setRange(0,0)
        self.task = TaskThread()
        self.task.setTime.connect(self.changePB)
        self.task.iteration.connect(self.update_prog_bar)
        self.task.start()

    @QtCore.pyqtSlot(int,int)
    def changePB(self, c, t):
        self.proportionFinished = int(math.floor(100*(float(c)/t)))
        self._uiform.progressBar.setValue(self.proportionFinished)

        self._uiform.progressBar.setRange(0,300)
        self._uiform.progressBar.setValue(0)

    @QtCore.pyqtSlot(threading._Event,int)
    def update_prog_bar(self,event, i)
        self._uiform.progressBar.setValue(i+1)
        print i
        event.set()
