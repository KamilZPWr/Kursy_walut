# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waluty.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(488, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.valueToConvert = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.valueToConvert.setObjectName("valueToConvert")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.valueToConvert)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.currency = QtWidgets.QLineEdit(self.centralwidget)
        self.currency.setObjectName("currency")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currency)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.calculate)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.convertedValue = QtWidgets.QLineEdit(self.centralwidget)
        self.convertedValue.setEnabled(True)
        self.convertedValue.setReadOnly(True)
        self.convertedValue.setClearButtonEnabled(False)
        self.convertedValue.setObjectName("convertedValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.convertedValue)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.currencyRate = QtWidgets.QLineEdit(self.centralwidget)
        self.currencyRate.setReadOnly(True)
        self.currencyRate.setObjectName("currencyRate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currencyRate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Waluty"))
        self.label.setText(_translate("MainWindow", "Kwota w PLN do przeliczenia:"))
        self.label_2.setText(_translate("MainWindow", "Trzyliterowy symbol waluty: "))
        self.calculate.setText(_translate("MainWindow", "Oblicz"))
        self.label_3.setText(_translate("MainWindow", "Kwota po kursie średnim:"))
        self.label_4.setText(_translate("MainWindow", "Kurs waluty:"))

