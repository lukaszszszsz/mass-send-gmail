import smtplib
import re

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(smtpObj.ehlo())    
#print(smtpObj.starttls())


userLogin = input("Please enter Your Login: ")

while not re.match(r"[^@]+@[^@]+\.[^@]+", userLogin):
    print("incorrect email adress ")
    userLogin = input("Please enter Your Login: ")


userPassword = input("Please enter Your password: ") 

    
smtpObj.login(userLogin,userPassword)


smtpObj.sendmail(userLogin, userLogin,'Subject: So long.\nDear Me, so long and thanks for all the fish. \nSincerely, Me')
                
