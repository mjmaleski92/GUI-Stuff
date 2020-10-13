from PyQt5 import QtWidgets, uic
import sys
import pyautogui
import mouse

points=[]

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('GUI.ui',self)
        self.pointTable=self.findChild(QtWidgets.QTableWidget,'PointTable')
        self.pointTable.setColumnCount(2)


        self.stopBtn=self.findChild(QtWidgets.QToolButton,'Stop')
        self.stopBtn.clicked.connect(self.stopBtnPressed)

        self.playbackBtn=self.findChild(QtWidgets.QToolButton,'Playback')
        self.playbackBtn.clicked.connect(self.playbackBtnPressed)

        self.recordBtn=self.findChild(QtWidgets.QToolButton,'Record')
        self.recordBtn.clicked.connect(self.recordBtnPressed)

        self.pauseBtn=self.findChild(QtWidgets.QToolButton,'Pause')
        self.pauseBtn.clicked.connect(self.pauseBtnPressed)

        self.show()
    def stopBtnPressed(self):
        print("Stop Button Pressed")
        print(points[0][0])
        row=0
        column=0
        for row in range(2):
            for column in points:
                print(points[int(row)][int(column)])
                column+=1
            row+=1
        
        
    def playbackBtnPressed(self):
        print("Playback Button Pressed")

    def recordBtnPressed(self):
        print("Record Button Pressed")
        mouse.hook(printMouseAction)

    def pauseBtnPressed(self):
        print("Pause Button Pressed")
        mouse.unhook_all()

    

def printMouseAction(callback):
    if isinstance(callback,mouse.ButtonEvent) and callback.event_type == "down":
        #print(callback)
        pointTuple=(mouse.get_position(),callback.time)
        points.append(pointTuple)




app = QtWidgets.QApplication(sys.argv)
window=Ui()
app.exec_()