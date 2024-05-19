from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SignUpGUi import SignUp
from Alert import CustomMessageBox
class Login_System(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login System")
        MainWindow.resize(511, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 140, 281, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 180, 131, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 210, 281, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.login_Button.setGeometry(QtCore.QRect(90, 280, 91, 31))
        self.login_Button.setStyleSheet("background-color: rgb(255, 85, 127);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";")
        self.login_Button.setObjectName("login_Button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 280, 61, 31))
        self.label_4.setObjectName("label_4")
        self.Signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.Signup_button.setGeometry(QtCore.QRect(270, 280, 91, 31))
        self.Signup_button.setStyleSheet("background-color: rgb(255, 85, 127);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 75 8pt \"MS Shell Dlg 2\";")
        self.Signup_button.setObjectName("Signup_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">UserName:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.login_Button.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.Signup_button.setText(_translate("MainWindow", "SignUp"))


 


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Login_System()
        self.ui.setupUi(self)
        self.ui.Signup_button.clicked.connect(self.on_Signup_button_clicked)
        self.ui.login_Button.clicked.connect(self.login_Button)
        self.signup_window = None
        name = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setPlainText(name)
        password = self.ui.textEdit_2.toPlainText()
        self.ui.textEdit_2.setPlainText(password)
        self.loginArray = []

    def on_Signup_button_clicked(self):
        print("Signup button clicked!")
        if self.signup_window is None:
            self.open_signup_window()
        else:
            print("Signup window is already open.")

    def open_signup_window(self):
        self.signup_window = SignUp()  
        self.signup_window.show()
        print("Signup window opened.")
        self.close() 

    def login_Button(self):
        username = self.ui.textEdit.toPlainText().strip()
        password = self.ui.textEdit_2.toPlainText().strip()
    
        if username == "" or password == "":
            print("Empty username or password")
            custom_msg_box = CustomMessageBox()
            # if custom_msg_box.button_clicked("Discard") == "Discard":
            #     print("discard")
            custom_msg_box.show()

        else:
            alertsucc = CustomMessageBox()
            alertsucc.loginSuccessFully("pasha")
           
            print("Login successful")
        data = {
            "UserName": username,
            "Password": password
        }
        self.loginArray.append(data)
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
