# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movieInfo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import requests
from PIL import Image
from PIL.ImageQt import ImageQt
from io import BytesIO
import io
import functools

import urllib.request
from PyQt5.QtWebEngineWidgets import *  
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

class Ui_movieInfo(object):

    def prevPage(self,prev):
            self.prevPage = prev
    def goBack(self, event):
            self.ui.hide()
            self.prevPage.show()
            
    def getKey(self, nameKey):
            self.nameKey = nameKey
    def playVideos(self):
        # self.nameKey = nameKey
        # print("Self.namekey:", self.nameKey)

        self.app = QtWidgets.QWidget()
        self.Form = QtWidgets.QWidget()
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web.page().fullScreenRequested.connect(lambda request: request.accept())
        baseUrl = "local"
        htmlString = """
                <iframe width="600" height="500" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>
                """.format(self.nameKey)
        self.web.setHtml(htmlString, QUrl(baseUrl))
        self.web.show()

    def getMovieInfo(self, titleText, voteText, overviewText, companyText, posterImg):
            self.titleText = titleText
            self.voteText = voteText
            self.overviewText = overviewText
            self.companyText = companyText
            self.posterImg = posterImg

            url = posterImg
            data = urllib.request.urlopen(url).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            
            self.poster.setPixmap(QtGui.QPixmap(image))
            self.company.setText(self.companyText)
            self.title.setText(self.titleText)
            self.description.setText(self.overviewText)
            self.ratingText.setText(str(self.voteText))

    def setupUi(self, movieInfo):
        self.ui = movieInfo
        movieInfo.setObjectName("movieInfo")
        movieInfo.resize(1440, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(movieInfo.sizePolicy().hasHeightForWidth())
        movieInfo.setSizePolicy(sizePolicy)
        movieInfo.setMinimumSize(QtCore.QSize(1400, 900))
        movieInfo.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(movieInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1400, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.poster = QtWidgets.QLabel(self.centralwidget)
        self.poster.setGeometry(QtCore.QRect(120, 210, 371, 461))
        self.poster.setStyleSheet("background:white")
        self.poster.setScaledContents(1)
        self.poster.setText("")
        self.poster.setScaledContents(True)
        self.poster.setObjectName("poster")
        self.backIcon = QtWidgets.QLabel(self.centralwidget)
        self.backIcon.setGeometry(QtCore.QRect(40, 40, 61, 61))
        self.backIcon.setText("")
        self.backIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/return.png"))
        self.backIcon.setScaledContents(True)
        self.backIcon.setObjectName("backIcon")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, 0, 1451, 901))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/Pic/Pic/bg.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(260, 120, 951, 71))
        self.title.setObjectName("title")
        self.title.setStyleSheet("font-size:42pt; font-weight:600; color:#ffffff;")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(510, 290, 821, 231))
        self.description.setStyleSheet("\n"
"background: #000033;font-size:16pt; color:#ffffff;")
        self.description.setObjectName("description")
        self.description.setReadOnly(1)
        self.company = QtWidgets.QLabel(self.centralwidget)
        self.company.setGeometry(QtCore.QRect(510, 220, 831, 51))
        self.company.setStyleSheet("color: #000033")
        self.company.setObjectName("company")
        self.company.setStyleSheet("font-size:36pt; font-weight:600; font-style:italic; color:#000033;")
        self.square = QtWidgets.QLabel(self.centralwidget)
        self.square.setGeometry(QtCore.QRect(500, 210, 841, 61))
        self.square.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.square.setText("")
        self.square.setObjectName("square")
        self.filmIcon = QtWidgets.QLabel(self.centralwidget)
        self.filmIcon.setGeometry(QtCore.QRect(120, 80, 121, 121))
        self.filmIcon.setText("")
        self.filmIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/filmIcon.png"))
        self.filmIcon.setScaledContents(True)
        self.filmIcon.setObjectName("filmIcon")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(520, 580, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(44)
        font.setBold(True)
        font.setWeight(75)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("#playButton{\n"
"background: rgb(248, 255, 89);\n"
"color:#000033;\n"
"font-weight:36px;\n"
"font-style:bold;\n"
"border-radius:10px\n"
"}\n"
"\n"
"#playButton:hover{\n"
"background: rgb(234, 239, 23);\n"
"}")
        self.playButton.setObjectName("playButton")
        self.ratingIcon = QtWidgets.QLabel(self.centralwidget)
        self.ratingIcon.setGeometry(QtCore.QRect(1040, 570, 141, 111))
        self.ratingIcon.setText("")
        self.ratingIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/ratingIcon.png"))
        self.ratingIcon.setScaledContents(True)
        self.ratingIcon.setObjectName("ratingIcon")
        self.ratingText = QtWidgets.QLabel(self.centralwidget)
        self.ratingText.setGeometry(QtCore.QRect(1200, 590, 131, 101))
        self.ratingText.setStyleSheet(" font-size:36pt; font-weight:600;color:white;\n"
"font-weight:34px")
        self.ratingText.setObjectName("ratingText")
        self.background.raise_()
        self.square.raise_()
        self.poster.raise_()
        self.backIcon.raise_()
        self.title.raise_()
        self.description.raise_()
        self.company.raise_()
        self.filmIcon.raise_()
        self.playButton.raise_()
        self.ratingIcon.raise_()
        self.ratingText.raise_()
        movieInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(movieInfo)
        QtCore.QMetaObject.connectSlotsByName(movieInfo)

        self.playButton.clicked.connect(self.playVideos)
        self.backIcon.mousePressEvent = self.goBack
        

    def retranslateUi(self, movieInfo):
        _translate = QtCore.QCoreApplication.translate
        movieInfo.setWindowTitle(_translate("movieInfo", "MainWindow"))
        self.title.setText(_translate("movieInfo", "<html><head/><body><p><span style=\" font-size:42pt; font-weight:600; color:#ffffff;\">Title</span></p></body></html>"))
        self.description.setHtml(_translate("movieInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Description</span></p></body></html>"))
        self.company.setText(_translate("movieInfo", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#000033;\">Company</span></p></body></html>"))
        self.playButton.setText(_translate("movieInfo", "Play"))
        self.ratingText.setText(_translate("movieInfo", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">0.0</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    movieInfo = QtWidgets.QMainWindow()
    ui = Ui_movieInfo()
    ui.setupUi(movieInfo)
    movieInfo.show()
    sys.exit(app.exec_())
