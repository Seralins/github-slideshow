
giriş = """
(0)-!!!Çıkış Yap!!!

------ 5 TEMEL İŞLEM (+)------ 
(1)-Toplama
(2)-Çıkarma
(3)-Çarpma
(4)-Bölme
(5)-Yüzde hesaplama

------ ALAN HESAPLAMA ------ 

(6)-Alan Hesaplama(Dik Dörtgen)
(7)-Alan Hesaplama(Kare)
(8)-Alan Hesaplama(Yamuk)
(9)-Alan Hesaplama(Paralel Kenar)

------ HACİM HESAPLAMA ------ 

(10)-Hacim Hesaplama(Silindir)
(11)-Hacim Hesaplama(küp)
(12)-Hacim Hesaplama(Dikdörtgenler Prizması)
(13)-Hacim Hesaplama(Kare Prizma)
(14)-Hacim Hesaplama(Dik Prizma)

------ ÇEMBER VE DAİRE ------ 

(15)-Çember Ve Daire(Çevre)
(16)-Çember Ve Daire(Alan)
(17)-Çember Ve Daire(Dilim Alanı)
(18)-Çember Ve Daire(Yay Uzunluğu)

------ ÜÇGEN VE ÇOKGENLER ------ 

(19)-Üçgen(Alan)
(20)-Üçgen(Çevre)
(21)-Çokgenler(İç Açıların Toplamı)
(22)-Çokgenler(Dış Açıların Toplamı)

------ FAİZ VE OLASILIK ------ 

(23)-Faiz Hesaplama
(24)-Olasılık Hesaplama

------ SAAT PROBLEMLERİ ------ 

(25)-Saat Problemleri(Kollar Arasındaki Açı)

------ YOL PROBLEMLERİ ------ 

(26)-Yol Problemleri(Yolu Hesaplama)
(27)-Yol Problemleri(Hızı Hesaplama)
(28)-Yol Problemleri(Zamanı Hesaplama)
(29)-Yol Problemleri(Aynı Anda Zıt Yönde Hareketli)
(30)-Yol Problemleri(Aynı Anda Aynı Yönde Hareketli)

------ DENKLEMLER VE PROBLEMLER ------
(31)-Trigonometri
(32)-Pisagor Bağıntısı

------ ÇEVRE HESAPLAMA ------
(33)Çevre Hesaplama(Dikdörtgen)
(34)Çevre Hesaplama(Kare)

----- ÜSLÜ SAYILAR -----
(35) Üslü Sayılar(kuvvet hesaplama)


"""
import time
print(giriş)

anahtar = 1

while anahtar == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

    if soru == "0":
              print("^-^Tekrar görüşmek üzere eski dostum ^-^")
              time.sleep(1)
              anahtar = 0

    elif soru == "1":
        toplanan=float(input("Lütfen Toplama işlemi için sayı girişi yapınız: "))
        toplayan=float(input("Lütfen Toplama işlemi için sayı girişi yapınız: "))
        print(toplanan, "+", toplayan, "=", toplanan + toplayan)

    elif soru == "2":
        çıkarılan=float(input("Lütfen Çıkarma için sayı girişi yapınız: "))
        çıkan=float(input("Lütfen Çıkarma işlemi için sayı girişi yapınız: "))
        print(çıkarılan, "-", çıkan, "=", çıkarılan - çıkan)

    elif soru == "3":
        çarpılan=float(input("Lütfen Çarpma işlemi için sayı girişi yapınız: "))
        çarpan=float(input("Lütfen Çarpma işlemi için sayı girişi yapınız: "))
        print(çarpılan, "X", çarpan, "=", çarpılan * çarpan)

    elif soru == "4":
        bölünen=float(input("Lütfen Bölme İşlemi İçin Sayı Girişi Yapınız: "))
        bölen=float(input("Lütfen Bölme İşlemi İçin Sayı Girişi Yapınız: "))
        print(bölünen, "/", bölen, "=", bölünen/bölen)
        
    elif soru == "5":
        anasayı=float(input("Lütfen Yüzdesini Almak İstediğiniz Sayıyı Giriniz: "))
        yüzdesi=float(input("Lütfen Yüzdeyi Giriniz(örn= yüzde dört ise 4 şeklinde giriniz ): "))
        print(anasayı, "%", yüzdesi, "=", anasayı*yüzdesi/100)  
        

    elif soru == "6":
        dikkenar=float(input("Lütfen Alanını Hesaplamak İstediğiniz Dikdörtgenin Dik Kenar Uzunluğunu Giriniz: "))
        yankerar=float(input("Lütfen Alanını Hesaplamak İstediğiniz Dikdörtgenin Yan Kenar Uzunluğunu Giriniz: "))
        print(dikkenar, "ve", yankenar, "uzunluklarına sahip dikdörtgenin alanı", "=", dikkenar*yankkenar)
        
    elif soru == "7":
        dikkenar2=float(input("Lütfen Alanını Hesaplamak İstediğiniz Karenin Kenar Uzunluğunu Giriniz: "))
        print(dikkenar2, "Kenar Uzunluğuna Sahip Karenin Alanı", "=", dikkenar2*dikkenar2)
        
    elif soru == "8":
        alttaban=float(input("Lütfen Alanını Hesaplamak İstediğiniz Yamuğun Alt Taban Uzunluğunu Giriniz: "))
        üsttaban=float(input("Lütfen Alanını Hesaplamak İstediğiniz Yamuğun Üst Taban Uzunluğunu Giriniz: "))
        yükseklik=float(input("Lütfen Alanını Hesaplamak İstediğiniz Yamuğun Yüksekliğini Giriniz: "))
        print("Bilgilerini Girdiğiniz Yamuğun Alanı", "=", (alttaban+üsttaban).yükseklik/2)
        
    elif soru == "9":
        tabankenarı=float(input("Lütfen Alanını Hesaplamak İstediğiniz Paralel Kenarın Taban Kenarını Giriniz: "))
        tabanainenyükseklik=float(input("Lütfen Alanını Hesaplamak İstediğiniz Paralel Kenarın Tabana İnen Yüksekliğini Giriniz: "))
        print("Taban Kenarı", tabankenarı, "ve", "Tabana İnen Yüksekliği", tabanainenyükseklik, "Olan Paralel Kenarın Alanı", "=", tabankenarı*tabanainenyükseklik)
        
    elif soru == "10":
        tabanyarıçap=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Silindirin Taban Yarı Çapını Giriniz: "))
        yükseklik2=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Silindirin Yüksekliğini Giriniz: "))
        print("Bilgilerini Girdiğiniz Silindirin Hacmi", "=", 3.14*tabanyarıçap*tabanyarıçap*yükseklik2)
        
    elif soru == "11":
        küpkenar=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Küpün Kenar Uzunluğunu Giriniz: "))
        print("Bilgilerini Girdiğiniz Küpün Hacmi", "=", küpkenar*küpkenar*küpkenar)
        
    elif soru == "12":
        en=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Dikdörtgen Prizmasının Enini Giriniz: "))
        boy=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Dikdörtgen Prizmasının Boyunu Giriniz: "))
        yükseklik3=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Dikdörtgen Prizmasının Yüksekliğini Giriniz: "))
        print("Bilgilerini Girdiğiniz Dikdörtgen Prizmasının Hacmi", "=", en*boy*yükseklik3)
 
    elif soru == "13":
        tabankenarı=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Kare Prizmasının Taban Kenarını Giriniz: "))
        yükseklik4=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Karen Prizmasının Yüksekliğini Giriniz: "))
        print("Bilgilerini Girdiğiniz Kare Prizmasının Hacmi", "=", tabankenarı*tabankenarı*yükseklik4)
        
    elif soru == "14":
        tabanalanı=float(input("Lütfen Hacmini Hesaplamak İstediğiniz Dik Prizmanın Taban Alanını Giriiniz: "))
        yükseklik5=float(input("Lütfen Hacminin Hesaplamak İstediğiniz Dik Prizmanın Yüksekliğini Giriniz: "))
        print("Taban Alanı", tabanalanı, "Yüksekliği", yükseklik5, "Olan Dik Prizmanın Hacmi", "=", tabanalanı*yükseklik5)
        
    elif soru == "15":
        yarıçap=float(input("Lütfen Çevresini Hesaplamak İstediğiniz Yarıçapını Giriniz: "))
        print("Yarıçapını Girdiğiniz Daire Veya Çemberin Çevresi", "=",2*3.14*yarıçap)
        
    elif soru == "16":
        yarıçap2=float(input("Lütfen Alanını Hesaplamak İstediğiniz Dairenin Yarıçapını Giriniz: "))
        print("Yarıçapını Girdiğiniz Dairenin Alanı", "=", 3.14*yarıçap2*yarıçap2)
        
    elif soru == "17":
        yarıçap3=float(input("Lütfen Dilim Alanını Hesaplamak İstediğiniz Dairenin Yarıçapını Giriniz: "))
        merkezaçı=float(input("Lütfen Dilim Alanını Hesaplamak İstediğiniz Diliminin Arasında Kalan Merkez Açısını Giriniz: ")) 
        print("Yarıçapı", yarıçap3,"Merkez Açısı", merkezaçı, "Olan Dairenin Dilim Alanı", "=", 3.14*yarıçap3*yarıçap3*merkezaçı/360)
        
    elif soru == "18":
        yarıçap4=float(input("Lütfen Yayını Hesaplamak İstediğiniz Çemberin Yarıçapını Giriniz: "))
        merkezaçı2=float(input("Lütfen Yayını Hesaplamak İstediğiniz Çemberin Parçasının Diliminin Arasında Kalan Merkez Açısını Giriniz:"))      
        print("Yarıçapı", yarıçap4, "Merkez Açısı", merkezaçı2, "Olan Çemberin Yay Uzunluğu", "=", 2*3.14*yarıçap4*merkezaçı2/360)
    
    elif soru == "19":
        yükseklik6=float(input("Lütfen Alanını Hesaplamak İstediğiniz Üçgenin Yüksekliğini Giriniz: "))
        kenar=float(input("Lütfen Alanını Hesaplamak İstediğiniz Üçgenin Kenar Uzunluğunu Giriniz: "))
        print("Bilgilerini Girdiğiniz Üçgenin Alanı", "=", yükseklik6*kenar/2)   
        
    elif soru == "20":
        taban=float(input("Lütfen Çevresini Hesaplamak İstediğiniz Üçgenin Tabanını Giriniz: "))
        solkenar=float(input("Lütfen Çevresini Hesaplamak İstediğiniz Üçgenin Sol Kenarını Giriniz: "))
        sağkenar=float(input("Lütfen Çevresini Hesaplamak İstediğiniz Üçgenin Sağ Kenarını Giriniz: "))
        print("Bilgilerini Girdiğiniz Üçgenin Çevresi", "=", taban+solkenar+sağkenar)
        
    elif soru == "21":
        kenarsayısı=float(input("Lütfen İç Açılarını Toplamak İstediğiniz Çokgenin Kenar Sayısını Giriniz: "))
        print("Kenar Sayısını Girdiğiniz Çokgenin İç Açılarının Toplamı", "=", kenarsayısı-2*180)
        
    elif soru == "22":
        print("Tüm Çokgenlerin Dış Açılarının Toplamı 360 Derecedir. ^-^")
        
    elif soru == "23":
        anapara=float(input("Lütfen Faizini Hesaplamak İstediğiniz Ana Parayı Giriniz: "))
        faizyüzdesi=float(input("Lütfen Hesaplamak İstediğiniz Faizin Yüzdesini Giriniz: "))
        zaman=float(input("Lütfen Faiz Süresince Geçecek/Geçen Zamanı Giriniz: "))
        print("Verdiğiniz Bilgilere Göre Ana Paranız Olan", anapara, "Yüzde", faizyüzdesi, "Faiz İle", "Yılda", anapara*faizyüzdesi*zaman/100 , "Ayda", anapara*faizyüzdesi*zaman/1200, "Günde", anapara*faizyüzdesi*zaman/36000, "Faize Uğramıştır")
        
    elif soru == "24":
        istenendurum=float(input("Lütfen Hesaplamak İstediğiniz Olasılıkta İstenen Durum Sayısını Giriniz: "))
        tümdurum=float(input("Lütfen Hesaplamak İstediğiniz Olasılıktaki Tüm Durumların Sayısını Giriniz: "))
        print("Girdiğiniz Durumlara Göre Olasılığınız", "=", istenendurum/tümdurum)
        
    elif soru == "25":
        akrep=int(input("Lütfen Açıyı Hesaplamak İstediğiniz Saatte Akrebin Kaçı Göstediğini Giriniz(saat): "))
        yelkovan=int(input("Lütfen Açıyı Hesaplamak İstediğiniz Saatte Yelkovannın Kaçı Göstediğini Giriniz(dakika): "))
        print("Girdiğiniz Bilgilere Göre Akrep Ve Yelkovan Arasındaki Açı", "=", 30*akrep-5,5*yelkovan)
        
    elif soru == "26":
        hız=float(input("Lütfen Hesaplamak İstediğiniz Yoldan Geçen Aracın Hızını Giriniz: "))
        zaman2=float(input("Lütfen Hesaplamak İstediğiniz Yolgan Geçen Aracın Ne Kadar Sürede Hedafe Ulaştığını Giriniz: "))
        print("Aracın Geçtiği Yol", "=", hız*zaman2)
        
    elif soru == "27":
        yol=float(input("Lütfen Yolun Uzunluğunu Giriniz: "))
        zaman3=float(input("Lütfen Geçen Süreyi Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Hız", "=", yol/zaman3)
        
    elif soru == "28":
        yol2=float(input("Lütfen Yolun Uzunluğunu Giriniz: "))
        hız2=float(input("Lütfen Aracın Hızını Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Yolun Uzunluğu", "=", yol2/hız2)
        
    elif soru == "29":
        hız3=float(input("Lütfen İlk Aracın Hızını Giriniz: "))
        hız4=float(input("Lütfen İkinci Aracın Hızını Giriniz: "))
        zaman4=float(input("Lütfen Geçen Zamanı Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Yolun Uzunluğu", "=", (hız3+hız4)*zaman4)
    
    elif soru == "30":
        hız5=float(input("Lütfen İlk Aracın Hızını Giriniz: "))
        hız6=float(input("Lütfen İkinci Aracın Hızını Giriniz: "))
        zaman5=float(input("Lütfen Geçen Zamanı Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Yolun Uzunluğu", "=", (hız5-hız6)*zaman5)
        
    elif soru == "31":
        karşı=float(input("Lütfen Karşıyı Giriniz: "))
        komşu=float(input("Lütfen Komşuyu Giriniz: "))
        hipotenüs=float(input("Lütfen Hipotenüsü Giriniz: "))
        print("SinC", "=", karşı/hipotenüs)
        print("CosC", "=", komşu/hipotenüs)
        print("TanC", "=", karşı/komşu)
        print("CotC", "=", komşu/karşı)
        
    elif soru == "32":
        dikkenar3=float(input("Lütfen Dik Kenar Uzunluğun Giriniz: "))
        yankenar2=float(input("Lütfen Yan Kenar(Taban) Uzunluğunu Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Üçgenizin Pisagor Bağıntısı", "=", (dikkenar3*dikkenar3)+(yankenar2+yankenar2))
        
    elif soru == "33":
        uzunkenar=float(input("Lütfen Uzun Kenar Uzunluğunu Giriniz: "))
        kısakenar=float(input("Lütfen Kısa Kenar Uzunluğunu Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Dikdörtgenin Çevresi" , "=", 2*(uzunkenar+kısakenar))
        
    elif soru == "34":
        karekenar=float(input("Lütfen Kenar Uzunluğunu Giriniz: "))
        print("Girdiğiniz Bilgilere Göre Karenin Çevresi", "=", 4*karekenar)
        
    elif soru == "35":
        tabansayı=float(input("Lütfen Taban Sayıyı Giriniz: "))
        üssayı=float(input("Lütfen Üssayıyı Giriniz: "))
        print("Girdiğiniz taban sayının", üssayı, ". kuvveti", "=", tabansayı**üssayı)
    
    
    
    else:
        print("Hatalı Giriş Yaptınız. Lütfen Yapmak İstediğiniz İşlemin Numarasını Giriniz!")
        
