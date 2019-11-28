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
        self.setAcceptDrops(True)
        self.dragPoint = None
        self.dragOffset = None

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


    def mouseReleaseEvent(self, cursor_event):
        self.chosenPoints.append(cursor_event.pos())
        ##cursor_event.accept()
        self.update()

    ### Wersja, która działa tylko ze zmianą kursora ###

    """def mouseMoveEvent(self, cursor_event):
        if (cursor_event.buttons() and Qt.LeftButton):
            drag = QtGui.QDrag(self)
            drag.setMimeData(QtCore.QMimeData())
            drag.exec_(QtCore.Qt.LinkAction)
            self.update()


    def dragEnterEvent(self, cursor_event):
        print (cursor_event.mimeData().colorData())
        if cursor_event.mimeData()==self.chosenPoints:

            cursor_event.accept()
        else:
            print("test")
            cursor_event.ignore()
          ##  cursor_event.accept()


    def dropEvent(self, cursor_event):
        cursor_event.setDropAction(Qt.MoveAction)
        cursor_event.accept()"""

    ### Wersja wedlug dokumentacji Qt z C++ ###

    def mousePressEvent(self, cursor_event):
        if (cursor_event.button() == Qt.LeftButton):

            self.dragPoint = cursor_event.pos()

    def mouseMoveEvent(self, cursor_event):

        if (not(cursor_event.buttons()) and Qt.LeftButton):
            return
        p = cursor_event.pos() - self.dragPoint
        if (p.manhattanLength() < QApplication.startDragDistance()):
            return

        drag = QtGui.QDrag(self)
        mimedata = QtCore.QMimeData()
        drag.setMimeData(mimedata)
        drag.exec_(QtCore.Qt.LinkAction)
        ##self.update()  ### ?

    def dragEnterEvent(self, cursor_event):
        if cursor_event.mimeData().colorData() == Qt.black:
            cursor_event.acceptProposedAction()

    def dropEvent(self, cursor_event):
        self.ui.drawingLabel.addItems(cursor_event.mimeData())
        cursor_event.acceptProposedAction()





if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())