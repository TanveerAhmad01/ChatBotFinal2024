from PyQt5.QtWidgets import QApplication, QMessageBox

class CustomMessageBox:
    def __init__(self):
        self.msg_box = QMessageBox()

    def error(self,mesge,wrong):
        self.mesge = mesge
        self.wrong = wrong
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setText(f"{self.wrong}")
        self.msg_box.setInformativeText(f"{self.mesge}")
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.setDefaultButton(QMessageBox.Discard)
        self.msg_box.buttonClicked.connect(self.button_clicked)  # Connect buttonClicked signal
        self.msg_box.exec()

    def button_clicked(self, button):
        if button.text() == "Discard":
            print("Discard!")
        elif button.text() == "OK":
            print("OK!")

    def SuccessFully(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("SignUp")
        dlg.setText("SuccessFully SignUp Now Login")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.buttonClicked.connect(self.button_clicked) 
        dlg.exec()
        

    def loginSuccessFully(self, username):
        self.username = username
        dlg = QMessageBox()
        dlg.setWindowTitle("Login")
        dlg.setText(f"Welcome  {self.username}") 
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.buttonClicked.connect(self.button_clicked)
        dlg.exec()

        
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    custom_msg_box = CustomMessageBox()
    custom_msg_box.show()
    alert2 = CustomMessageBox()
    alert2.SuccessFully() 
    alert2.show()
    alert3 = CustomMessageBox()
    alert3.loginSuccessFully() 
    alert3.show()
    sys.exit(app.exec_())
