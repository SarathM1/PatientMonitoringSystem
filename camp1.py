# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camp1.ui'
#
# Created: Sun Feb 22 20:34:08 2015
#      by: PyQt4 UI code generator 4.10.3
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
        MainWindow.resize(918, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 871, 531))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.log = QtGui.QTextBrowser(self.tab)
        self.log.setGeometry(QtCore.QRect(45, 190, 791, 291))
        self.log.setObjectName(_fromUtf8("log"))
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 60, 160, 71))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.clientIp = QtGui.QLineEdit(self.formLayoutWidget)
        self.clientIp.setObjectName(_fromUtf8("clientIp"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.clientIp)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.clientPort = QtGui.QLineEdit(self.formLayoutWidget)
        self.clientPort.setObjectName(_fromUtf8("clientPort"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.clientPort)
        self.connect = QtGui.QPushButton(self.tab)
        self.connect.setGeometry(QtCore.QRect(250, 80, 71, 27))
        self.connect.setObjectName(_fromUtf8("connect"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 58, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 231, 128))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.heart = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.heart.setObjectName(_fromUtf8("heart"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.heart)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.temp = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.temp.setObjectName(_fromUtf8("temp"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.temp)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.pressure = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.pressure.setObjectName(_fromUtf8("pressure"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.pressure)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.name = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.name)
        self.table = QtGui.QTableWidget(self.tab_2)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(10, 250, 821, 201))
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 40, 91, 128))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clearName = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clearName.setObjectName(_fromUtf8("clearName"))
        self.verticalLayout.addWidget(self.clearName)
        self.clearHeart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clearHeart.setObjectName(_fromUtf8("clearHeart"))
        self.verticalLayout.addWidget(self.clearHeart)
        self.clearTemp = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clearTemp.setObjectName(_fromUtf8("clearTemp"))
        self.verticalLayout.addWidget(self.clearTemp)
        self.clearPressure = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clearPressure.setObjectName(_fromUtf8("clearPressure"))
        self.verticalLayout.addWidget(self.clearPressure)
        self.send = QtGui.QPushButton(self.tab_2)
        self.send.setGeometry(QtCore.QRect(430, 90, 89, 27))
        self.send.setObjectName(_fromUtf8("send"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Camp ID : 1", None))
        self.label.setText(_translate("MainWindow", "IP", None))
        self.clientIp.setText(_translate("MainWindow", "127.0.0.1", None))
        self.label_2.setText(_translate("MainWindow", "Port", None))
        self.clientPort.setText(_translate("MainWindow", "5001", None))
        self.connect.setText(_translate("MainWindow", "Connect", None))
        self.label_3.setText(_translate("MainWindow", "Log File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings", None))
        self.label_8.setText(_translate("MainWindow", "Heart ", None))
        self.label_9.setText(_translate("MainWindow", "Temp", None))
        self.label_10.setText(_translate("MainWindow", "Pressure", None))
        self.label_11.setText(_translate("MainWindow", "Name", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Heart Beat", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Temp", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pressure", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Serious ?", None))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Time", None))
        self.clearName.setText(_translate("MainWindow", "Clear", None))
        self.clearHeart.setText(_translate("MainWindow", "Clear", None))
        self.clearTemp.setText(_translate("MainWindow", "Clear", None))
        self.clearPressure.setText(_translate("MainWindow", "Clear", None))
        self.send.setText(_translate("MainWindow", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data", None))

