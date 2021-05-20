# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 701, 581))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(800, 420, 171, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # self.gridLayoutWidget.setStyleSheet('''
        #     QPushButton{border:none;color:blue;}
        #
        #     QPushButton#pushButton_7{
        #         border:none;
        #         border-bottom:1px solid white;
        #         font-size:30px;
        #         font-weight:700;
        #         font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        #     }
        #     QPushButton#pushbutton_3:hover{border-left:4px solid red;font-weight:700;}
        # ''')
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 240, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(780, 240, 211, 161))
        # self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.label_3.setObjectName("label_3")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(760, 240, 251, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('''QTextBrowser{color:red;
                                        font-size:20px;
                                        font-weight:700;
                                        font-family:Times New Roman;}''')

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 40, 251, 181))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QAction("帮助", self.menubar)  # QAction
        self.menu_2.setObjectName("menu_2")
        # self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3 = QtWidgets.QAction("反馈", self.menubar)  # QAction
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopenPicture = QtWidgets.QAction(MainWindow)
        self.actionopenPicture.setObjectName("actionopenPicture")
        self.actionopenVideo = QtWidgets.QAction(MainWindow)
        self.actionopenVideo.setObjectName("actionopenVideo")
        self.menu.addAction(self.actionopenPicture)
        self.menu.addAction(self.actionopenVideo)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2)
        self.menubar.addAction(self.menu_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能垃圾分类系统"))
        self.pushButton_7.setText(_translate("MainWindow", "停止识别"))
        self.pushButton_2.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton.setText(_translate("MainWindow", "图片识别"))
        self.pushButton_3.setText(_translate("MainWindow", "截图识别"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionopenPicture.setText(_translate("MainWindow", "打开图片"))
        self.actionopenVideo.setText(_translate("MainWindow", "打开视频"))
