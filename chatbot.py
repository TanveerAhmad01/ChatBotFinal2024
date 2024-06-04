import tkinter as tk
import json
import random

class frontEnd:
    def __init__(self, username):
        self.wind = tk.Tk()
        self.wind.title('ChatBot')
        self.wind.geometry('600x600')
        self.wind.configure(bg='#0084ff')
        self.xi = 0
        self.yi = 0
        self.username = username
        self.create_widgets()

        with open('dataSet.json') as file:
            self.data = json.load(file)

    def create_widgets(self,):
        
        hcb_text = tk.Label(self.wind, height=2, width=20, bg='#0084ff', text=f'{self.username} ChatBot', font=('Impact', 20), fg='white')
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

        self.chat_text = tk.Text(self.chat_bg, width=60, height=20, bg='#f5f5f5', font=('Helvectica', 15), relief=tk.FLAT, border=0)
        self.chat_text.place(x=10, y=10)

class ChatBotApp(frontEnd):

    def on_enter(self, event):
        self.user_entry.delete(0, 'end')
        self.user_entry.config(fg='black')

    def on_leave(self, event):
        if self.user_entry.get() == '':
            self.user_entry.insert(0, 'Enter message...')
            self.user_entry.config(fg='#5c5a5a')

    def send_message(self):
        user_input = self.user_entry.get()
        self.user_entry.delete(0, 'end')

        matched_intent = None
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                if pattern.lower() in user_input.lower():
                    matched_intent = intent
                    break

        if matched_intent:
            responses = matched_intent['responses']
            response = random.choice(responses)
            self.chat_text.insert('end', f'You: {user_input}\n')
            self.chat_text.insert('end', f'Bot: {response}\n\n')
        else:
            self.chat_text.insert('end', f'You: {user_input}\n')
            self.chat_text.insert('end', f'Bot: Sorry, I\'m not sure how to respond to that.\n\n')

    def run(self):
        self.wind.mainloop()

if __name__ == "__main__":
    app = ChatBotApp('User')
    app.run()