import random

def tas_kagit_makas_sema_nur_aydogdu():
    print("Taş Kağıt Makas oyununa hoşgeldiniz.\n Kurallar:\nOyun 3 turdan oluşuyor ve ilk iki turu kazanan oyunu kazanır. \nMakas kağıdı keser. Kağıt taşı sarar. Taş makası kırar. \nOyun bittiğinde tekrar oynamak istiyorsanız \nterminale tas_kagit_makas_sema_nur_aydogdu() yazınız. \nOyundan çıkmak istiyorsanız çıkış yazınız.")

    tercih = ["evet", "hayır"]
    oyun = ["taş", "kağıt", "makas"]
    sizin_skorunuz = 0
    bilgisayarın_skoru = 0
    
    cevap = input("Oyunu oynamak istiyorsanız evet, istemiyorsanız hayır yazınız.\n")

    while cevap == "hayır":
        print("Daha sonra tekrar görüşürüz.")
        break
    while cevap == "evet":
        bil_tercih = random.choice(tercih)
        if bil_tercih == "hayır":
            print("Bilgisayar oynamak istemiyor.")
        if bil_tercih == "evet":
            print("Oyun Başlıyor.")
            kullanıcı = input("taş mı? kağıt mı? makas mı? Seçiniz.")
            if kullanıcı == "çıkış":
                break
            bilgisayar = random.choice(oyun)
            if kullanıcı == "taş":
                if bilgisayar == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İlk tur berabere.")
                if bilgisayar == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İlk turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İlk turu siz kazandınız.")
                    sizin_skorunuz += 1
            if kullanıcı == "kağıt":
                if bilgisayar == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İlk turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İlk tur berabere.")
                if bilgisayar == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İlk turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
            if kullanıcı == "makas":
                if bilgisayar == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İlk turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İlk turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İlk tur berabere.")
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                break
            print(f"Sizin skorunuz: {sizin_skorunuz} \nBilgisayarın skoru: {bilgisayarın_skoru}")
            print("İkinci Tur Başlıyor.")
            kullanıcı = input("taş mı? kağıt mı? makas mı? Seçiniz.")
            if kullanıcı == "çıkış":
                break
            bilgisayar2 = random.choice(oyun)
            if kullanıcı == "taş":
                if bilgisayar2 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İkinci tur berabere.")
                if bilgisayar2 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İkinci turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar2 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İkinci turu siz kazandınız.")
                    sizin_skorunuz += 1
            if kullanıcı == "kağıt":
                if bilgisayar2 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İkinci turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar2 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İkinci tur berabere.")
                if bilgisayar2 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İkinci turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
            if kullanıcı == "makas":
                if bilgisayar2 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("İkinci turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar2 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("İkinci turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar2 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("İkinci tur berabere.")
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                break
            print(f"Sizin skorunuz: {sizin_skorunuz} \nBilgisayarın skoru: {bilgisayarın_skoru}")
            if sizin_skorunuz == 2:
                break
            elif bilgisayarın_skoru == 2:
                break
            print("Üçüncü Tur Başlıyor.")
            kullanıcı = input("taş mı? kağıt mı? makas mı? Seçiniz.")
            if kullanıcı == "çıkış":
                break
            bilgisayar3 = random.choice(oyun)
            if kullanıcı == "taş":
                if bilgisayar3 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("Üçüncü tur berabere.")
                if bilgisayar3 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("Üçüncü turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar3 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("Üçüncü turu siz kazandınız.")
                    sizin_skorunuz += 1
            elif kullanıcı == "kağıt":
                if bilgisayar3 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("Üçüncü turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar3 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("Üçüncü tur berabere.")
                if bilgisayar3 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("Üçüncü turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
            elif kullanıcı == "makas":
                if bilgisayar3 == "taş":
                    print("Bilgisayar taşı seçti.")
                    print("Üçüncü turu bilgisayar kazandı.")
                    bilgisayarın_skoru += 1
                if bilgisayar3 == "kağıt":
                    print("Bilgisayar kağıdı seçti.")
                    print("Üçüncü turu siz kazandınız.")
                    sizin_skorunuz += 1
                if bilgisayar3 == "makas":
                    print("Bilgisayar makası seçti.")
                    print("Üçüncü tur berabere.")
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                break
        break
    
tas_kagit_makas_sema_nur_aydogdu()
    



"""Genel Bakış:
Bu projenin amacı, taş, kağıt, makas oyunu tasarlamaktır. 
Bu proje sayesinde sadece Python diline değil, aynı zamanda 
kodlamanın temel kurallarına da hakimiyetinizi geliştireceksiniz. 
Proje kodunuzu PEP-8 kurallarına göre yazmak ve proje icin 
yaratıcılığınızı ön plana çıkarmak önemlidir. """

"""Projenin Amaçları:
• Döngüler, koşullu ifadeler ve kullanıcı girişi gibi temel Python kavramlarını uygulamak.
• Mantıksal düşünme yeteneğinizi geliştirerek esnekliğe uyum sağlamak"""

"""Projenin Ana Hatları:
• Taş, kağıt, makas oyunu için bir fonksiyon oluşturacaksınız ve bu fonksiyonu 
tas_kagit_makas_ADINIZ_SOYADINIZ şeklinde adlandıracaksınız.
• Fonksiyonunuz sorunsuz çalışmalı ve Python terminali üzerinden 
tas_kagit_makas_ADINIZ_SOYADINIZ() şeklinde çalıştırılabilir olmalıdır.
• Oyun birden fazla turdan oluşacak ve ilk iki turu kazanan oyunun
galibi olacaktır.
• Her oyundan sonra hem kullanıcıya hem de bilgisayara başka bir oyun 
oynamak isteyip istemediği sorulacak. Eğer iki taraf da oynamak 
isterse oyun tekrarlanacaktır. (Bilgisayara nazik davranmayı unutmayın! ) 😊
• Unutmayın! Kodunuz çalışmazsa projeniz değerlendirmeye alınmayacaktır."""

"""Projeyi Oluştururken İzlenmesi Gerekenler:
1. Oyun Tanıtımı:
• Oyunun kurallarını açıklayan bir karşılama mesajı oluşturun.
• Kullanıcıya oyunun nasıl oynanacağını veya oyundan nasıl çıkılacağını bildirin.
• Oyunun turları üç seçenekten oluşmalıdır: Oyuncu kazanabilir, bilgisayar
kazanabilir veya beraberlik olabilir.
• İlk iki turu kazanan oyunu kazanır.
2. Oyun Kurulumu:
• Taş, kağıt ve makas seçeneklerinden oluşan bir liste tanımlayın. Daha fazlasi
can yakmaz. Unutmayin, hayal gücünüz size öne tasir.
• Oynanan oyun sayısı, oynanan tur sayısı, oyuncu galibiyetleri ve bilgisayar
galibiyetleri için sayaçlar başlatın.
3. Oyunun Ana Döngüsü:
• Oyunu oynanabilir kılmak için bir while döngüsü kullanın.
• Bu döngü içinde, her yeni oyun için tur ve galibiyet sayaçlarını sıfırlayın.
4. Turların Döngüsü:
• Oyuncu veya bilgisayar iki tur kazanana kadar başka bir while döngüsü kullanın.
• Oyuncudan üç seçenekten birini yapmasını isteyin, geçersiz bir opsiyon seçerse,
yeniden bir seçenek girmesini isteyin.
• Bilgisayarın seçimini rastgele oluşturun (ipucu: random modülünü kullanabilirsiniz).
• Seçimleri aldıktan sonra turun kazananını belirlemek için mantıksal 
operasyonlar veya temel if-else ifadelerini kullanın.
• İlk iki turu kazanan oyunu kazanacağından galibiyet sayaçlarını güncellemeyi
unutmayın.
• Her turun sonucunu ekrana yazdırın (ipucu: print() fonksiyonu tam da bu iş için).
5. Oyun Galibini Belirleyin:
• Turların döngüsü bittikten sonra (bir oyuncu iki tur kazandığında), oyunun
genel galibini belirleyin ve uygun mesajı gösterin.
6. Devam Etme İsteği:
• Kullanıcıya başka bir oyun oynamak isteyip istemediğini sorun.
• Bilgisayarın da oyuna devam etmek isteyip istemediğini sorun (rastgele bir
cevap oluşturabilirsiniz).
• Her iki taraf da oyuna devam etmek istiyorsa oyun devam etsin; fakat iki
taraftan biri devam etmek istemiyorsa oyun bitsin (ipucu:bunun için 
                                                   break kullanabilirsiniz).
• Her durum için uygun bir mesaj gösterin"""