import webbrowser
import json
import subprocess
import urllib3
import random
import passlib
import hashlib
import requests
import string
import os 
os.system("clear")
print("""
# _______  ________ __    __  ______                                              
#|       \|        |  \  |  \/      \                                             
#| $$$$$$$| $$$$$$$| $$  | $|  $$$$$$\                                            
#| $$  | $| $$__   | $$  | $| $$___\$$                                            
#| $$  | $| $$  \  | $$  | $$\$$    \                                             
#| $$  | $| $$$$$  | $$  | $$_\$$$$$$\                                            
#| $$__/ $| $$_____| $$__/ $|  \__| $$                                            
#| $$    $| $$     \\$$    $$\$$    $$                                            
# \$$$$$$$ \$$$$$$$$ \$$$$$$  \$$$$$$                                                                                                                       
            # __       ______  _______  ________ __    __ ________  ______        
           # |  \     /      \|       \|        |  \  |  |        \/      \       
            #| $$    |  $$$$$$| $$$$$$$| $$$$$$$| $$\ | $$\$$$$$$$|  $$$$$$\      
           # | $$    | $$  | $| $$__| $| $$__   | $$$\| $$   /  $$| $$  | $$      
           # | $$    | $$  | $| $$    $| $$  \  | $$$$\ $$  /  $$ | $$  | $$      
           # | $$    | $$  | $| $$$$$$$| $$$$$  | $$\$$ $$ /  $$  | $$  | $$      
            #| $$____| $$__/ $| $$  | $| $$_____| $$ \$$$$/  $$___| $$__/ $$      
            #| $$     \$$    $| $$  | $| $$     | $$  \$$|  $$    \\$$    $$      
             #\$$$$$$$$\$$$$$$ \$$   \$$\$$$$$$$$\$$   \$$\$$$$$$$$ \$$$$$$       
""")
print("""
###############################################
#1- İP ADRESİ SORGULAMA                       #
###############################################
#2- SQL WAF BYPASS                            #  
###############################################   
#3- SQL AÇIKLI SİTE DBS CEKME                 #
###############################################
#4- HEDEF İŞLETİM SİSTEMİ ÖĞRENME             #
###############################################
#5- MD5 ŞİFRELEYİCİ                           # 
###############################################
#6- ŞİFRE OLUŞTURUCU                          #
###############################################
#7- PORT TARAMASI(80-1)                       # 
###############################################
#8- TERMİNAL DİLİNİ TÜRKÇE YAP                #
###############################################
#9- MÜZİK DİNLE                               # 
###############################################
#10- YAPIMCI HAKKINDA BİLGİLER                #
###############################################

""")
    
vur = input("Seçim Yap Kanka -->")
if vur == "1" :
    target= input("[+]Target -> : ")
    data = subprocess.check_output(["curl",f"http://ip-api.com/json/" + target ]).decode("utf-8")
    json.loads(data)
    print("İp Adress   => " , json.loads(data)["query"])
    print("şehir => " , json.loads(data)["city"])
    print("Ülke  => " , json.loads(data)["country"])
    print("Posta Kodu  => " , json.loads(data)["zip"])
    print("Host   => " , json.loads(data)["isp"])
    print("Host   => " , json.loads(data)["org"])
    print("lat  => " , json.loads(data)["lat"])
    print("lat  => " , json.loads(data)["lon"])
    print("adres için  lat değeri ve lon değerini sayılarını google'a yazınız ")
if vur == "2":
   vur2 = input("Açıklı Url => ")
   os.system("sqlmap "+vur3 +" --forms --risk=3 --level=5 --tamper=space2comment --dbs --batch")
if vur == "3" :
   vur3 == input("site urlsi giriniz ..:")
   os.system("sqlmap "+vur3 +" --forms --risk=3 --level=5 --skip-waf -v 2 --dbs --batch")
if vur == "4" : 
    vur5 = input("İşletim sistemini öğrenmek istediğiniz ip adresini girin..:")
    os.system("sudo nmap -sS -O "+vur5)
if vur == "5" :
    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()        
    print(h2)
if vur == "6" : 
    def rastgele_sifre_uret(uzunluk):
        harfler =  string.ascii_letters + string.digits + string.punctuation
        sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
        return sonuc
    try : 
        karakter_sayı = int(input("KAC KARAKTER OLSUN İSTERSİN : "))
        print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı)) 
        print("ŞİFRENİZ : " + rastgele_sifre_uret(karakter_sayı))
    except ValueError:
        print("Lütfen sadece sayı girin!")       
if vur == "7" : 
   vur7 = input("trancak site url 'örnek.com' =>>")
   os.system("nmap "+vur7)
if vur == "8" :
    vur8 = input("Terminali Türkçe diline çevirmek istiyorsanız enterlayın ..:")
    os.system("setxkbmap tr")
if vur == "9" : 
    vur9 = input("dinlemek istediğiniz müziğin urlsini gir kanka..:") 
    os.system(" webbrowser.open_new"+ vur9)
if vur == "10" :
   print("""
   Adım Deus Lorenzo sanala 2016 da instagram sanalı ile başladım 2018 de kali linux ile heyecan
   saldığım hacking işlerine girdim uzun uğraş eğitim ,çabalarla ve dostlarımın sayesinde bu gün Bir Defacerim 
   ilgi alanlarım yazılım , siber güvenlik ve web penterest dir discordumu bırakıyorum sormak ve ya yazmak istediginiz seyleri yazabilirsiziniz
   DEUS LORENZO#6666
   """)