import tkinter as tk

class LoginPage:
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

        login_button = tk.Button(self.wind, text='Login', bg='#0084ff', fg='white', command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='we')

        signup_button = tk.Button(self.wind, text='Signup', bg='#0084ff', fg='white', command=self.signup)
        signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='we')

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f'Logging in with username: {username} and password: {password}')

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f'Signing up with username: {username} and password: {password}')

    def run(self):
        self.wind.mainloop()

if __name__ == "__main__":
    app = LoginPage()
    app.run()
