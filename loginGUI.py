import tkinter as tk
from apiCall import loginClient
from SignUpGUi import SignupPage
from Alert import *
import sys
from chatbot import *

class TkFrontLogin:
    def __init__(self):
        self.wind = tk.Tk()
        self.wind.title('Login')
        self.wind.geometry('400x200')
        self.wind.configure(bg='#0084ff')

        self.create_widgets()

    def create_widgets(self):
        username_label = tk.Label(self.wind, text='Username:', bg='#0084ff', fg='white')
        username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(self.wind, bg='white')
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(self.wind, text='Password:', bg='#0084ff', fg='white')
        password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.wind, bg='white', show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(self.wind, text='Login', bg='#0084ff', fg='white', command=self.LoginUsingAPI)
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        signup_button = tk.Button(self.wind, text='Signup', bg='#0084ff', fg='white', command=self.closeWindow)
        signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='we')


class LoginPage(TkFrontLogin):

    def LoginUsingAPI(self):
        UserName = self.username_entry.get()
        Password = self.password_entry.get()
        result = loginClient({"UserName": UserName, "Password": Password})
        print(result)
        if result == "Invalid username or password":
                x = "Invalid username or password"
                y = "Something went very wrong."
                app = QApplication(sys.argv)
                custom_msg_box = CustomMessageBox()
                custom_msg_box.error(x,y)
                custom_msg_box.show()
                sys.exit(app.exec_())
        else:
            
            for item in result: 
                for key, value in  item.items():
                    print(f'{key}: {value}')
            username = item.get('username')  
            app = QApplication(sys.argv)
            alert3 = CustomMessageBox()
            alert3.loginSuccessFully(username)
            self.OpenChatGUI(username)
            alert3.show()
            

    def signup(self):
        showScreen = SignupPage()
        showScreen.run()

    def OpenChatGUI(self,username):
        self.username = username
        ShowChatBot = ChatBotApp(username)
        ShowChatBot.create_widgets()
        self.wind.destroy()
        ShowChatBot.run()
        

    def run(self):
        self.wind.mainloop()


    def closeWindow(self):
        self.wind.destroy()  
        self.signup()  


if __name__ == "__main__":
    app = LoginPage()
    app.run()
    
    
