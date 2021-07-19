# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_App(object):
    def setupUi(self, App):
        if not App.objectName():
            App.setObjectName(u"App")
        App.setEnabled(True)
        App.resize(400, 120)
        App.setMinimumSize(QSize(400, 150))
        App.setMaximumSize(QSize(800, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(51, 51, 51, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(
            QPalette.Inactive, QPalette.WindowText, brush
        )
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(117, 117, 117, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(
            QPalette.Disabled, QPalette.WindowText, brush2
        )
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        App.setPalette(palette)
        App.setStyleSheet(
            u"QPushButton:hover {\n"
            "	text-decoration: underline;\n"
            "	cursor: pointer;\n"
            "}\n"
            "\n"
            "\n"
            "#label  {\n"
            "	font-size: 25px; \n"
            "	ext-align: center; \n"
            "	color: #fff; \n"
            "	font-weight: 800; \n"
            "	overflow-wrap: break-word;\n"
            "}\n"
            "\n"
            "#getBtn {\n"
            "	background-color: #00BFFF; \n"
            "	color: #fff;\n"
            "	width: 110px;\n"
            "	height: 35px;\n"
            "	text-align: center;\n"
            "}\n"
            "\n"
            "\n"
            "#randomPageBtn {\n"
            "	background-color: #0000FF;\n"
            "	color: #fff;\n"
            "	width: 110px;\n"
            "	height: 35px;\n"
            "	text-align: center;\n"
            "}\n"
            "\n"
            "#quitBtn {\n"
            "	background-color: #ff105e; \n"
            "	color: #fff;\n"
            "	width: 110px;\n"
            "	height: 35px;\n"
            "	text-align: center;\n"
            "}\n"
            ""
        )
        self.lineEdit = QLineEdit(App)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 30, 250, 50))
        self.lineEdit.setMinimumSize(QSize(250, 50))
        self.lineEdit.setMaximumSize(QSize(0, 0))
        palette1 = QPalette()
        self.lineEdit.setPalette(palette1)
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setStyleSheet(
            u"padding: 10; font-family: Roboto;\n" "\n" "\n" ""
        )
        self.getBtn = QPushButton(App)
        self.getBtn.setObjectName(u"getBtn")
        self.getBtn.setGeometry(QRect(20, 30, 110, 35))
        self.getBtn.setMinimumSize(QSize(110, 35))
        self.getBtn.setMaximumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(0, 191, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(
            QPalette.Active, QPalette.PlaceholderText, brush4
        )
        # endif
        palette2.setBrush(
            QPalette.Inactive, QPalette.WindowText, brush
        )
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(
            QPalette.Inactive, QPalette.ButtonText, brush
        )
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(
            QPalette.Inactive, QPalette.PlaceholderText, brush5
        )
        # endif
        palette2.setBrush(
            QPalette.Disabled, QPalette.WindowText, brush
        )
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(
            QPalette.Disabled, QPalette.ButtonText, brush
        )
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(
            QPalette.Disabled, QPalette.PlaceholderText, brush6
        )
        # endif
        self.getBtn.setPalette(palette2)
        font1 = QFont()
        font1.setPointSize(9)
        self.getBtn.setFont(font1)
        self.getBtn.setStyleSheet(u"")
        self.getBtn.setFlat(False)
        self.randomPageBtn = QPushButton(App)
        self.randomPageBtn.setObjectName(u"randomPageBtn")
        self.randomPageBtn.setGeometry(QRect(20, 70, 110, 35))
        self.randomPageBtn.setMinimumSize(QSize(110, 35))
        self.randomPageBtn.setMaximumSize(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush7 = QBrush(QColor(0, 0, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(
            QPalette.Active, QPalette.PlaceholderText, brush8
        )
        # endif
        palette3.setBrush(
            QPalette.Inactive, QPalette.WindowText, brush
        )
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(
            QPalette.Inactive, QPalette.ButtonText, brush
        )
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(
            QPalette.Inactive, QPalette.PlaceholderText, brush9
        )
        # endif
        palette3.setBrush(
            QPalette.Disabled, QPalette.WindowText, brush
        )
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(
            QPalette.Disabled, QPalette.ButtonText, brush
        )
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(
            QPalette.Disabled, QPalette.PlaceholderText, brush10
        )
        # endif
        self.randomPageBtn.setPalette(palette3)
        self.randomPageBtn.setFont(font1)
        self.randomPageBtn.setStyleSheet(u"")
        self.quitBtn = QPushButton(App)
        self.quitBtn.setObjectName(u"quitBtn")
        self.quitBtn.setGeometry(QRect(280, 100, 110, 35))
        self.quitBtn.setMinimumSize(QSize(110, 35))
        self.quitBtn.setMaximumSize(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(255, 16, 94, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush11)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(
            QPalette.Active, QPalette.PlaceholderText, brush12
        )
        # endif
        palette4.setBrush(
            QPalette.Inactive, QPalette.WindowText, brush
        )
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(
            QPalette.Inactive, QPalette.ButtonText, brush
        )
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(
            QPalette.Inactive, QPalette.PlaceholderText, brush13
        )
        # endif
        palette4.setBrush(
            QPalette.Disabled, QPalette.WindowText, brush
        )
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(
            QPalette.Disabled, QPalette.ButtonText, brush
        )
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(
            QPalette.Disabled, QPalette.PlaceholderText, brush14
        )
        # endif
        self.quitBtn.setPalette(palette4)
        self.quitBtn.setFont(font1)
        self.quitBtn.setStyleSheet(u"")
        self.gridFrame = QFrame(App)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 310, 371, 400))
        self.gridFrame.setMinimumSize(QSize(300, 300))
        self.gridFrame.setMaximumSize(QSize(400, 400))
        palette5 = QPalette()
        brush15 = QBrush(QColor(17, 112, 255, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette5.setBrush(
            QPalette.Inactive, QPalette.ButtonText, brush
        )
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette5.setBrush(
            QPalette.Disabled, QPalette.ButtonText, brush2
        )
        self.gridFrame.setPalette(palette5)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(App)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 160, 161, 50))
        self.label.setMinimumSize(QSize(150, 50))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setStyleSheet(u"")

        self.retranslateUi(App)

        self.getBtn.setDefault(False)

        QMetaObject.connectSlotsByName(App)

    # setupUi

    def retranslateUi(self, App):
        App.setWindowTitle(
            QCoreApplication.translate("App", u"Wiki images saver", None)
        )
        self.lineEdit.setText(
            QCoreApplication.translate("App", u"Wiki page url", None)
        )
        self.getBtn.setText(
            QCoreApplication.translate("App", u"Get Images", None)
        )
        self.randomPageBtn.setText(
            QCoreApplication.translate(
                "App", u"Random Wiki Page", None
            )
        )
        self.quitBtn.setText(
            QCoreApplication.translate("App", u"Quit", None)
        )
        self.label.setText("")

    # retranslateUi
