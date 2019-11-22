from Bezier import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from math import *

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
            iter = iter+1
            if iter>degree+1:
                break
            x = pos.x()
            y = pos.y()
            settingPosY = settingPosY+20
            qp.drawPoint(pos)
            qp.drawText(x-10, y-10, "P {}".format(iter))
            qp.drawText(settingPosX, settingPosY+20, "P {} {} ".format(iter, pos))
            penLine = QPen(Qt.green, 4)
            path = QPainterPath()
            if (degree == 1) and (iter == 2):
                qp.setPen(penLine)
                qp.drawLine(self.chosenPoints[0].x(), self.chosenPoints[0].y(), self.chosenPoints[1].x(), self.chosenPoints[1].y())
            elif (degree == 2) and (iter == 3):
                qp.setPen(penLine)
                path.moveTo(self.chosenPoints[0].x(), self.chosenPoints[0].y())
                path.cubicTo(self.chosenPoints[0].x(), self.chosenPoints[0].y(), self.chosenPoints[1].x(), self.chosenPoints[1].y(), self.chosenPoints[2].x(), self.chosenPoints[2].y())
                qp.drawPath(path)
            elif (degree == 3) and (iter == 4):
                qp.setPen(penLine)
                path.moveTo(self.chosenPoints[0].x(), self.chosenPoints[0].y())
                path.quadTo(self.chosenPoints[1].x(), self.chosenPoints[1].y(),  self.chosenPoints[3].x(), self.chosenPoints[3].y())
                qp.drawPath(path)
        qp.end()


    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            print("Jakis tymczasowy tekst, dopoki nie bede miala pomyslu, co z tym zrobic")

    def mouseReleaseEvent(self, cursor_event):
        self.chosenPoints.append(cursor_event.pos())
        self.update()




if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())