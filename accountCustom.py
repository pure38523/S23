# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountCustom.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation,QRect
from mainWindow import Ui_MainWindow
# from PyQt5.QObject
from datetime import datetime

import sqlite3

class Ui_selectAccount(object):
    color = ""
    avatar = ""
    username =''
    name=''
    
    def setUserName(self, userName):
        self.userName = userName

    def confirmButtonPressed(self):
        self.setUserName(self.userName)
        usercolor = self.color
        useravatar = self.avatar
        print("Username: ", self.userName)
        self.mainwindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.getUserNameMain(self.userName)

        connection = sqlite3.connect("/Users/purepolachan/Desktop/ProjectSEP_final/Register.db")
        cur = connection.cursor()
        cur.execute("UPDATE USERS SET USERAKA=?, USERCOLOR=?, USERAVATAR=? WHERE USERNAME=?",(self.name,usercolor,useravatar,self.userName))

        
        connection.commit()
        connection.close()

        self.ui2.setupUi(self.mainwindow)
        self.mainwindow.show()
        self.ui.hide()
        

    def nextButton(self):
        self.name = self.getName.text()
        if self.name:
            self.label_avatar.raise_()
            self.green.deleteLater()
            self.red.deleteLater()
            self.white.deleteLater()
            self.cyan.deleteLater()
            self.yellow.deleteLater()
            self.ava01.deleteLater()
            self.ava02.deleteLater()
            self.ava03.deleteLater()
            self.nameText.deleteLater()
            self.getName.deleteLater()
            self.colorText.deleteLater()
            self.avatarText.deleteLater()
            self.anim = QPropertyAnimation(self.label_avatar,b"geometry")
            self.anim.setDuration(2000)
            self.anim.setStartValue(QRect(280,280,250,250))
            self.anim.setEndValue(QRect(550,280,250,250))
            self.confirmButton.deleteLater()
            self.anim2 = QPropertyAnimation(self.doneButton,b"geometry")
            self.anim2.setDuration(2000)
            self.anim2.setStartValue(QRect(830, 600, 141, 51))
            self.anim2.setEndValue(QRect(600, 600, 141, 51))
            self.anim.start()
            self.anim2.start()

            self.userText.setText(self.name)
            # self.fade = QGraphicsOpacityEffect()
            

    def yellowChanged(self, event):
        self.label_avatar.setStyleSheet("background:yellow")
        self.color = "yellow" 
    def redChanged(self, event):
        self.label_avatar.setStyleSheet("background:red")
        self.color = "red"
    def cyanChanged(self, event):
        self.label_avatar.setStyleSheet("background:cyan")
        self.color = "cyan"
    def whiteChanged(self, event):
        self.label_avatar.setStyleSheet("background:white")
        self.color = "white"
    def greenChanged(self, event):
        self.label_avatar.setStyleSheet("background:green")
        self.color = "green"

    def av1Changed(self, event):
        self.label_avatar.setPixmap(QtGui.QPixmap(":/Pic/Pic/avatar01.png"))
        self.avatar = "avatar01"
    def av2Changed(self, event):
        self.label_avatar.setPixmap(QtGui.QPixmap(":/Pic/Pic/avartar02.png"))
        self.avatar = "avatar02"
    def av3Changed(self, event):
        self.label_avatar.setPixmap(QtGui.QPixmap(":/Pic/Pic/avatar03.png"))
        self.avatar = "avatar03"

    def setupUi(self, selectAccount):
        self.ui = selectAccount
        selectAccount.setObjectName("selectAccount")
        selectAccount.resize(1440, 900)
        selectAccount.setMinimumSize(QtCore.QSize(1440, 900))
        font = QtGui.QFont()
        font.setFamily("Optima")
        selectAccount.setFont(font)
        selectAccount.setStyleSheet("background-image: url(:/Pic/Pic/bg.png);")
        self.label_title = QtWidgets.QLabel(selectAccount)
        self.label_title.setGeometry(QtCore.QRect(250, 140, 1000, 61))
        self.label_title.setObjectName("label_title")
        self.label_avatar = QtWidgets.QLabel(selectAccount)
        self.label_avatar.setGeometry(QtCore.QRect(280, 280, 250, 250))
        self.label_avatar.setStyleSheet("background:white")
        self.label_avatar.setText("")
        self.label_avatar.setPixmap(QtGui.QPixmap(":/Pic/Pic/logo_pic.png"))
        self.label_avatar.setScaledContents(True)
        self.label_avatar.setObjectName("label_avatar")
        self.nameText = QtWidgets.QLabel(selectAccount)
        self.nameText.setGeometry(QtCore.QRect(550, 300, 71, 41))
        self.nameText.setObjectName("nameText")
        self.getName = QtWidgets.QLineEdit(selectAccount)
        self.getName.setGeometry(QtCore.QRect(650, 300, 221, 41))
        self.getName.setStyleSheet("border-radius: 10px;\n"
"background: white;\n"
"color:black;")
        self.getName.setObjectName("getName")
        self.colorText = QtWidgets.QLabel(selectAccount)
        self.colorText.setGeometry(QtCore.QRect(550, 400, 71, 31))
        self.colorText.setObjectName("colorText")
        self.avatarText = QtWidgets.QLabel(selectAccount)
        self.avatarText.setGeometry(QtCore.QRect(550, 480, 81, 41))
        self.avatarText.setObjectName("avatarText")
        self.horizontalLayoutWidget = QtWidgets.QWidget(selectAccount)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(650, 400, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.colorLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.colorLayout.setContentsMargins(0, 0, 0, 0)
        self.colorLayout.setObjectName("colorLayout")
        self.red = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.red.setStyleSheet("background:red;\n"
"")
        self.red.setText("")
        self.red.setObjectName("red")
        self.colorLayout.addWidget(self.red)
        self.yellow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.yellow.setStyleSheet("background:yellow\n"
";\n"
"")
        self.yellow.setText("")
        self.yellow.setObjectName("yellow")
        self.colorLayout.addWidget(self.yellow)
        self.cyan = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cyan.setStyleSheet("background:cyan;\n"
"")
        self.cyan.setText("")
        self.cyan.setObjectName("cyan")
        self.colorLayout.addWidget(self.cyan)
        self.white = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.white.setStyleSheet("background:white;\n"
"")
        self.white.setText("")
        self.white.setObjectName("white")
        self.colorLayout.addWidget(self.white)
        self.green = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.green.setStyleSheet("background:green;\n"
"")
        self.green.setText("")
        self.green.setObjectName("green")
        self.colorLayout.addWidget(self.green)
        self.ava02 = QtWidgets.QLabel(selectAccount)
        self.ava02.setGeometry(QtCore.QRect(760, 460, 100, 100))
        self.ava02.setText("")
        self.ava02.setPixmap(QtGui.QPixmap(":/Pic/Pic/avartar02.png"))
        self.ava02.setScaledContents(True)
        self.ava02.setObjectName("ava02")
        self.ava03 = QtWidgets.QLabel(selectAccount)
        self.ava03.setGeometry(QtCore.QRect(870, 460, 100, 100))
        self.ava03.setText("")
        self.ava03.setPixmap(QtGui.QPixmap(":/Pic/Pic/avatar03.png"))
        self.ava03.setScaledContents(True)
        self.ava03.setObjectName("ava03")
        self.ava01 = QtWidgets.QLabel(selectAccount)
        self.ava01.setGeometry(QtCore.QRect(650, 460, 100, 100))
        self.ava01.setStyleSheet("border-color: white")
        self.ava01.setText("")
        self.ava01.setPixmap(QtGui.QPixmap(":/Pic/Pic/avatar01.png"))
        self.ava01.setScaledContents(True)
        self.ava01.setObjectName("ava01")

        self.doneButton = QtWidgets.QPushButton(selectAccount)
        self.doneButton.setGeometry(QtCore.QRect(830, 600, 141, 51))
        self.doneButton.setObjectName("doneButton")
        self.doneButton.setStyleSheet("#doneButton{\n"
"font: 20pt \"American Typewriter\";\n"
"font-weight:bold;\n"
"background: rgb(245, 255, 0);\n"
"color: rgb(9, 52, 56);\n"
"border-radius: 10px;\n"
"}\n"
"#doneButton:hover{\n"
"background: rgb(214, 215, 0);\n"
"}")

        self.confirmButton = QtWidgets.QPushButton(selectAccount)
        self.confirmButton.setGeometry(QtCore.QRect(830, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("#confirmButton{\n"
"font: 20pt \"American Typewriter\";\n"
"font-weight:bold;\n"
"background: rgb(245, 255, 0);\n"
"color: rgb(9, 52, 56);\n"
"border-radius: 10px;\n"
"}\n"
"#confirmButton:hover{\n"
"background: rgb(214, 215, 0);\n"
"}")
        
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.nextButton)
        self.doneButton.clicked.connect(self.confirmButtonPressed)
        self.userText = QtWidgets.QLabel(selectAccount)
        self.userText.setGeometry(QtCore.QRect(650,540,500,41))
        self.userText.setStyleSheet("font-size:24pt; font-weight:600; color:#ffffff;")
#         self.cancelButton = QtWidgets.QPushButton(selectAccount)
#         self.cancelButton.setGeometry(QtCore.QRect(660, 600, 141, 51))
#         self.cancelButton.setStyleSheet("#cancelButton{\n"
# "font: 20pt \"American Typewriter\";\n"
# "font-weight:bold;\n"
# "background: white;\n"
# "    color: rgb(207, 203, 0);\n"
# "border-radius: 10px;\n"
# "}\n"
# "#cancelButton:hover{\n"
# "background: rgb(230, 228, 231);\n"
# "}")
#         self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(selectAccount)
        QtCore.QMetaObject.connectSlotsByName(selectAccount)

        self.yellow.mousePressEvent = self.yellowChanged
        self.red.mousePressEvent = self.redChanged
        self.cyan.mousePressEvent = self.cyanChanged
        self.white.mousePressEvent = self.whiteChanged
        self.green.mousePressEvent = self.greenChanged
        self.ava01.mousePressEvent = self.av1Changed
        self.ava02.mousePressEvent = self.av2Changed
        self.ava03.mousePressEvent = self.av3Changed

    def retranslateUi(self, selectAccount):
        _translate = QtCore.QCoreApplication.translate
        selectAccount.setWindowTitle(_translate("selectAccount", "Form"))
        self.label_title.setText(_translate("selectAccount", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Firstly, Choose your name and avatar!</span></p><p><br/></p></body></html>"))
        self.nameText.setText(_translate("selectAccount", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Name</span></p></body></html>"))
        self.colorText.setText(_translate("selectAccount", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Color</span></p><p><br/></p></body></html>"))
        self.avatarText.setText(_translate("selectAccount", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Avatar</span></p></body></html>"))
        self.ava02.setStyleSheet(_translate("selectAccount", "border-color: white"))
        self.ava03.setStyleSheet(_translate("selectAccount", "border-color: white"))
        self.confirmButton.setText(_translate("selectAccount", "Next"))
        self.doneButton.setText(_translate("selectAccount", "Done"))
        # self.cancelButton.setText(_translate("selectAccount", "Cancel"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectAccount = QtWidgets.QWidget()
    ui = Ui_selectAccount()
    ui.setupUi(selectAccount)
    selectAccount.show()
    sys.exit(app.exec_())
