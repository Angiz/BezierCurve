# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bezier.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(499, 50, 271, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.polynomialLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.polynomialLabel.setFont(font)
        self.polynomialLabel.setObjectName("polynomialLabel")
        self.verticalLayout.addWidget(self.polynomialLabel)
        self.polynomialText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.polynomialText.setFont(font)
        self.polynomialText.setObjectName("polynomialText")
        self.verticalLayout.addWidget(self.polynomialText)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 490, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.polynomialButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.polynomialButton.setObjectName("polynomialButton")
        self.horizontalLayout.addWidget(self.polynomialButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(500, 140, 271, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pointsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.pointsLabel.setText("")
        self.pointsLabel.setObjectName("pointsLabel")
        self.verticalLayout_3.addWidget(self.pointsLabel)
        self.drawingLabel = QtWidgets.QLabel(self.centralwidget)
        self.drawingLabel.setGeometry(QtCore.QRect(30, 50, 441, 521))
        self.drawingLabel.setText("")
        self.drawingLabel.setObjectName("drawingLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.polynomialLabel.setText(_translate("MainWindow", "Set a degree of a polynomial:"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.polynomialButton.setText(_translate("MainWindow", "OK"))
