import tkinter as tk
from apiCall import *
from Alert import *
import sys



class TkFrontSign:
    def __init__(self):
        self.wind = tk.Tk()
        self.wind.title('Signup')
        self.wind.geometry('400x250')
        self.wind.configure(bg='#0084ff')

        self.create_widgets()

    def create_widgets(self):
        name_label = tk.Label(self.wind, text='Name:', bg='#0084ff', fg='white')
        name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self.wind, bg='white')
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        username_label = tk.Label(self.wind, text='Username:', bg='#0084ff', fg='white')
        username_label.grid(row=1, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(self.wind, bg='white')
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        password_label = tk.Label(self.wind, text='Password:', bg='#0084ff', fg='white')
        password_label.grid(row=2, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.wind, bg='white', show='*')
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        signup_button = tk.Button(self.wind, text='Signup', bg='#0084ff', fg='white', command=self.signupLogic)
        signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        login_button = tk.Button(self.wind, text='Back to Login', bg='#0084ff', fg='white', command=self.closewindow)
        login_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='we')

class SignupPage(TkFrontSign):
    def signupLogic(self):
        x = "User Alreay Exist"
        y = "Something went very wrong."
        z = "Data inserted successfully"
        a = "Try Again"
        b= "Fill all Blanks"
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.data = []
        dataItem = {
            "name": name,
            "UserName" : username,
            "Password" : password
        }
        self.data.append(dataItem)
      
        if name== '' or  username == '' or password=='':
            self.AlertData(b,y)
        else:
            data = signUp(dataItem)
            print(data)
            if data == x:
                self.AlertData(x,y)
            elif z:
                x = "Congratulations"
                y = "You have SuccesFully Login"
                self.AlertData(x,y)
                
            else:
                self.AlertData(a,y)
                


    def run(self):
        self.wind.mainloop()

    def AlertData(Self,x,y):
        app = QApplication(sys.argv)
        custom_msg_box = CustomMessageBox()
        custom_msg_box.error(x,y)
        custom_msg_box.show()
        Self.OKButtonAlert()
        sys.exit(app.exec_())
  
    def OKButtonAlert(Self):
        custom_msg_box.button_clicked("OK")
        Self.closewindow()
        print("1")

    
        
    
    def closewindow(self):
        self.wind.destroy()
        self.openLoginwindow()
    
    def openLoginwindow(self):
        from loginGUI import LoginPage
        x = LoginPage()
        x.run()

if __name__ == "__main__":
    app = SignupPage()
    app.run()
