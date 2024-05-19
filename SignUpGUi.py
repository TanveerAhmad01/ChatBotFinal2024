

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Alert import CustomMessageBox

class signUp_System(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 511)
        MainWindow.setMinimumSize(QtCore.QSize(511, 473))
        MainWindow.setMaximumSize(QtCore.QSize(458, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(70, 70, 61, 21))
        self.namelabel.setObjectName("namelabel")
        self.nametextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.nametextEdit.setGeometry(QtCore.QRect(70, 100, 261, 31))
        self.nametextEdit.setObjectName("nametextEdit")
        self.namelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_2.setGeometry(QtCore.QRect(70, 150, 81, 21))
        self.namelabel_2.setObjectName("namelabel_2")
        self.usernametextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.usernametextEdit.setGeometry(QtCore.QRect(70, 180, 261, 31))
        self.usernametextEdit.setObjectName("usernametextEdit")
        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(70, 240, 91, 21))
        self.Password.setObjectName("Password")
        self.passwordtextEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordtextEdit_3.setGeometry(QtCore.QRect(70, 270, 261, 31))
        self.passwordtextEdit_3.setObjectName("passwordtextEdit_3")
        self.SignUp_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp_Button.setGeometry(QtCore.QRect(70, 330, 75, 23))
        self.SignUp_Button.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.SignUp_Button.setObjectName("SignUp_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.namelabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Name:</span></p></body></html>"))
        self.namelabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">UserName:</span></p></body></html>"))
        self.Password.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Password:</span></p><p><br/></p></body></html>"))
        self.SignUp_Button.setText(_translate("MainWindow", "SignUP"))
        

   

class SignUp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = signUp_System()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        
        self.ui.SignUp_Button.clicked.connect(self.call_press_button)
        name = self.ui.nametextEdit.toPlainText()
        self.ui.nametextEdit.setPlainText(name)
        username = self.ui.usernametextEdit.toPlainText()
        self.ui.usernametextEdit.setPlainText(username)
        text = self.ui.passwordtextEdit_3.toPlainText()
        self.ui.passwordtextEdit_3.setPlainText(text)


        self.x = []

        
    def call_press_button(self):
        name = self.ui.nametextEdit.toPlainText()
        print(name)
        username = self.ui.usernametextEdit.toPlainText()
        print(username)
        password = self.ui.passwordtextEdit_3.toPlainText()
        print(password)

        data = {
            "name"  : name,
            "UserName" : username,
            "Password" : password
        }
        self.x.append(data)
        
        if name.strip() == "" or password.strip() == "" or name.strip() == " ":
            print("Empty data")
            custom_msg_box = CustomMessageBox()
            custom_msg_box.show()
        else:
            print("Signup successfully")
            custom_msg_box = CustomMessageBox()
            custom_msg_box.SuccessFully()
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    signup_window = SignUp()
    signup_window.show()
    sys.exit(app.exec_())