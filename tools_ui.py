# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_lineEdit_3.setObjectName("output_lineEdit_3")
        self.horizontalLayout.addWidget(self.output_lineEdit_3)
        self.output_toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.output_toolButton.setObjectName("output_toolButton")
        self.horizontalLayout.addWidget(self.output_toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.topic_lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.topic_lineEdit_2.setObjectName("topic_lineEdit_2")
        self.gridLayout.addWidget(self.topic_lineEdit_2, 1, 1, 1, 1)
        self.bootstrap_serverslineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bootstrap_serverslineEdit.setObjectName("bootstrap_serverslineEdit")
        self.gridLayout.addWidget(self.bootstrap_serverslineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setMidLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setMidLineWidth(1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setMidLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_toolButton.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Output_Path："))
        self.label_2.setText(_translate("MainWindow", "Topic："))
        self.label.setText(_translate("MainWindow", "Bootstrap_Servers："))
        self.start.setText(_translate("MainWindow", "Start"))
