# OTP system for ATMAS
# run pip install twilio on terminal
import math
import random
import twilio
from twilio.rest import Client

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(string)

#Generating a 6 digit random OTP
otp = ""
for i in range(6):
    otp += string[math.floor(random.random()*length)]

print(otp)

# Your Account Sid and Auth Token from twilio.com/console
# WARNING! Don't share these credentials
account_sid = 'Enter your account SID from Twilio Console'
auth_token = 'Your secured auth token from console'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Your 6 digit OTP is: " + otp,
                     from_='Your paid number capable of sending SMS',
                     to='To any verified number added in your Twilio console'
                 )

print(message.sid)
