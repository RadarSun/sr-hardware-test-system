# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\liuya\Desktop\SR_work\miangui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1391, 659)
        Dialog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(1000, 120, 341, 151))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(1000, 280, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(540, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(1000, 320, 351, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label11.setFont(font)
        self.label11.setAutoFillBackground(False)
        self.label11.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(255, 0, 0);")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setWordWrap(False)
        self.label11.setObjectName("label11")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(980, 80, 401, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(980, 430, 401, 211))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton1.setGeometry(QtCore.QRect(50, 40, 141, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton1.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton2.setGeometry(QtCore.QRect(220, 40, 141, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(230, 120, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setAutoFillBackground(False)
        self.label2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setWordWrap(False)
        self.label2.setObjectName("label2")
        self.label9 = QtWidgets.QLabel(Dialog)
        self.label9.setGeometry(QtCore.QRect(90, 520, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label9.setFont(font)
        self.label9.setAutoFillBackground(False)
        self.label9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setWordWrap(False)
        self.label9.setObjectName("label9")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(90, 220, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setAutoFillBackground(False)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setWordWrap(False)
        self.label3.setObjectName("label3")
        self.label7 = QtWidgets.QLabel(Dialog)
        self.label7.setGeometry(QtCore.QRect(90, 420, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setAutoFillBackground(False)
        self.label7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setWordWrap(False)
        self.label7.setObjectName("label7")
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(90, 320, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setAutoFillBackground(False)
        self.label5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setWordWrap(False)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(Dialog)
        self.label6.setGeometry(QtCore.QRect(230, 320, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setAutoFillBackground(False)
        self.label6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setWordWrap(False)
        self.label6.setObjectName("label6")
        self.label10 = QtWidgets.QLabel(Dialog)
        self.label10.setGeometry(QtCore.QRect(230, 520, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label10.setFont(font)
        self.label10.setAutoFillBackground(False)
        self.label10.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label10.setAlignment(QtCore.Qt.AlignCenter)
        self.label10.setWordWrap(False)
        self.label10.setObjectName("label10")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(90, 120, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.label8 = QtWidgets.QLabel(Dialog)
        self.label8.setGeometry(QtCore.QRect(230, 420, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label8.setFont(font)
        self.label8.setAutoFillBackground(False)
        self.label8.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setWordWrap(False)
        self.label8.setObjectName("label8")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(230, 220, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setAutoFillBackground(False)
        self.label4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setWordWrap(False)
        self.label4.setObjectName("label4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 80, 331, 561))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label2_2 = QtWidgets.QLabel(Dialog)
        self.label2_2.setGeometry(QtCore.QRect(560, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_2.setFont(font)
        self.label2_2.setAutoFillBackground(False)
        self.label2_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setWordWrap(False)
        self.label2_2.setObjectName("label2_2")
        self.label1_2 = QtWidgets.QLabel(Dialog)
        self.label1_2.setGeometry(QtCore.QRect(420, 120, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setAutoFillBackground(False)
        self.label1_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setWordWrap(False)
        self.label1_2.setObjectName("label1_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 80, 561, 561))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label3_2 = QtWidgets.QLabel(Dialog)
        self.label3_2.setGeometry(QtCore.QRect(560, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_2.setFont(font)
        self.label3_2.setAutoFillBackground(False)
        self.label3_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_2.setWordWrap(False)
        self.label3_2.setObjectName("label3_2")
        self.label4_2 = QtWidgets.QLabel(Dialog)
        self.label4_2.setGeometry(QtCore.QRect(560, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_2.setFont(font)
        self.label4_2.setAutoFillBackground(False)
        self.label4_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_2.setWordWrap(False)
        self.label4_2.setObjectName("label4_2")
        self.label5_2 = QtWidgets.QLabel(Dialog)
        self.label5_2.setGeometry(QtCore.QRect(420, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_2.setFont(font)
        self.label5_2.setAutoFillBackground(False)
        self.label5_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_2.setWordWrap(False)
        self.label5_2.setObjectName("label5_2")
        self.label1_3 = QtWidgets.QLabel(Dialog)
        self.label1_3.setGeometry(QtCore.QRect(420, 300, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setAutoFillBackground(False)
        self.label1_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setWordWrap(False)
        self.label1_3.setObjectName("label1_3")
        self.label3_3 = QtWidgets.QLabel(Dialog)
        self.label3_3.setGeometry(QtCore.QRect(560, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_3.setFont(font)
        self.label3_3.setAutoFillBackground(False)
        self.label3_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_3.setWordWrap(False)
        self.label3_3.setObjectName("label3_3")
        self.label4_3 = QtWidgets.QLabel(Dialog)
        self.label4_3.setGeometry(QtCore.QRect(560, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_3.setFont(font)
        self.label4_3.setAutoFillBackground(False)
        self.label4_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_3.setWordWrap(False)
        self.label4_3.setObjectName("label4_3")
        self.label2_3 = QtWidgets.QLabel(Dialog)
        self.label2_3.setGeometry(QtCore.QRect(560, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_3.setFont(font)
        self.label2_3.setAutoFillBackground(False)
        self.label2_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setWordWrap(False)
        self.label2_3.setObjectName("label2_3")
        self.label5_3 = QtWidgets.QLabel(Dialog)
        self.label5_3.setGeometry(QtCore.QRect(420, 420, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_3.setFont(font)
        self.label5_3.setAutoFillBackground(False)
        self.label5_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_3.setWordWrap(False)
        self.label5_3.setObjectName("label5_3")
        self.label3_4 = QtWidgets.QLabel(Dialog)
        self.label3_4.setGeometry(QtCore.QRect(830, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_4.setFont(font)
        self.label3_4.setAutoFillBackground(False)
        self.label3_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_4.setWordWrap(False)
        self.label3_4.setObjectName("label3_4")
        self.label2_4 = QtWidgets.QLabel(Dialog)
        self.label2_4.setGeometry(QtCore.QRect(830, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_4.setFont(font)
        self.label2_4.setAutoFillBackground(False)
        self.label2_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setWordWrap(False)
        self.label2_4.setObjectName("label2_4")
        self.label4_4 = QtWidgets.QLabel(Dialog)
        self.label4_4.setGeometry(QtCore.QRect(830, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_4.setFont(font)
        self.label4_4.setAutoFillBackground(False)
        self.label4_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_4.setWordWrap(False)
        self.label4_4.setObjectName("label4_4")
        self.label1_4 = QtWidgets.QLabel(Dialog)
        self.label1_4.setGeometry(QtCore.QRect(690, 300, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_4.setFont(font)
        self.label1_4.setAutoFillBackground(False)
        self.label1_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setWordWrap(False)
        self.label1_4.setObjectName("label1_4")
        self.label5_4 = QtWidgets.QLabel(Dialog)
        self.label5_4.setGeometry(QtCore.QRect(690, 420, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_4.setFont(font)
        self.label5_4.setAutoFillBackground(False)
        self.label5_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_4.setWordWrap(False)
        self.label5_4.setObjectName("label5_4")
        self.label2_5 = QtWidgets.QLabel(Dialog)
        self.label2_5.setGeometry(QtCore.QRect(830, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_5.setFont(font)
        self.label2_5.setAutoFillBackground(False)
        self.label2_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_5.setWordWrap(False)
        self.label2_5.setObjectName("label2_5")
        self.label5_5 = QtWidgets.QLabel(Dialog)
        self.label5_5.setGeometry(QtCore.QRect(690, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_5.setFont(font)
        self.label5_5.setAutoFillBackground(False)
        self.label5_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_5.setWordWrap(False)
        self.label5_5.setObjectName("label5_5")
        self.label4_5 = QtWidgets.QLabel(Dialog)
        self.label4_5.setGeometry(QtCore.QRect(830, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_5.setFont(font)
        self.label4_5.setAutoFillBackground(False)
        self.label4_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_5.setWordWrap(False)
        self.label4_5.setObjectName("label4_5")
        self.label3_5 = QtWidgets.QLabel(Dialog)
        self.label3_5.setGeometry(QtCore.QRect(830, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_5.setFont(font)
        self.label3_5.setAutoFillBackground(False)
        self.label3_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_5.setWordWrap(False)
        self.label3_5.setObjectName("label3_5")
        self.label1_5 = QtWidgets.QLabel(Dialog)
        self.label1_5.setGeometry(QtCore.QRect(690, 120, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_5.setFont(font)
        self.label1_5.setAutoFillBackground(False)
        self.label1_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_5.setWordWrap(False)
        self.label1_5.setObjectName("label1_5")
        self.label2_6 = QtWidgets.QLabel(Dialog)
        self.label2_6.setGeometry(QtCore.QRect(830, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_6.setFont(font)
        self.label2_6.setAutoFillBackground(False)
        self.label2_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_6.setWordWrap(False)
        self.label2_6.setObjectName("label2_6")
        self.label3_6 = QtWidgets.QLabel(Dialog)
        self.label3_6.setGeometry(QtCore.QRect(560, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_6.setFont(font)
        self.label3_6.setAutoFillBackground(False)
        self.label3_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_6.setWordWrap(False)
        self.label3_6.setObjectName("label3_6")
        self.label5_6 = QtWidgets.QLabel(Dialog)
        self.label5_6.setGeometry(QtCore.QRect(690, 590, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_6.setFont(font)
        self.label5_6.setAutoFillBackground(False)
        self.label5_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_6.setWordWrap(False)
        self.label5_6.setObjectName("label5_6")
        self.label2_7 = QtWidgets.QLabel(Dialog)
        self.label2_7.setGeometry(QtCore.QRect(560, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_7.setFont(font)
        self.label2_7.setAutoFillBackground(False)
        self.label2_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_7.setWordWrap(False)
        self.label2_7.setObjectName("label2_7")
        self.label4_6 = QtWidgets.QLabel(Dialog)
        self.label4_6.setGeometry(QtCore.QRect(830, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_6.setFont(font)
        self.label4_6.setAutoFillBackground(False)
        self.label4_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_6.setWordWrap(False)
        self.label4_6.setObjectName("label4_6")
        self.label3_7 = QtWidgets.QLabel(Dialog)
        self.label3_7.setGeometry(QtCore.QRect(830, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_7.setFont(font)
        self.label3_7.setAutoFillBackground(False)
        self.label3_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_7.setWordWrap(False)
        self.label3_7.setObjectName("label3_7")
        self.label4_7 = QtWidgets.QLabel(Dialog)
        self.label4_7.setGeometry(QtCore.QRect(560, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_7.setFont(font)
        self.label4_7.setAutoFillBackground(False)
        self.label4_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_7.setWordWrap(False)
        self.label4_7.setObjectName("label4_7")
        self.label1_6 = QtWidgets.QLabel(Dialog)
        self.label1_6.setGeometry(QtCore.QRect(420, 470, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_6.setFont(font)
        self.label1_6.setAutoFillBackground(False)
        self.label1_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_6.setWordWrap(False)
        self.label1_6.setObjectName("label1_6")
        self.label1_7 = QtWidgets.QLabel(Dialog)
        self.label1_7.setGeometry(QtCore.QRect(690, 470, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_7.setFont(font)
        self.label1_7.setAutoFillBackground(False)
        self.label1_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_7.setWordWrap(False)
        self.label1_7.setObjectName("label1_7")
        self.label5_7 = QtWidgets.QLabel(Dialog)
        self.label5_7.setGeometry(QtCore.QRect(420, 590, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_7.setFont(font)
        self.label5_7.setAutoFillBackground(False)
        self.label5_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_7.setWordWrap(False)
        self.label5_7.setObjectName("label5_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SR 硬件生产测试系统"))
        self.label.setText(_translate("Dialog", "SR 硬件生产测试平台"))
        self.label11.setText(_translate("Dialog", "请连接扫描枪！"))
        self.groupBox_2.setTitle(_translate("Dialog", "当前状态与测试进度"))
        self.groupBox_3.setTitle(_translate("Dialog", "选项"))
        self.pushButton1.setText(_translate("Dialog", "生成PDF\n"
"写入数据库\n"
"打印标签"))
        self.checkBox.setText(_translate("Dialog", "自动运行"))
        self.pushButton2.setText(_translate("Dialog", "取消本次测试"))
        self.label2.setText(_translate("Dialog", "未连接"))
        self.label9.setText(_translate("Dialog", "功能固件版本"))
        self.label3.setText(_translate("Dialog", "控制器版本"))
        self.label7.setText(_translate("Dialog", "是否合格"))
        self.label5.setText(_translate("Dialog", "测试固件版本"))
        self.label6.setText(_translate("Dialog", "None"))
        self.label10.setText(_translate("Dialog", "None"))
        self.label1.setText(_translate("Dialog", "扫码枪状态"))
        self.label8.setText(_translate("Dialog", "None"))
        self.label4.setText(_translate("Dialog", "None"))
        self.groupBox.setTitle(_translate("Dialog", "硬件信息"))
        self.label2_2.setText(_translate("Dialog", "None"))
        self.label1_2.setText(_translate("Dialog", "IO"))
        self.groupBox_4.setTitle(_translate("Dialog", "外设检测情况"))
        self.label3_2.setText(_translate("Dialog", "None"))
        self.label4_2.setText(_translate("Dialog", "None"))
        self.label5_2.setText(_translate("Dialog", "Note:Null"))
        self.label1_3.setText(_translate("Dialog", "CAN"))
        self.label3_3.setText(_translate("Dialog", "None"))
        self.label4_3.setText(_translate("Dialog", "None"))
        self.label2_3.setText(_translate("Dialog", "None"))
        self.label5_3.setText(_translate("Dialog", "Note:Null"))
        self.label3_4.setText(_translate("Dialog", "None"))
        self.label2_4.setText(_translate("Dialog", "None"))
        self.label4_4.setText(_translate("Dialog", "None"))
        self.label1_4.setText(_translate("Dialog", "UART"))
        self.label5_4.setText(_translate("Dialog", "Note:Null"))
        self.label2_5.setText(_translate("Dialog", "None"))
        self.label5_5.setText(_translate("Dialog", "Note:Null"))
        self.label4_5.setText(_translate("Dialog", "None"))
        self.label3_5.setText(_translate("Dialog", "None"))
        self.label1_5.setText(_translate("Dialog", "SPI"))
        self.label2_6.setText(_translate("Dialog", "None"))
        self.label3_6.setText(_translate("Dialog", "None"))
        self.label5_6.setText(_translate("Dialog", "Note:Null"))
        self.label2_7.setText(_translate("Dialog", "None"))
        self.label4_6.setText(_translate("Dialog", "None"))
        self.label3_7.setText(_translate("Dialog", "None"))
        self.label4_7.setText(_translate("Dialog", "None"))
        self.label1_6.setText(_translate("Dialog", "其他1"))
        self.label1_7.setText(_translate("Dialog", "其他2"))
        self.label5_7.setText(_translate("Dialog", "Note:Null"))
