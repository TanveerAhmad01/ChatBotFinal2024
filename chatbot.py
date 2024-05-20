import tkinter as tk

class ChatBotApp:
    def __init__(self):
        self.wind = tk.Tk()
        self.wind.title('ChatBot')
        self.wind.geometry('600x600')
        self.wind.configure(bg='#0084ff')
        self.xi = 0
        self.yi = 0
        
        self.create_widgets()

    def create_widgets(self):
        hcb_text = tk.Label(self.wind, height=2, width=14, bg='#0084ff', text='Tanveer ChatBot', font=('Impact', 20), fg='white')
        hcb_text.place(x=200, y=5)

        self.chat_bg = tk.Frame(self.wind, height=420, width=580, bg='#f5f5f5')
        self.chat_bg.place(x=10, y=80)

        entry_bg = tk.Frame(self.wind, height=60, width=500, bg='white')
        entry_bg.place(x=10, y=520)

        sendbtn_bg = tk.Frame(self.wind, height=60, width=65, bg='white')
        sendbtn_bg.place(x=525, y=520)

        self.user_entry = tk.Entry(entry_bg, width=32, bg='white', font=('Helvectica', 20), relief=tk.FLAT, border=0)
        self.user_entry.place(x=10, y=13)
        self.user_entry.insert(0, 'Enter message...')
        self.user_entry.config(fg='#5c5a5a')
        self.user_entry.bind("<FocusIn>", self.on_enter)
        self.user_entry.bind("<FocusOut>", self.on_leave)

        send_button = tk.Button(sendbtn_bg, height=1, width=3, bg='#0084ff', text='➤', font=('helvectica', 20),
                                activeforeground='white', fg='white', relief=tk.FLAT, border=0,
                                activebackground='#0084ff', command=self.send_message)
        send_button.place(x=5, y=4)

    def clear_message(self):
        self.yi = 0
        for widget in self.chat_bg.winfo_children():
            widget.destroy()

    def send_message(self):
        u = self.user_entry.get()
        user = tk.Label(self.chat_bg, height=1, width=64, bg='#a6a6a6', fg='black', text=u+' <You ', font=12, anchor='e')
        user.place(x=self.xi, y=self.yi)
        if 'hello' in u:
            bot = tk.Label(self.chat_bg, height=1, width=64, bg='white', fg='black', text=' Bot> Hello', font=12, anchor='w')
            bot.place(x=self.xi, y=self.yi + 25)
        elif 'how are you?' in u:
            bot = tk.Label(self.chat_bg, height=1, width=64, bg='white', fg='black', text=' Bot> Im fine', font=12, anchor='w')
            bot.place(x=self.xi, y=self.yi + 25)
        elif u == 'clear':
            self.clear_message()
        else:
            bot = tk.Label(self.chat_bg, height=1, width=64, bg='white', fg='black', text=' Bot> Do not understand you', font=12, anchor='w')
            bot.place(x=self.xi, y=self.yi + 25)
        self.yi += 50
        self.user_entry.delete(0, 'end')

    def on_enter(self, e):
        self.user_entry.delete(0, 'end')
        self.user_entry.config(fg='black')

    def on_leave(self, e):
        n = self.user_entry.get()
        self.user_entry.config(fg='#5c5a5a')
        if n == '' or n == ' ':
            self.user_entry.insert(0, 'Enter message...')
            self.user_entry.config(fg='#5c5a5a')

    def run(self):
        self.wind.mainloop()

if __name__ == "__main__":
    app = ChatBotApp()
    app.run()
