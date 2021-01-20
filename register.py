# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3




class Ui_register_2(object):

    def setPrevPage(self, prev):
        self.PrevPage = prev
    def messageBoxShow(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    
    def back(self):
        self.ui.hide()
        self.PrevPage.show()

        
    def signup(self):
        username = self.getUsernameText.text()
        password = self.getPasswordText.text()
        confirmpassword = self.getConPassText.text()
        activated = 0
        email = self.getEmailText.text()

        if username == '' or email == '':
                self.messageBoxShow('Sorry','Please fill the information')
        elif password != confirmpassword:
                self.messageBoxShow("Sorry","Passwords do not match")
        else:
        ####################      Database
                connection = sqlite3.connect("/Users/purepolachan/Desktop/ProjectSEP_final/Register.db")
                print("AA")
                data = connection.execute("INSERT INTO USERS VALUES (?, ?, ?, ?,NULL,NULL,NULL,?)",(username,password,confirmpassword,email,activated))
                connection.commit()
                connection.close()

                if (data):
                        self.messageBoxShow("Welcome", "You are successfully signed up")
                        self.ui.hide()
                        self.PrevPage.show()
        



    def setupUi(self, register_2):
        self.ui = register_2
        register_2.setObjectName("register_2")
        register_2.resize(1440, 900)
        register_2.setMinimumSize(QtCore.QSize(1440, 900))
        font = QtGui.QFont()
        font.setFamily("Optima")
        register_2.setFont(font)
        register_2.setStyleSheet("background-image: url(:/Pic/Pic/bg.png);")
        self.label_logo = QtWidgets.QLabel(register_2)
        self.label_logo.setGeometry(QtCore.QRect(40, 30, 171, 121))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/Pic/Pic/logo_pic.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_title = QtWidgets.QLabel(register_2)
        self.label_title.setGeometry(QtCore.QRect(230, 30, 801, 111))
        self.label_title.setObjectName("label_title")
        self.whiteBackground = QtWidgets.QLabel(register_2)
        self.whiteBackground.setGeometry(QtCore.QRect(-10, 170, 1451, 671))
        self.whiteBackground.setStyleSheet("background : white;\n"
"\n"
"")
        self.whiteBackground.setText("")
        self.whiteBackground.setObjectName("whiteBackground")
        self.getUsernameText = QtWidgets.QLineEdit(register_2)
        self.getUsernameText.setGeometry(QtCore.QRect(170, 280, 231, 31))
        self.getUsernameText.setStyleSheet("background: white;\n"
"color:black;\n"
"border: 1px solid black;")
        self.getUsernameText.setObjectName("getUsernameText")
        self.getPasswordText = QtWidgets.QLineEdit(register_2)
        self.getPasswordText.setGeometry(QtCore.QRect(170, 330, 231, 31))
        self.getPasswordText.setStyleSheet("background: white;\n"
"color:black;\n"
"border: 1px solid black;")
        self.getPasswordText.setObjectName("getPasswordText")
        self.getConPassText = QtWidgets.QLineEdit(register_2)
        self.getConPassText.setGeometry(QtCore.QRect(170, 380, 231, 31))
        self.getConPassText.setStyleSheet("background: white;\n"
"color:black;\n"
"border: 1px solid black;")
        self.getConPassText.setObjectName("getConPassText")
        self.getEmailText = QtWidgets.QLineEdit(register_2)
        self.getEmailText.setGeometry(QtCore.QRect(170, 430, 231, 31))
        self.getEmailText.setStyleSheet("background: white;\n"
"color:black;\n"
"border: 1px solid black;")
        self.getEmailText.setObjectName("getEmailText")
        self.signupButton = QtWidgets.QPushButton(register_2)
        self.signupButton.setGeometry(QtCore.QRect(260, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.signupButton.setFont(font)
        self.signupButton.setStyleSheet("#signupButton{\n"
"color:white;\n"
"background-color: rgb(9, 52, 56);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#signupButton:hover{\n"
"color:white;\n"
"background: rgb(0, 107, 116);\n"
"}")
        self.signupButton.setObjectName("signupButton")
        self.cancelButton = QtWidgets.QPushButton(register_2)
        self.cancelButton.setGeometry(QtCore.QRect(150, 490, 71, 31))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("#cancelButton{\n"
"color:rgb(9, 52, 56);\n"
"background: white;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.cancelButton.setObjectName("cancelButton")
        self.usernameText = QtWidgets.QLabel(register_2)
        self.usernameText.setGeometry(QtCore.QRect(20, 280, 129, 21))
        self.usernameText.setAutoFillBackground(False)
        self.usernameText.setStyleSheet("background:white;color:black\n"
"")
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLabel(register_2)
        self.passwordText.setGeometry(QtCore.QRect(20, 330, 129, 31))
        self.passwordText.setAutoFillBackground(False)
        self.passwordText.setStyleSheet("background:white;color:black\n"
"")
        self.passwordText.setObjectName("passwordText")
        self.conPassText = QtWidgets.QLabel(register_2)
        self.conPassText.setGeometry(QtCore.QRect(20, 370, 129, 41))
        self.conPassText.setAutoFillBackground(False)
        self.conPassText.setStyleSheet("background:white;color:black\n"
"")
        self.conPassText.setObjectName("conPassText")
        self.emailText = QtWidgets.QLabel(register_2)
        self.emailText.setGeometry(QtCore.QRect(20, 430, 129, 21))
        self.emailText.setAutoFillBackground(False)
        self.emailText.setStyleSheet("background:white;color:black\n"
"")
        self.emailText.setObjectName("emailText")
        self.whiteBackground.raise_()
        self.label_logo.raise_()
        self.label_title.raise_()
        self.getUsernameText.raise_()
        self.getPasswordText.raise_()
        self.getConPassText.raise_()
        self.getEmailText.raise_()
        self.signupButton.raise_()
        self.cancelButton.raise_()
        self.usernameText.raise_()
        self.passwordText.raise_()
        self.conPassText.raise_()
        self.emailText.raise_()

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)
        self.signupButton.clicked.connect(self.signup)
        self.cancelButton.clicked.connect(self.back)


    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "Form"))
        self.label_title.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Welcome to our streaming platform</span></p></body></html>"))
        self.signupButton.setText(_translate("register_2", "Sign Up"))
        self.cancelButton.setText(_translate("register_2", "Cancel"))
        self.usernameText.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-weight:600;\">Username</span></p></body></html>"))
        self.passwordText.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-weight:600;\">Password</span></p></body></html>"))
        self.conPassText.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.emailText.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-weight:600;\">Email address</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_2 = QtWidgets.QWidget()
    ui = Ui_register_2()
    ui.setupUi(register_2)
    register_2.show()
    sys.exit(app.exec_())
