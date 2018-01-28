import smtplib
import re

from tkinter import Tk, Label, Button

class Root():
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def greet(self):
        print("Greetings!")



def sendMail():
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print(smtpObj.ehlo())    
    #print(smtpObj.starttls())

    userLogin = input("Please enter Your Login: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", userLogin):
        print("incorrect email adress ")
        userLogin = input("Please enter Your Login: ")

    userPassword = input("Please enter Your password: ")        
    smtpObj.login(userLogin,userPassword)
    smtpObj.sendmail(userLogin, userLogin,'Subject: Hej Koteczku\nKocham Cie. Z powazaniem, Lukaszek')
                    



if __name__ == "__main__":
    root = Tk()
    my_gui = Root(root)
    root.mainloop()
