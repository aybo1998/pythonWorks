# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'irc2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(354, 500)
        self.sendButton = QtGui.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(270, 460, 84, 34))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.lineSend = QtGui.QLineEdit(Form)
        self.lineSend.setGeometry(QtCore.QRect(10, 460, 261, 34))
        self.lineSend.setObjectName(_fromUtf8("lineSend"))
        self.lineSend.returnPressed.connect(self.sendButton.click)
        self.chatBox = QtGui.QPlainTextEdit(Form)
        self.chatBox.setGeometry(QtCore.QRect(0, 10, 351, 411))
        self.chatBox.setReadOnly(True)
        self.chatBox.setObjectName(_fromUtf8("chatBox"))
        self.botMode = QtGui.QCheckBox(Form)
        self.botMode.setGeometry(QtCore.QRect(20, 430, 88, 22))
        self.botMode.setObjectName(_fromUtf8("botMode"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineSend, self.sendButton)
        Form.setTabOrder(self.sendButton, self.chatBox)
        Form.setTabOrder(self.chatBox, self.botMode)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Gnulug irc chat", None))
        self.sendButton.setText(_translate("Form", "Send", None))
        self.botMode.setText(_translate("Form", "Bot mode", None))

