import tkinter as tk

class SignupPage:
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

        signup_button = tk.Button(self.wind, text='Signup', bg='#0084ff', fg='white', command=self.signup)
        signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='we')

    def signup(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f'Signing up with Name: {name}, Username: {username}, and Password: {password}')

    def run(self):
        self.wind.mainloop()

if __name__ == "__main__":
    app = SignupPage()
    app.run()
