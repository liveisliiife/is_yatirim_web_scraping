import requests
from bs4 import BeautifulSoup
import re
import time

class Hisse:
    def __init__(self):
        self.dongu = True

    def program(self):
        secim = self.menu()

        if secim == "1":
            print("     Güncel fiyatlar     ".center(30,"*"),"\n")
            time.sleep(1)
            self.guncel_fiyat()

        elif secim == "2":
            print("     Künye Bilgileri     ".center(30,"*"),"\n")
            time.sleep(1)
            self.kunye()

        elif secim == "3":
            print("     Cari Değerler   ".center(30,"*"),"\n")
            time.sleep(1)
            self.carideger()

        elif secim == "4":
            print("     Getiri Bilgileri    ".center(30,"*"),"\n")
            time.sleep(1)
            self.getiri()

        elif secim == "5":
            print("     Endeks Ağırlık Oranları     ".center(30, "*"),"\n")
            time.sleep(1)
            self.dahil_oldugu_endeks()

        elif secim == "6":
            print("     Çıkış   ".center(30, "*"),"\n")
            time.sleep(1)
            self.exit()
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim) or len(secim) != 1:
                raise Exception("Lütfen 1 ve 6 aralığında bir değer giriniz")
        while True:
            try:
                secim = input("1- Güncel Fiyat\n2- Şirket Künyesi\n3- Cari Değerler\n4- Getiri Rakamları\n5- Şirketin Dahil Olduğu Endeksler\n6- Çıkış\n7- Seçiminiz: ")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(1)
            else:
                break
        return secim

    def guncel_fiyat(self):
        while True:
            try:
                hisse = input("Şirket Adını Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                html = requests.get(url).content
                parser = BeautifulSoup(html,"html.parser")
                fiyat = parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(hisse)}).parent.parent.find_all("td")
                bilgi1 = fiyat[1].string
                bilgi2 = fiyat[2].span.string
                bilgi3 = fiyat[3].string
                bilgi4 = fiyat[4].string
                bilgi5 = fiyat[5].string
                print(f"Son fiyat:   {bilgi1}\nDeğişim(%):   {bilgi2.lstrip()}\rDeğişim(TL):   {bilgi3}\nHacim(TL):   {bilgi4}\nHacim(Adet):   {bilgi5}\n")
            except Exception as hata:
                print(hata)
            else:
                break
        self.return_menu()

    def kunye(self):
        while True:
            try:
                hisse = input("Şirket Adını Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(hisse)
                html = requests.get(url).content
                parser = BeautifulSoup(html,"html.parser")
                kunye = parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}).find_all("tr")
                for i in kunye:
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1}:{bilgi2}")
            except Exception as hata:
                print(hata)
            else:
                break
        self.return_menu()

    def carideger(self):
        while True:
            try:
                hisse = input("Şirket Adını Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(hisse)
                html = requests.get(url).content
                parser = BeautifulSoup(html,"html.parser")
                carideger = parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}).find_all("tr")
                for i in carideger:
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1}:{bilgi2}")
            except Exception as hata:
                print(hata)
            else:
                break
        self.return_menu()

    def getiri(self):
        while True:
            try:
                hisse = input("Şirket Adını Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(hisse)
                html = requests.get(url).content
                parser = BeautifulSoup(html,"html.parser")
                getiri = parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}).find("table").find("tbody").find_all("tr")
                for i in getiri:
                    bilgi = i.find_all("td")
                    print(f"Birim:{bilgi[0].string}\nGünlük(%):{bilgi[1].string}\nHaftalık(%):{bilgi[2].string}\nAylık(%):{bilgi[3].string}\nYıl İçi Getiri(%):{bilgi[4].string}\n")

            except Exception as hata:
                print(hata)
            else:
                break
        self.return_menu()

    def dahil_oldugu_endeks(self):
        while True:
            try:
                hisse = input("Şirket Adını Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(hisse)
                html = requests.get(url).content
                parser = BeautifulSoup(html,"html.parser")
                endeksi = parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("tbody").find("tr").find_all("td")
                endeksi2 = parser.find("div", {"id": "ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("thead").find("tr").find_all("th")
                for i in range(0,len(endeksi)):
                    print(f"{endeksi2[i].string}:{endeksi[i].string}")

            except Exception as hata:
                print(hata)
            else:
                break
        self.return_menu()

    def exit(self):
        self.dongu = False
        exit()

    def return_menu(self):
        while True:
            x = input("Ana Menüye Dönmek İçin 1'e Çıkmak için 0'a basınız")
            if x == "1":
                self.program()
                time.sleep(1)
                break
            elif x == "0":
                self.exit()
                time.sleep(1)
                break
            else:
                print("Hatalı Bir Tuşa Bastınız")
                time.sleep(1)

sistem = Hisse()
while sistem.dongu:
    sistem.program()