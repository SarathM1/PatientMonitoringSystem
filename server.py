# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created: Thu Feb 26 16:33:07 2015
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
        MainWindow.resize(918, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 901, 531))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(560, 40, 160, 71))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.serverIp = QtGui.QLineEdit(self.formLayoutWidget)
        self.serverIp.setObjectName(_fromUtf8("serverIp"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.serverIp)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.serverPort = QtGui.QLineEdit(self.formLayoutWidget)
        self.serverPort.setObjectName(_fromUtf8("serverPort"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.serverPort)
        self.run = QtGui.QPushButton(self.tab)
        self.run.setGeometry(QtCore.QRect(650, 150, 71, 27))
        self.run.setObjectName(_fromUtf8("run"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(50, 210, 831, 281))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(110, 30, 231, 161))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.name1 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.name1.setObjectName(_fromUtf8("name1"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.name1)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.heart1 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.heart1.setObjectName(_fromUtf8("heart1"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.heart1)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.temp1 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.temp1.setObjectName(_fromUtf8("temp1"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.temp1)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.pressure1 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.pressure1.setObjectName(_fromUtf8("pressure1"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.pressure1)
        self.campId1 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.campId1.setObjectName(_fromUtf8("campId1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.campId1)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.table = QtGui.QTableWidget(self.tab_2)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(0, 0, 881, 481))
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(9)
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
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDelete_Table = QtGui.QAction(MainWindow)
        self.actionDelete_Table.setObjectName(_fromUtf8("actionDelete_Table"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Server", None))
        self.label.setText(_translate("MainWindow", "IP", None))
        self.serverIp.setText(_translate("MainWindow", "0.0.0.0", None))
        self.label_2.setText(_translate("MainWindow", "Port", None))
        self.serverPort.setText(_translate("MainWindow", "5000", None))
        self.run.setText(_translate("MainWindow", "Run", None))
        self.label_11.setText(_translate("MainWindow", "Name", None))
        self.label_8.setText(_translate("MainWindow", "Heart ", None))
        self.label_9.setText(_translate("MainWindow", "Temp", None))
        self.label_10.setText(_translate("MainWindow", "Pressure", None))
        self.label_4.setText(_translate("MainWindow", "Camp ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Camp ID", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Heart Beat", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Temp", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pressure", None))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Serious ?", None))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data", None))
        self.actionDelete_Table.setText(_translate("MainWindow", "Delete Table", None))

