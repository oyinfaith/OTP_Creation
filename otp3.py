from tkinter import *
from twilio.rest import Client
import random
from tkinter import messagebox
import string

class OTP_Verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x420")
        self.configure(bg='white')
        self.resizable(0, 0)
        self.title("Motunrayo's One Time Password  🥰💗")
        self.email = input("Enter your email: ")
        self.generate_OTP()

    def generate_OTP(self):
        self.otp = ''.join(random.choices(string.digits, k=6))
        self.SendOtp_Message()

    def SendOtp_Message(self):
        self.client = Client('ACa2c20306dba3c3e34adf6b69a10464fe', 'cbb2da599fe1c1428d5a820bce68f1e6')
        self.client.messages.create(
            to='+2348168066237',
            from_='+14123019598',
            body=f'Your OTP is: {self.otp}'
        )

    def Labels(self):
        self.canvas = Canvas(self, bg='white', width=370, height=280)
        self.canvas.place(x=100, y=60)

        self.login_title = Label(self, text='OTP Verification', font='bold 20', bg='white', fg='red')
        self.login_title.place(x=210, y=90)

        self.user_name = Text(self, borderwidth=8, width=29, wrap='word', height=2, font='timeroman 12 bold', fg='red')
        self.user_name.place(x=160, y=160)

        self.submit = Button(self, text="Submit", fg="red", width=10, command=self.check_OTP, borderwidth=8)
        self.submit.place(x=208, y=240)

        self.resend_otp = Button(self, text="Resend OTP", fg="red", width=10, command=self.resend_OTP_message, borderwidth=8)
        self.resend_otp.place(x=320, y=240)

    def check_OTP(self):
        try:
            user_input = self.user_name.get(1.0, "end-1c")
            if user_input == self.otp:
                messagebox.showinfo("showinfo", "Login Success")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except ValueError:
            messagebox.showinfo("showinfo", "Invalid OTP")

    def resend_OTP_message(self):
        self.generate_OTP()
        self.SendOtp_Message()

if __name__ == "__main__":
    window = OTP_Verifier()
    window.Labels()
    window.mainloop()
