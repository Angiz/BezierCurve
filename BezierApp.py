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
        self.ui.clearButton.clicked.connect(self.Clearing)
        self.chosenPoints = []
        self.show()

    def getDegree(self):
        global degree
        degree =(int)(self.ui.polynomialText.text())

    def Clearing(self):
        self.ui.polynomialText.clear()
        self.chosenPoints.clear()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 8)
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
            qp.setPen(pen)
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
            elif (degree >2) and (iter >3):
                path.moveTo(self.chosenPoints[0].x(), self.chosenPoints[0].y())
                length = len(self.chosenPoints)
                if length <= (degree + 1):
                    for i in range (1, (length-2)):
                        p0 = self.chosenPoints[i]
                        p1 = self.chosenPoints[i+1]
                        midx = (p0.x() + p1.x()) / 2
                        midy = (p0.y() + p1.y()) / 2
                        path.quadTo(p0.x(), p0.y(), midx, midy)
                        qp.setPen(penLine)
                        qp.drawPath(path)
                    p0 = self.chosenPoints[length-2]
                    p1 = self.chosenPoints[length-1]
                    path.quadTo(p0.x(), p0.y(), p1.x(), p1.y())
                    qp.drawPath(path)
                    qp.save()
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