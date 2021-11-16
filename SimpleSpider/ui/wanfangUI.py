# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wanfang.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 40, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 140, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 90, 111, 41))
        self.pushButton_5.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(self.click1)
        self.pushButton_3.clicked.connect(self.click2)
        self.pushButton_4.clicked.connect(self.click3)
        self.pushButton_5.clicked.connect(self.click4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        os.chdir('D:\\scrapy\\wanfang\\wanfang')
        os.popen('scrapy crawl wanfang')

    def click1(self):
        
        os.chdir('D:\\scrapy\\wanfang\\wanfang\\output\\')
        os.system('python json_xls.py')
        pass

    def click2(self):
        path = 'D:\\scrapy\\wanfang\\wanfang\\output'
        os.system("explorer.exe %s" % path)

    def click3(self):
        path = 'D:\\scrapy\\wanfang\\wanfang\\show\\'
        os.chdir(path)
        os.system("python show.py")
    
    def click4(self):
        path = 'D:\\scrapy\\wanfang\\wanfang\\show\\'
        os.chdir(path)
        os.system("python echart.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "万方数据"))
        self.pushButton.setText(_translate("MainWindow", "开始爬取"))
        self.pushButton_2.setText(_translate("MainWindow", "格式转换"))
        self.pushButton_3.setText(_translate("MainWindow", "打开文件所在目录"))
        self.pushButton_4.setText(_translate("MainWindow", "词云生成"))
        self.pushButton_5.setText(_translate("MainWindow", "表格生成"))

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())