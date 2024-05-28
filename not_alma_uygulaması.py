import json
import os.path

import colorama

# colorama modülünü başlat


# Renkleri kullanabilmek için bir değişken


# Renklerin isimlerini ve karşılık gelen colorama renklerini bir sözlükte tutuyoruz
RENKLER = {
    "mavi": F.BLUE,
    "cyan": F.CYAN,
    "yesil": F.GREEN,
    "magenta": F.MAGENTA,
    "kirmizi": F.RED,
    "beyaz": F.WHITE,
    "sari": F.YELLOW,
}

# Notları saklamak için bir liste oluşturuyoruz
NOTLAR = []

# Notlarımızı NOTLAR listesinde şu şekilde tutacağız:
"""
{
    "renk": RENKLER["white"],
    "not": ""
}
"""


def renkleri_yazdir():
    pass


def notlari_yazdir():
    print("Kaydedilen notlar:")
    for i, sozluk in enumerate(NOTLAR):
        print(f"{i + 1}. {sozluk['renk']}{sozluk['not']}")  # Notları renkli olarak yazdır


def not_ekle():
    pass


def not_sil():
    pass


def notlari_kaydet():
    pass


def notlari_yukle():
    pass


def renk_degistir():
    pass


def secenekleri_goster():
    print("""
    1 -> Notları Göster
    2 -> Not Ekle
    3 -> Not Sil
    4 -> Renk Değiştir
    5 -> Seçenekleri Göster
    6 -> Dosyaya Kaydet
    7 -> Dosyadan Yükle
    0 -> Çıkış
    """)


secenekleri_goster()

while True:
    secenek = input("> ")

    if secenek == "1":
        notlari_yazdir()
    elif secenek == "2":
        not_ekle()
    elif secenek == "3":
        not_sil()
    elif secenek == "4":
        renk_degistir()
    elif secenek == "5":
        secenekleri_goster()
    elif secenek == "6":
        notlari_kaydet()
    elif secenek == "7":
        notlari_yukle()
    elif secenek == "0":
        print("Çıkılıyor...")
        break
    else:
        print(F.RED + "Hatalı seçenek")
