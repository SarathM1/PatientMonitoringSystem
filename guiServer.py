# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udpClientGui.ui'
#
# Created: Mon Feb 16 17:34:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(706, 494)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 50, 571, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.termOp = QtGui.QTextBrowser(self.tab)
        self.termOp.setGeometry(QtCore.QRect(50, 100, 481, 181))
        self.termOp.setObjectName(_fromUtf8("termOp"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(330, 300, 71, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.cmd = QtGui.QLineEdit(self.tab)
        self.cmd.setGeometry(QtCore.QRect(130, 50, 271, 25))
        self.cmd.setObjectName(_fromUtf8("cmd"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.cmdOk = QtGui.QPushButton(self.tab)
        self.cmdOk.setGeometry(QtCore.QRect(430, 50, 85, 27))
        self.cmdOk.setObjectName(_fromUtf8("cmdOk"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 70, 160, 142))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.serverIp = QtGui.QLineEdit(self.gridLayoutWidget)
        self.serverIp.setObjectName(_fromUtf8("serverIp"))
        self.gridLayout.addWidget(self.serverIp, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.serverPort = QtGui.QLineEdit(self.gridLayoutWidget)
        self.serverPort.setObjectName(_fromUtf8("serverPort"))
        self.gridLayout.addWidget(self.serverPort, 2, 1, 1, 1)
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(260, 0, 21, 251))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(100, 30, 81, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(340, 70, 160, 142))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.clientIp = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.clientIp.setObjectName(_fromUtf8("clientIp"))
        self.gridLayout_5.addWidget(self.clientIp, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.clientPort = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.clientPort.setObjectName(_fromUtf8("clientPort"))
        self.gridLayout_5.addWidget(self.clientPort, 2, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(380, 30, 71, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 561, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.settingsOk = QtGui.QPushButton(self.tab_2)
        self.settingsOk.setGeometry(QtCore.QRect(220, 270, 85, 27))
        self.settingsOk.setObjectName(_fromUtf8("settingsOk"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget = QtGui.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 50, 241, 219))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.temp = QtGui.QLineEdit(self.layoutWidget)
        self.temp.setObjectName(_fromUtf8("temp"))
        self.gridLayout_2.addWidget(self.temp, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.breath1 = QtGui.QLineEdit(self.layoutWidget)
        self.breath1.setObjectName(_fromUtf8("breath1"))
        self.gridLayout_2.addWidget(self.breath1, 2, 1, 1, 1)
        self.heart = QtGui.QLineEdit(self.layoutWidget)
        self.heart.setObjectName(_fromUtf8("heart"))
        self.gridLayout_2.addWidget(self.heart, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(260, 20, 31, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.dataOk = QtGui.QPushButton(self.tab_3)
        self.dataOk.setGeometry(QtCore.QRect(250, 280, 85, 27))
        self.dataOk.setObjectName(_fromUtf8("dataOk"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.openDb = QtGui.QAction(MainWindow)
        self.openDb.setObjectName(_fromUtf8("openDb"))
        self.deleteDb = QtGui.QAction(MainWindow)
        self.deleteDb.setObjectName(_fromUtf8("deleteDb"))
        self.menuFile.addAction(self.openDb)
        self.menuFile.addAction(self.deleteDb)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.serverIp, self.serverPort)
        MainWindow.setTabOrder(self.serverPort, self.clientIp)
        MainWindow.setTabOrder(self.clientIp, self.clientPort)
        MainWindow.setTabOrder(self.clientPort, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.cmd)
        MainWindow.setTabOrder(self.cmd, self.cmdOk)
        MainWindow.setTabOrder(self.cmdOk, self.temp)
        MainWindow.setTabOrder(self.temp, self.heart)
        MainWindow.setTabOrder(self.heart, self.breath1)
        MainWindow.setTabOrder(self.breath1, self.termOp)
        MainWindow.setTabOrder(self.termOp, self.pushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Test ", None))
        self.label_13.setText(_translate("MainWindow", "Command:", None))
        self.cmdOk.setText(_translate("MainWindow", "Ok", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Terminal", None))
        self.serverIp.setText(_translate("MainWindow", "127.0.0.1", None))
        self.label.setText(_translate("MainWindow", "IP Address", None))
        self.label_2.setText(_translate("MainWindow", "Port", None))
        self.serverPort.setText(_translate("MainWindow", "5000", None))
        self.label_18.setText(_translate("MainWindow", "Server Socket", None))
        self.clientIp.setText(_translate("MainWindow", "127.0.0.1", None))
        self.label_6.setText(_translate("MainWindow", "IP Address", None))
        self.label_7.setText(_translate("MainWindow", "Port", None))
        self.clientPort.setText(_translate("MainWindow", "5001", None))
        self.label_19.setText(_translate("MainWindow", "Client Socket", None))
        self.settingsOk.setText(_translate("MainWindow", "Ok", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings", None))
        self.label_3.setText(_translate("MainWindow", "Temp", None))
        self.label_5.setText(_translate("MainWindow", "Breath", None))
        self.label_4.setText(_translate("MainWindow", "Heartbeat", None))
        self.label_8.setText(_translate("MainWindow", "Data ", None))
        self.dataOk.setText(_translate("MainWindow", "OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Data", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.openDb.setText(_translate("MainWindow", "Open Database", None))
        self.deleteDb.setText(_translate("MainWindow", "Delete Database", None))

