# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from movieInfo import Ui_movieInfo
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import requests
import pandas as panda
import functools

from PyQt5.QtWebEngineWidgets import *  
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

class Ui_searchWindow(object):
    poster_index= ''
    def prevPage(self, prev):
        self.prevPage = prev
    
    def goBack(self, event):
        self.ui.hide()
        self.prevPage.show()

    def getTrailerKey(self, movies, poster, titleText,overviewText,rateText,companyText):
            self.movies = movies
            self.poster = poster
            self.titleText = titleText
            self.overviewText = overviewText
            self.rateText = rateText
            self.companyText = companyText
        #     print("Movies in search:\n", movies)
    def VideoTrailer(self,event,source_object = None):
        name = self.movies[source_object]
        vote = self.rateText[source_object]
        overview = self.overviewText[source_object]
        title = self.titleText[source_object]
        company = self.companyText[source_object]
        poster = self.poster[source_object]


        self.movieinfo = QtWidgets.QMainWindow()
        self.result = Ui_movieInfo()
        self.result.setupUi(self.movieinfo)
        self.result.getMovieInfo(title, vote, overview, company,poster)
        self.result.prevPage(self.ui)
        self.result.getKey(name)
        self.ui.hide()
        self.movieinfo.show()

        print("NameK1:",name)

        # self.app = QtWidgets.QWidget()
        # self.Form = QtWidgets.QWidget()
        # self.web = QWebEngineView()
        # self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        # self.web.page().fullScreenRequested.connect(lambda request: request.accept())
        # baseUrl = "local"
        # htmlString = """
        #         <iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>
        #         """.format(name)
        # self.web.setHtml(htmlString, QUrl(baseUrl))
        # self.web.show()



    def Load_Picture(self,poster, searchText):
        for i in range (len(poster)):
                url = poster[i]
                data = urllib.request.urlopen(url).read()

                image = QtGui.QImage()
                image.loadFromData(data)
                if i == 0:
                        self.item1_1.setPixmap(QtGui.QPixmap(image))
                        poster_index ='0'
                elif i ==1:
                        self.item1_2.setPixmap(QtGui.QPixmap(image))
                        poster_index ='1'
                elif i==2:
                        self.item1_3.setPixmap(QtGui.QPixmap(image))
                        poster_index ='2'
                elif i==3:
                        self.item1_4.setPixmap(QtGui.QPixmap(image))
                        poster_index ='3'
                elif i==4:
                        self.item1_5.setPixmap(QtGui.QPixmap(image))
                        poster_index ='4'
                elif i==5:
                        self.item2_1.setPixmap(QtGui.QPixmap(image))
                        poster_index ='5'
                elif i==6:
                        self.item2_2.setPixmap(QtGui.QPixmap(image))
                        poster_index ='6'
                elif i==7:
                        self.item2_3.setPixmap(QtGui.QPixmap(image))
                        poster_index ='7'
                elif i==8:
                        self.item2_4.setPixmap(QtGui.QPixmap(image))
                        poster_index ='8'
                elif i==9:
                        self.item2_5.setPixmap(QtGui.QPixmap(image))
                        poster_index ='9'
                elif i==10:
                        self.item3_1.setPixmap(QtGui.QPixmap(image))
                        poster_index ='10'
                elif i==11:
                    self.item3_2.setPixmap(QtGui.QPixmap(image))
                    poster_index ='11'
                elif i==12:
                    self.item3_3.setPixmap(QtGui.QPixmap(image))
                    poster_index ='12'
                elif i==13:
                    self.item3_4.setPixmap(QtGui.QPixmap(image))
                    poster_index ='13'
                elif i==15:
                    self.item3_5.setPixmap(QtGui.QPixmap(image))
                    poster_index ='14'

        self.text.setText("Seach results: "+ searchText)

        



    def setupUi(self, searchWindow):
        # print("AA")
        self.ui = searchWindow
        searchWindow.setObjectName("searchWindow")
        searchWindow.resize(1440, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(searchWindow.sizePolicy().hasHeightForWidth())
        searchWindow.setSizePolicy(sizePolicy)
        searchWindow.setMinimumSize(QtCore.QSize(1400, 900))
        searchWindow.setStyleSheet("background-image: url(:/Pic/Pic/bg.png);")
        self.centralwidget = QtWidgets.QWidget(searchWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1400, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameTop = QtWidgets.QFrame(self.centralwidget)
        self.frameTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTop.setObjectName("frameTop")
        self.text = QtWidgets.QLabel(self.frameTop)
        self.text.setGeometry(QtCore.QRect(30, 130, 741, 41))
        self.text.setObjectName("text")
        self.text.setStyleSheet("font-size:36pt; font-weight:600; color:white")
        self.logo = QtWidgets.QLabel(self.frameTop)
        self.logo.setGeometry(QtCore.QRect(1150, 10, 231, 171))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/Pic/Pic/logo_pic.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.scrollArea = QtWidgets.QScrollArea(self.frameTop)
        self.scrollArea.setGeometry(QtCore.QRect(-20, 200, 1441, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -327, 1437, 944))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.row1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row1.setMinimumSize(QtCore.QSize(0, 300))
        self.row1.setObjectName("row1")
        self.item1_2 = QtWidgets.QLabel(self.row1)
        self.item1_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item1_2.setStyleSheet("background:white")
        self.item1_2.setText("")
        self.item1_2.setScaledContents(True)
        self.item1_2.setObjectName("item1_2")
        self.item1_1 = QtWidgets.QLabel(self.row1)
        self.item1_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item1_1.setStyleSheet("background:white")
        self.item1_1.setText("")
        self.item1_1.setScaledContents(True)
        self.item1_1.setObjectName("item1_1")
        self.item1_3 = QtWidgets.QLabel(self.row1)
        self.item1_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item1_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item1_3.setStyleSheet("background:white")
        self.item1_3.setText("")
        self.item1_3.setScaledContents(True)
        self.item1_3.setObjectName("item1_3")
        self.item1_4 = QtWidgets.QLabel(self.row1)
        self.item1_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item1_4.setStyleSheet("background:white")
        self.item1_4.setText("")
        self.item1_4.setScaledContents(True)
        self.item1_4.setObjectName("item1_4")
        self.item1_5 = QtWidgets.QLabel(self.row1)
        self.item1_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item1_5.setStyleSheet("background:white")
        self.item1_5.setText("")
        self.item1_5.setScaledContents(True)
        self.item1_5.setObjectName("item1_5")
        self.verticalLayout_2.addWidget(self.row1)
        self.row2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row2.setMinimumSize(QtCore.QSize(0, 300))
        self.row2.setObjectName("row2")
        self.item2_2 = QtWidgets.QLabel(self.row2)
        self.item2_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item2_2.setStyleSheet("background:white")
        self.item2_2.setText("")
        self.item2_2.setScaledContents(True)
        self.item2_2.setObjectName("item2_2")
        self.item2_1 = QtWidgets.QLabel(self.row2)
        self.item2_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item2_1.setStyleSheet("background:white")
        self.item2_1.setText("")
        self.item2_1.setScaledContents(True)
        self.item2_1.setObjectName("item2_1")
        self.item2_3 = QtWidgets.QLabel(self.row2)
        self.item2_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item2_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item2_3.setStyleSheet("background:white")
        self.item2_3.setText("")
        self.item2_3.setScaledContents(True)
        self.item2_3.setObjectName("item2_3")
        self.item2_4 = QtWidgets.QLabel(self.row2)
        self.item2_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item2_4.setStyleSheet("background:white")
        self.item2_4.setText("")
        self.item2_4.setScaledContents(True)
        self.item2_4.setObjectName("item2_4")
        self.item2_5 = QtWidgets.QLabel(self.row2)
        self.item2_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item2_5.setStyleSheet("background:white")
        self.item2_5.setText("")
        self.item2_5.setScaledContents(True)
        self.item2_5.setObjectName("item2_5")
        self.verticalLayout_2.addWidget(self.row2)
        self.row3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row3.setMinimumSize(QtCore.QSize(0, 300))
        self.row3.setStyleSheet("")
        self.row3.setObjectName("row3")
        self.item3_2 = QtWidgets.QLabel(self.row3)
        self.item3_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item3_2.setStyleSheet("background:white")
        self.item3_2.setText("")
        self.item3_2.setScaledContents(True)
        self.item3_2.setObjectName("item3_2")
        self.item3_1 = QtWidgets.QLabel(self.row3)
        self.item3_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item3_1.setStyleSheet("background:white")
        self.item3_1.setText("")
        self.item3_1.setScaledContents(True)
        self.item3_1.setObjectName("item3_1")
        self.item3_3 = QtWidgets.QLabel(self.row3)
        self.item3_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item3_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item3_3.setStyleSheet("background:white")
        self.item3_3.setText("")
        self.item3_3.setScaledContents(True)
        self.item3_3.setObjectName("item3_3")
        self.item3_4 = QtWidgets.QLabel(self.row3)
        self.item3_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item3_4.setStyleSheet("background:white")
        self.item3_4.setText("")
        self.item3_4.setScaledContents(True)
        self.item3_4.setObjectName("item3_4")
        self.item3_5 = QtWidgets.QLabel(self.row3)
        self.item3_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item3_5.setStyleSheet("background:white")
        self.item3_5.setText("")
        self.item3_5.setScaledContents(True)
        self.item3_5.setObjectName("item3_5")
        self.verticalLayout_2.addWidget(self.row3)
        self.verticalLayout_2.setStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.backIcon = QtWidgets.QLabel(self.frameTop)
        self.backIcon.setGeometry(QtCore.QRect(20, 10, 81, 71))
        self.backIcon.setText("")
        self.backIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/return.png"))
        self.backIcon.setScaledContents(True)
        self.backIcon.setObjectName("backIcon")
        self.verticalLayout.addWidget(self.frameTop)
        searchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(searchWindow)
        QtCore.QMetaObject.connectSlotsByName(searchWindow)

        # EVENT
        self.item1_1.mousePressEvent = functools.partial(self.VideoTrailer, source_object=0)
        self.item1_2.mousePressEvent = functools.partial(self.VideoTrailer, source_object=1)
        self.item1_3.mousePressEvent = functools.partial(self.VideoTrailer, source_object=2)
        self.item1_4.mousePressEvent = functools.partial(self.VideoTrailer, source_object=3)
        self.item1_5.mousePressEvent = functools.partial(self.VideoTrailer, source_object=4)
        self.item2_1.mousePressEvent = functools.partial(self.VideoTrailer, source_object=5)
        self.item2_2.mousePressEvent = functools.partial(self.VideoTrailer, source_object=6)
        self.item2_3.mousePressEvent = functools.partial(self.VideoTrailer, source_object=7)
        self.item2_4.mousePressEvent = functools.partial(self.VideoTrailer, source_object=8)
        self.item2_5.mousePressEvent = functools.partial(self.VideoTrailer, source_object=9)
        self.item3_1.mousePressEvent = functools.partial(self.VideoTrailer, source_object=10)
        self.item3_2.mousePressEvent = functools.partial(self.VideoTrailer, source_object=11)
        self.item3_3.mousePressEvent = functools.partial(self.VideoTrailer, source_object=12)
        self.item3_4.mousePressEvent = functools.partial(self.VideoTrailer, source_object=13)
        self.item3_5.mousePressEvent = functools.partial(self.VideoTrailer, source_object=14)

        self.backIcon.mousePressEvent = self.goBack

    def retranslateUi(self, searchWindow):
        _translate = QtCore.QCoreApplication.translate
        searchWindow.setWindowTitle(_translate("searchWindow", "MainWindow"))
        self.text.setText(_translate("searchWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Text</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchWindow = QtWidgets.QMainWindow()
    ui = Ui_searchWindow()
    ui.setupUi(searchWindow)
    searchWindow.show()
    sys.exit(app.exec_())
