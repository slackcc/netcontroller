# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 467)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 380, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 40, 551, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 795, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMyTest = QtWidgets.QMenu(self.menuBar)
        self.menuMyTest.setObjectName("menuMyTest")
        self.menuAnother_Tab = QtWidgets.QMenu(self.menuBar)
        self.menuAnother_Tab.setObjectName("menuAnother_Tab")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSomething = QtWidgets.QAction(MainWindow)
        self.actionSomething.setObjectName("actionSomething")
        self.menuMyTest.addAction(self.actionSomething)
        self.menuBar.addAction(self.menuMyTest.menuAction())
        self.menuBar.addAction(self.menuAnother_Tab.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.menuMyTest.setTitle(_translate("MainWindow", "MyTest"))
        self.menuAnother_Tab.setTitle(_translate("MainWindow", "Another Tab"))
        self.actionSomething.setText(_translate("MainWindow", "Something"))

