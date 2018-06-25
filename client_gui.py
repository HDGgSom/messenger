# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientWidget(object):
    def setupUi(self, ClientWidget):
        ClientWidget.setObjectName("ClientWidget")
        ClientWidget.resize(252, 446)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sphere.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ClientWidget.setWindowIcon(icon)
        ClientWidget.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.formLayout = QtWidgets.QFormLayout(ClientWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ClientWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(ClientWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.listWidget = QtWidgets.QListWidget(ClientWidget)
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(ClientWidget)
        self.listWidget_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.listWidget_2)
        self.action234 = QtWidgets.QAction(ClientWidget)
        self.action234.setObjectName("action234")

        self.retranslateUi(ClientWidget)
        QtCore.QMetaObject.connectSlotsByName(ClientWidget)
        ClientWidget.setTabOrder(self.listWidget, self.listWidget_2)

    def retranslateUi(self, ClientWidget):
        _translate = QtCore.QCoreApplication.translate
        ClientWidget.setWindowTitle(_translate("ClientWidget", "Client Gui"))
        self.label.setText(_translate("ClientWidget", "Добавить контакт"))
        self.label_2.setText(_translate("ClientWidget", "Список контактов"))
        self.listWidget.setToolTip(_translate("ClientWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Используйте даблклик для добавления контактов</span></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("ClientWidget", "Контакт 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("ClientWidget", "Контакт 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("ClientWidget", "123"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.action234.setText(_translate("ClientWidget", "234"))

