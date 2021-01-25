# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(466, 354)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 441, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 441, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 441, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 50, 441, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.debugTextBrowser = QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setObjectName(u"debugTextBrowser")
        self.debugTextBrowser.setGeometry(QRect(10, 150, 441, 161))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 466, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.browseFolderPathSlot)
        self.checkBox.toggled.connect(MainWindow.excludeConfigSlot)
        self.pushButton_2.clicked.connect(MainWindow.compressToZipSlot)
        self.lineEdit.returnPressed.connect(MainWindow.returnedPressedSlot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zip OpenCart folder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zip OpenCart folder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Folder path", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Exclude configs", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
    # retranslateUi

