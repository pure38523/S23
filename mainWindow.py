# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from searchWindow import Ui_searchWindow
from movieInfo import Ui_movieInfo

import sys
import random
# for api
import pandas as pd
import requests

import urllib.request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# for picture-
from PIL import Image
from PIL.ImageQt import ImageQt
from io import BytesIO
import io

import functools

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWebEngineWidgets import *  
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import tmdbsimple as tmdb
tmdb.API_KEY = '6b26f3633dc922246c0a8f1893ba0cb2'


import sqlite3


class Movie(object):
    def __init__(self):
        self.company = []
        self.title = []
        self.poster = []
        self.average_vote = []
        self.overview = []
        self.id = []
        self.movie_link = []
        self.Movie_key = []
        self.backdrop = []
   
    def get_Video_key(self):
        for i in self.id:
                url = "https://api.themoviedb.org/3/movie/{}/videos?api_key=6b26f3633dc922246c0a8f1893ba0cb2&language=en-US".format(i)
                r = requests.get(url)
                video = r.json()
                b = video['results']
                if b:
                        self.Movie_key.append(b[0]['key'])
        print(self.Movie_key)

    def get_title(self,s):
        title = []
        overview = []
        vote = []
        company = []
        for i in s:
                url = "https://api.themoviedb.org/3/movie/{}?api_key=6b26f3633dc922246c0a8f1893ba0cb2&language=en-US".format(i['id'])
                r = requests.get(url)
                j = r.json()

                title.append(j['original_title'])
                overview.append(j['overview'])
                vote.append(j['vote_average'])
                data = j['production_companies']
                if data:
                        company.append(data[0]['name'])



        return title,overview,vote,company
                

    def get_Movie_link(self,s):
        movie_link = []
        poster_link = []
        for i in s:
                # print(i)
                url = "https://api.themoviedb.org/3/movie/{}/videos?api_key=6b26f3633dc922246c0a8f1893ba0cb2&language=en-US".format(i['id'])
                r = requests.get(url)
                video = r.json()
                b = video['results']
                if b:
                        # print(i['title'])

                        movie_link.append(b[0]['key'])
                        poster_link.append("https://image.tmdb.org/t/p/original"+i['poster_path'])
        return movie_link,poster_link
        
    def get_company(self):
        for i in self.id:
                url = "https://api.themoviedb.org/3/movie/{}?api_key=6b26f3633dc922246c0a8f1893ba0cb2&language=en-US".format(i)
                r = requests.get(url)
                company = r.json()
                self.title.append(company['original_title'])
                b = company['production_companies']
                if b:
                        self.company.append(b[0]['name'])
        print(self.company)


        

#     def get_vote(self,index):

    def get_movie_video(self,index):
        return "https://www.youtube.com/watch?v=/"+self.movie_link[index]
                        
    def get_Movie_backdrop(self,index):
        return "https://image.tmdb.org/t/p/original"+self.backdrop[index]
        
    def get_Movie_poster(self,index):
        return  "https://image.tmdb.org/t/p/original/"+self.poster[index]

    def get_popular_movie(self):
        self.id = []
        pages = random.randint(1,200)
        url = "https://api.themoviedb.org/3/movie/popular?api_key=6b26f3633dc922246c0a8f1893ba0cb2&language=en-US&page={}".format(pages)
        r = requests.get(url)
        popular = r.json()
        # print(popular['results'][0]['original_title'])
        a = popular['results']
        for i in range(16):
                self.average_vote.append(a[i]['vote_average'])
                self.overview.append(a[i]['overview'])
        #     print(a[i]['original_title'],a[i]['id'],a[i]['poster_path'])
                self.poster.append("https://image.tmdb.org/t/p/original"+a[i]['poster_path'])
                self.id.append(a[i]['id'])
                self.backdrop.append("https://image.tmdb.org/t/p/original"+a[i]['backdrop_path'])
        print(self.average_vote)
        # print(self.id)
        


M = Movie()
M.get_popular_movie()
M.get_Video_key()
M.get_company()
# print(M.get_Video_key)
# print(M.get_Movie_link)
class Ui_MainWindow(object):

    username = ''

    def getLogin(self,loginUI):
        self.loginUI = loginUI

    def loginPage(self, loginPage):
        self.loginPage = loginPage
        
    def signOut(self, event):
        # self.loginWindow = QtWidgets.QMainWindow()
        # self.result = Ui_movieInfo()
        # self.result.setupUi(self.loginWindow)
        # self.ui.hide()
        # self.loginWindow.show()
        self.uiMain.hide()
        self.loginPage.show()

    def getUserNameMain(self, userName):
        self.userName = userName

    def update(self, event):
            global M
            M.id = []
            print("Updated:")
            M.get_popular_movie()
            self.Poster_Pic()
            

    def Poster_Pic(self):
        BackUrl = M.backdrop[15]
        # TopUrl = M.poster[15]
        # data = urllib.request.urlopen(TopUrl).read()
        data2 = urllib.request.urlopen(BackUrl).read()
        # image = QtGui.QImage()
        image2 = QtGui.QImage()
        # image.loadFromData(data)
        image2.loadFromData(data2)
        # self.showPoster.setPixmap(QtGui.QPixmap(image))
        self.showBackdrop.setPixmap(QtGui.QPixmap(image2))
        for i in range (0,15):
                url = M.poster[i]
                data = urllib.request.urlopen(url).read()

                image = QtGui.QImage()
                image.loadFromData(data)
                if i == 0:
                        self.item1_1.setPixmap(QtGui.QPixmap(image))
                elif i ==1:
                        self.item1_2.setPixmap(QtGui.QPixmap(image))
                elif i==2:
                        self.item1_3.setPixmap(QtGui.QPixmap(image))
                elif i==3:
                        self.item1_4.setPixmap(QtGui.QPixmap(image))
                elif i==4:
                        self.item1_5.setPixmap(QtGui.QPixmap(image))
                elif i==5:
                        self.item2_1.setPixmap(QtGui.QPixmap(image))
                elif i==6:
                        self.item2_2.setPixmap(QtGui.QPixmap(image))
                elif i==7:
                        self.item2_3.setPixmap(QtGui.QPixmap(image))
                elif i==8:
                        self.item2_4.setPixmap(QtGui.QPixmap(image))
                elif i==9:
                        self.item2_5.setPixmap(QtGui.QPixmap(image))
                elif i==10:
                        self.item3_1.setPixmap(QtGui.QPixmap(image))
                elif i==11:
                        self.item3_2.setPixmap(QtGui.QPixmap(image))
                elif i==12:
                        self.item3_3.setPixmap(QtGui.QPixmap(image))
                elif i==13:
                        self.item3_4.setPixmap(QtGui.QPixmap(image))
                elif i==14:
                        self.item3_5.setPixmap(QtGui.QPixmap(image))

    def VideoTrailer(self,event,source_object = None):
        name  = M.Movie_key[source_object]
        print(name)
        vote = M.average_vote[source_object]
        overview = M.overview[source_object]
        title = M.title[source_object]
        company = M.company[source_object]
        poster = M.poster[source_object]

        self.movieinfo = QtWidgets.QMainWindow()
        self.result = Ui_movieInfo()
        self.result.setupUi(self.movieinfo)
        self.result.getMovieInfo(title, vote, overview, company,poster)
        self.result.getKey(name)
        self.result.prevPage(self.uiMain)
        self.uiMain.hide()
        self.movieinfo.show()


        



    def Search(self):
        ids = []
        global M
        search_text = self.searchBox.text()
        print(search_text)

        search = tmdb.Search()
        r = search.movie(query = search_text)
        for s in (search.results):
            ids.append(s)
        # print(ids)

        title,overview,vote,company = M.get_title(ids)


        movies,posters = M.get_Movie_link(ids)
        
        
        self.window = QtWidgets.QMainWindow()
        result1 = Ui_searchWindow()
        result1.setupUi(self.window)
        result1.Load_Picture(posters, search_text)
        result1.getTrailerKey(movies,posters,title,overview,vote,company)
        result1.prevPage(self.uiMain)
        self.window.show()
        self.uiMain.hide()

        
        

    def getUserInfo(self):
        self.getUserNameMain(self.userName)
        connection = sqlite3.connect("/Users/purepolachan/Desktop/ProjectSEP_final/Register.db")
        c = connection.cursor()
        c.execute("SELECT USERAKA,USERCOLOR,USERAVATAR FROM USERS WHERE USERNAME=?",(self.userName,))
        print("username:",self.userName)
        data = c.fetchall()
        print("data:",data)
        picture_color = data[0][1]
        picture_avatar = data[0][2]
        nameAka = data[0][0]
        print("color :", picture_color)
        print("avatar :", picture_avatar)
        self.profileName.setText(nameAka)
        self.profilePic.setStyleSheet("background:"+picture_color)
        self.profilePic.setPixmap(QtGui.QPixmap(":/Pic/Pic/"+picture_avatar+".png"))

  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.uiMain = MainWindow
        MainWindow.resize(1440, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 900))
        MainWindow.setStyleSheet("background-image: url(:/Pic/Pic/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.profilePic = QtWidgets.QLabel(self.frameTop)
        self.profilePic.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.profilePic.setStyleSheet("background:white")
        self.profilePic.setText("")
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName("profilePic")
        self.profileName = QtWidgets.QLabel(self.frameTop)
        self.profileName.setGeometry(QtCore.QRect(110, 30, 271, 41))
        self.profileName.setObjectName("profileName")
        self.profileName.setStyleSheet("font-size:36pt; font-weight:600; color:#ffffff;")
        self.logo = QtWidgets.QLabel(self.frameTop)
        self.logo.setGeometry(QtCore.QRect(620, 0, 121, 91))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/Pic/Pic/logo_pic.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.searcIcon = QtWidgets.QLabel(self.frameTop)
        self.searcIcon.setGeometry(QtCore.QRect(970, 40, 41, 41))
        self.searcIcon.setText("")
        self.searcIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/searchIcon.png"))
        self.searcIcon.setScaledContents(True)
        self.searcIcon.setObjectName("searcIcon")
        self.searchBox = QtWidgets.QLineEdit(self.frameTop)
        self.searchBox.setGeometry(QtCore.QRect(1040, 40, 241, 41))
        self.searchBox.setStyleSheet("color:black;\n"
"background:white;\n"
"border-color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.searchBox.setInputMask("")
        self.searchBox.setObjectName("searchBox")
        self.searchBox.returnPressed.connect(self.Search)
        self.FrameMid = QtWidgets.QFrame(self.frameTop)
        self.FrameMid.setGeometry(QtCore.QRect(0, 110, 1401, 311))
        self.FrameMid.setStyleSheet("background: rgb(32, 67, 175);\n"
"border-radius:10px")
        self.FrameMid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameMid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameMid.setObjectName("FrameMid")
        # self.showPoster = QtWidgets.QLabel(self.FrameMid)
        # self.showPoster.setGeometry(QtCore.QRect(320, 30, 161, 241))
        # self.showPoster.setStyleSheet("border-radius:10px;")
        # self.showPoster.setFrameShape(QtWidgets.QFrame.Box)
        # self.showPoster.setScaledContents(1)
        # self.showPoster.setText("")
        # self.showPoster.setPixmap(QtGui.QPixmap(":/Pic/Pic/bg.png"))
        # self.showPoster.setObjectName("showPoster")
        self.showBackdrop = QtWidgets.QLabel(self.FrameMid)
        self.showBackdrop.setGeometry(QtCore.QRect(310, 10, 461, 291))
        self.showBackdrop.setStyleSheet("background:white;")
        self.showBackdrop.setScaledContents(1)
        self.showBackdrop.setText("")
        self.showBackdrop.setObjectName("showBackdrop")
        self.watchButton = QtWidgets.QPushButton(self.FrameMid)
        self.watchButton.setGeometry(QtCore.QRect(840, 170, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.watchButton.setFont(font)
        self.watchButton.setStyleSheet("#watchButton{\n"
"color: rgb(9, 52, 56);\n"
"background:white;\n"
"border-radius:10px}\n"
"\n"
"#watchButton:hover{\n"
"background:rgb(233, 231, 234)}")
        self.watchButton.setObjectName("watchButton")
        self.recIcon = QtWidgets.QLabel(self.FrameMid)
        self.recIcon.setGeometry(QtCore.QRect(830, 50, 81, 71))
        self.recIcon.setText("")
        self.recIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/icon.png"))
        self.recIcon.setScaledContents(True)
        self.recIcon.setObjectName("recIcon")
        self.reviewText = QtWidgets.QLabel(self.FrameMid)
        self.reviewText.setGeometry(QtCore.QRect(930, 50, 431, 61))
        self.reviewText.setObjectName("reviewText")
        self.tvText = QtWidgets.QLabel(self.FrameMid)
        self.tvText.setGeometry(QtCore.QRect(20, 50, 291, 191))
        self.tvText.setText("")
        self.tvText.setPixmap(QtGui.QPixmap(":/Pic/Pic/tvIcon.png"))
        self.tvText.setScaledContents(True)
        self.tvText.setObjectName("tvText")
        self.tvText.raise_()
        self.showBackdrop.raise_()
        self.watchButton.raise_()
        # self.showPoster.raise_()
        self.recIcon.raise_()
        self.reviewText.raise_()
        self.FrameMid.raise_()
        self.profilePic.raise_()
        self.profileName.raise_()
        self.logo.raise_()
        self.searcIcon.raise_()
        self.searchBox.raise_()
        self.verticalLayout.addWidget(self.frameTop)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1412, 944))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.row1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row1.setMinimumSize(QtCore.QSize(0, 300))
        self.row1.setObjectName("row1")
        self.item1_2 = QtWidgets.QLabel(self.row1)
        self.item1_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item1_2.setStyleSheet("background:white")
        self.item1_2.setScaledContents(1)
        self.item1_2.setText("")
        self.item1_2.setObjectName("item1_2")
        self.topic1 = QtWidgets.QLabel(self.row1)
        self.topic1.setGeometry(QtCore.QRect(0, 0, 100, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topic1.sizePolicy().hasHeightForWidth())
        self.topic1.setSizePolicy(sizePolicy)
        self.topic1.setObjectName("topic1")
        self.item1_1 = QtWidgets.QLabel(self.row1)
        self.item1_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item1_1.setStyleSheet("background:white")
        self.item1_1.setScaledContents(1)
        self.item1_1.setText("")
        self.item1_1.setObjectName("item1_1")
        self.item1_3 = QtWidgets.QLabel(self.row1)
        self.item1_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item1_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item1_3.setStyleSheet("background:white")
        self.item1_3.setScaledContents(1)
        self.item1_3.setText("")
        self.item1_3.setObjectName("item1_3")
        self.item1_4 = QtWidgets.QLabel(self.row1)
        self.item1_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item1_4.setStyleSheet("background:white")
        self.item1_4.setScaledContents(1)
        self.item1_4.setText("")
        self.item1_4.setObjectName("item1_4")
        self.next1 = QtWidgets.QPushButton(self.row1)
        self.next1.setGeometry(QtCore.QRect(1340, 40, 40, 240))
        self.next1.setObjectName("next1")
        self.prev1 = QtWidgets.QPushButton(self.row1)
        self.prev1.setGeometry(QtCore.QRect(0, 40, 40, 240))
        self.prev1.setObjectName("prev1")
        self.item1_5 = QtWidgets.QLabel(self.row1)
        self.item1_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item1_5.setStyleSheet("background:white")
        self.item1_5.setScaledContents(1)
        self.item1_5.setText("")
        self.item1_5.setObjectName("item1_5")
        self.verticalLayout_2.addWidget(self.row1)
        self.row2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row2.setMinimumSize(QtCore.QSize(0, 300))
        self.row2.setObjectName("row2")
        self.item2_2 = QtWidgets.QLabel(self.row2)
        self.item2_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item2_2.setStyleSheet("background:white")
        self.item2_2.setScaledContents(1)
        self.item2_2.setText("")
        self.item2_2.setObjectName("item2_2")
        self.topic2 = QtWidgets.QLabel(self.row2)
        self.topic2.setGeometry(QtCore.QRect(0, 0, 200, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topic2.sizePolicy().hasHeightForWidth())
        self.topic2.setSizePolicy(sizePolicy)
        self.topic2.setObjectName("topic2")
        self.item2_1 = QtWidgets.QLabel(self.row2)
        self.item2_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item2_1.setStyleSheet("background:white")
        self.item2_1.setScaledContents(1)
        self.item2_1.setText("")
        self.item2_1.setObjectName("item2_1")
        self.item2_3 = QtWidgets.QLabel(self.row2)
        self.item2_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item2_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item2_3.setStyleSheet("background:white")
        self.item2_3.setScaledContents(1)
        self.item2_3.setText("")
        self.item2_3.setObjectName("item2_3")
        self.item2_4 = QtWidgets.QLabel(self.row2)
        self.item2_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item2_4.setStyleSheet("background:white")
        self.item2_4.setScaledContents(1)
        self.item2_4.setText("")
        self.item2_4.setObjectName("item2_4")
        self.next2 = QtWidgets.QPushButton(self.row2)
        self.next2.setGeometry(QtCore.QRect(1340, 40, 40, 240))
        self.next2.setObjectName("next2")
        self.prev2 = QtWidgets.QPushButton(self.row2)
        self.prev2.setGeometry(QtCore.QRect(0, 40, 40, 240))
        self.prev2.setObjectName("prev2")
        self.item2_5 = QtWidgets.QLabel(self.row2)
        self.item2_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item2_5.setStyleSheet("background:white")
        self.item2_5.setScaledContents(1)
        self.item2_5.setText("")
        self.item2_5.setObjectName("item2_5")
        self.verticalLayout_2.addWidget(self.row2)
        self.row3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.row3.setMinimumSize(QtCore.QSize(0, 300))
        self.row3.setStyleSheet("")
        self.row3.setObjectName("row3")
        self.item3_2 = QtWidgets.QLabel(self.row3)
        self.item3_2.setGeometry(QtCore.QRect(350, 40, 200, 240))
        self.item3_2.setStyleSheet("background:white")
        self.item3_2.setScaledContents(1)
        self.item3_2.setText("")
        self.item3_2.setObjectName("item3_2")
        self.topic1_5 = QtWidgets.QLabel(self.row3)
        self.topic1_5.setGeometry(QtCore.QRect(0, 0, 200, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topic1_5.sizePolicy().hasHeightForWidth())
        self.topic1_5.setSizePolicy(sizePolicy)
        self.topic1_5.setObjectName("topic1_5")
        self.item3_1 = QtWidgets.QLabel(self.row3)
        self.item3_1.setGeometry(QtCore.QRect(100, 40, 200, 240))
        self.item3_1.setStyleSheet("background:white")
        self.item3_1.setScaledContents(1)
        self.item3_1.setText("")
        self.item3_1.setObjectName("item3_1")
        self.item3_3 = QtWidgets.QLabel(self.row3)
        self.item3_3.setGeometry(QtCore.QRect(600, 40, 200, 240))
        self.item3_3.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.item3_3.setStyleSheet("background:white")
        self.item3_3.setScaledContents(1)
        self.item3_3.setText("")
        self.item3_3.setObjectName("item3_3")
        self.item3_4 = QtWidgets.QLabel(self.row3)
        self.item3_4.setGeometry(QtCore.QRect(850, 40, 200, 240))
        self.item3_4.setStyleSheet("background:white")
        self.item3_4.setScaledContents(1)
        self.item3_4.setText("")
        self.item3_4.setObjectName("item3_4")
        self.next1_5 = QtWidgets.QPushButton(self.row3)
        self.next1_5.setGeometry(QtCore.QRect(1340, 40, 40, 240))
        self.next1_5.setObjectName("next1_5")
        self.prev1_5 = QtWidgets.QPushButton(self.row3)
        self.prev1_5.setGeometry(QtCore.QRect(0, 40, 40, 240))
        self.prev1_5.setObjectName("prev1_5")
        self.item3_5 = QtWidgets.QLabel(self.row3)
        self.item3_5.setGeometry(QtCore.QRect(1090, 40, 200, 240))
        self.item3_5.setStyleSheet("background:white")
        self.item3_5.setScaledContents(1)
        self.item3_5.setText("")
        self.item3_5.setObjectName("item3_5")
        self.verticalLayout_2.addWidget(self.row3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.logoutIcon = QtWidgets.QLabel(self.frameTop)
        self.logoutIcon.setGeometry(QtCore.QRect(1310, 20, 81, 71))
        self.logoutIcon.setText("")
        self.logoutIcon.setPixmap(QtGui.QPixmap(":/Pic/Pic/logoutIcon.png"))
        self.logoutIcon.setScaledContents(True)
        self.logoutIcon.setObjectName("logoutIcon")
        self.logoutIcon.raise_()

        self.logo.mousePressEvent = functools.partial(self.update)
        ### EVENT
        
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
        
        self.watchButton.mousePressEvent = functools.partial(self.VideoTrailer, source_object = 15)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.logoutIcon.mousePressEvent = functools.partial(self.signOut)
        self.getUserInfo()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profileName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Profile</span></p></body></html>"))
        self.searchBox.setPlaceholderText(_translate("MainWindow", "search details"))
        self.watchButton.setText(_translate("MainWindow", "Watch now"))
        self.reviewText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Top review movies</span></p></body></html>"))
        self.topic1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Popular</span></p></body></html>"))
        self.next1.setText(_translate("MainWindow", "PushButton"))
        self.prev1.setText(_translate("MainWindow", "PushButton"))
        self.topic2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Top charts</span></p></body></html>"))
        self.next2.setText(_translate("MainWindow", "PushButton"))
        self.prev2.setText(_translate("MainWindow", "PushButton"))
        self.topic1_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Most viewed</span></p></body></html>"))
        self.next1_5.setText(_translate("MainWindow", "PushButton"))
        self.prev1_5.setText(_translate("MainWindow", "PushButton"))
        
        self.Poster_Pic()
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
