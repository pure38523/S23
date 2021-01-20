# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from accountCustom import Ui_selectAccount
from register import Ui_register_2
from mainWindow import Ui_MainWindow

import sqlite3

class Ui_login(object):
    username = ''
    def messageBoxShow(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def registerWindowShow(self):
        self.registerWindow = QtWidgets.QWidget()
        self.ui2 = Ui_register_2()
        self.ui2.setupUi(self.registerWindow)
        self.ui.hide()
        self.ui2.setPrevPage(self.ui)
        self.registerWindow.show()

    def accountWindowShow(self):
    
        self.accountWindow = QtWidgets.QWidget()
        self.uiAC = Ui_selectAccount()
        self.uiAC.setupUi(self.accountWindow)
        self.accountWindow.show()
        self.ui.hide()
    
    def loginWindowShow(self):
        self.MainWindow = QtWidgets.QWidget()
        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.MainWindow)
        self.uiMain.loginPage(self.ui)
        self.MainWindow.show()
        self.ui.hide()
    
    def skipMain(self):
        self.mainUI = QtWidgets.QMainWindow()
        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.mainUI)
        print("USERNAME:",self.username)
        # self.uiMain.getUserNameMain(self.username)
        self.mainUI.show()
        self.ui.hide()

    def loginCheck(self):
        print("boblancer", self.lineEdit_username.displayText())
        self.username = self.lineEdit_username.displayText()
        password = self.lineEdit_password.text()
        email = self.lineEdit_username.text()

        connection = sqlite3.connect("/Users/purepolachan/Desktop/ProjectSEP_final/Register.db")
            

        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ? OR EMAIL = ?", (self.username,password,email))
        if (len(result.fetchall()) > 0):
            self.accountWindowShow()

            self.uiAC.setUserName(self.username)
            # self.accountWindowShow()

        else:
            self.messageBoxShow("Invalid","Please enter valid username or password !")


    def setupUi(self, login):
        self.ui = login
        login.setObjectName("login")
        login.resize(1440, 781)
        font = QtGui.QFont()
        font.setFamily("Optima")
        login.setFont(font)
        login.setStyleSheet("background-image: url(:/Pic/Pic/bg.png);")
        self.label_logo = QtWidgets.QLabel(login)
        self.label_logo.setGeometry(QtCore.QRect(550, 150, 341, 221))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/Pic/Pic/logo_pic.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.lineEdit_username = QtWidgets.QLineEdit(login)
        self.lineEdit_username.setGeometry(QtCore.QRect(670, 440, 231, 41))
        font = QtGui.QFont()
        font.setFamily(".Muna PUA")
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("background:white;\n"
"color:black;\n"
"border-radius:10px;\n"
"\n"
"")
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(login)
        self.lineEdit_password.setGeometry(QtCore.QRect(670, 500, 231, 41))
        font = QtGui.QFont()
        font.setFamily(".Muna PUA")
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background:white;\n"
"color:black;\n"
"border-radius:10px;\n"
"\n"
"")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.idText = QtWidgets.QLabel(login)
        self.idText.setGeometry(QtCore.QRect(610, 440, 31, 41))
        self.idText.setObjectName("idText")
        self.passwordText = QtWidgets.QLabel(login)
        self.passwordText.setGeometry(QtCore.QRect(540, 510, 121, 41))
        self.passwordText.setObjectName("passwordText")
        self.loginButton = QtWidgets.QPushButton(login)
        self.loginButton.setGeometry(QtCore.QRect(780, 560, 113, 32))
        self.loginButton.setStyleSheet("#loginButton{\n"
"color:black;\n"
"background:white;\n"
"}\n"
"#loginButton:hover{\n"
"color:black;\n"
"background-color: rgb(216, 214, 217);\n"
"}")
        self.loginButton.setText("Login")
        self.loginButton.setObjectName("loginButton")
        ############# EVENT

        self.loginButton.clicked.connect(self.loginCheck)

        self.register_2 = QtWidgets.QPushButton(login)
        self.register_2.setGeometry(QtCore.QRect(700, 570, 61, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("#register_2{\n"
"border-color: rgb(9, 52, 56);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#register_2:hover{\n"
"\n"
"}")
        self.register_2.setObjectName("register_2")
        #############  EVENT

        self.register_2.clicked.connect(lambda:self.registerWindowShow())

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.lineEdit_username.setPlaceholderText(_translate("login", "Email / username"))
        self.idText.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">ID</span></p></body></html>"))
        self.passwordText.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Password</span></p><p><br/></p></body></html>"))
        self.register_2.setText(_translate("login", "Register"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
