from Bezier import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.polynomialButton.clicked.connect(self.getDegree)
        self.chosenPoints = []
        self.show()

    def getDegree(self):
        global degree
        degree =(int)(self.ui.polynomialText.text())
        print(degree)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 8)
        qp.setPen(pen)
        iter = 0
        settingPos = QtCore.QPoint(505, 145)
        settingPosX = settingPos.x()
        settingPosY = settingPos.y()

        for pos in self.chosenPoints:
            x = pos.x()
            y = pos.y()

            settingPosY = settingPosY+10
            iter = iter+1
            qp.drawPoint(pos)
            qp.drawText(x-10, y-10, "P {}".format(iter))
            qp.drawText(settingPosX, settingPosY+10, "P {} {} ".format(iter, pos))


    def mouseReleaseEvent(self, cursor_event):
        self.chosenPoints.append(cursor_event.pos())
        self.update()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())