# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class LoginPage(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(800, 600)
        Dialog.setStyleSheet("background-color: rgb(202, 215, 239);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 110, 301, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginTitleLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setUnderline(True)
        self.loginTitleLabel.setFont(font)
        self.loginTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTitleLabel.setObjectName("loginTitleLabel")
        self.verticalLayout.addWidget(self.loginTitleLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.emailInput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.emailInput.setFont(font)
        self.emailInput.setStyleSheet("background-color: rgb(255,255,255);\n"
"")
        self.emailInput.setObjectName("emailInput")
        self.verticalLayout.addWidget(self.emailInput)
        self.passwordInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("background-color: rgb(255,255,255)")
        self.passwordInput.setObjectName("passwordInput")
        self.verticalLayout.addWidget(self.passwordInput)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.loginButton = QtWidgets.QPushButton(self.layoutWidget)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("background-color: rgb(137, 255, 128);\n"
"\n"
"\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.registerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerButton.setStyleSheet("background-color: rgb(255, 249, 141)")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet("background-color: rgb(246, 156,167)")
        self.exitButton.setCheckable(False)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.loginExplanationText = QtWidgets.QLabel(Dialog)
        self.loginExplanationText.setGeometry(QtCore.QRect(520, 550, 271, 41))
        self.loginExplanationText.setWordWrap(True)
        self.loginExplanationText.setObjectName("loginExplanationText")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginTitleLabel.setText(_translate("Dialog", "CP\'s BOOKS"))
        self.emailInput.setPlaceholderText(_translate("Dialog", "Email"))
        self.passwordInput.setPlaceholderText(_translate("Dialog", "Password"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.loginExplanationText.setText(_translate("Dialog", "Please Log In. If you do not have an account, press \"Register\" to create an account."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
