from PyQt5.QtWidgets import QApplication
from SignUpGUi import SignUp
from GUIdesign import Login_System,Login  # Assuming Login_System is the class containing your login_Button
import sys

def showloginUp():
    app = QApplication(sys.argv)  
    window = Login()
    window.show()
    sys.exit(app.exec_())
    
     
if __name__ == "__main__":
    showloginUp()
