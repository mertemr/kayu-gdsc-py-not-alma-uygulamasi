import colorama
import json
import os

# colorama modülünü başlat
colorama.init(autoreset=True)

# Renkleri kullanabilmek için bir değişken
F = colorama.Fore

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

# Renkleri ekrana yazdıran fonksiyon
def renkleri_yazdir():
    print("Mevcut renkler:")
    for renk in RENKLER:
        print(f"{RENKLER[renk]}{renk}", end=" ")  # Renkli olarak yazdır
    print()

# Notları ekrana yazdıran fonksiyon
def notlari_yazdir():
    print("Kaydedilen notlar:")
    for i, not_ in enumerate(NOTLAR):
        print(f"{i + 1}. {not_['renk']}{not_['not']}")  # Notları renkli olarak yazdır

# Yeni bir not ekleyen fonksiyon
def not_ekle():
    not_ = input("Notunuzu girin: ")
    renkleri_yazdir()
    renk = input("Notunuzun rengini girin: ")
    if renk not in RENKLER:
        print(F.RED + "Hatalı renk")
        return
    NOTLAR.append({"renk": RENKLER[renk], "not": not_})
    print(F.GREEN + "Not eklendi!")

# Bir notu silen fonksiyon
def not_sil():
    notlari_yazdir()
    try:
        index = int(input("Silmek istediğiniz notun numarasını girin: ")) - 1
        NOTLAR.pop(index)
        print(F.GREEN + "Not silindi!")
    except (IndexError, ValueError):
        print(F.RED + "Hatalı numara")

# Notları bir dosyaya kaydeden fonksiyon
def notlari_kaydet():
    with open("notlar.json", "w") as f:
        json.dump(NOTLAR, f)
    print(F.GREEN + "Notlar kaydedildi!")

# Notları bir dosyadan yükleyen fonksiyon
def notlari_yukle():
    global NOTLAR
    
    if not os.path.exists("notlar.json"):
        return
    
    with open("notlar.json", "r") as f:
        NOTLAR = json.load(f)
    print(F.GREEN + "Notlar yüklendi!")

# Bir notun rengini değiştiren fonksiyon
def renk_degistir():
    notlari_yazdir()
    try:
        index = int(input("Rengini değiştirmek istediğiniz notun numarasını girin: ")) - 1
        renkleri_yazdir()
        yeni_renk = input("Yeni rengi girin: ")
        if yeni_renk not in RENKLER:
            print(F.RED + "Hatalı renk")
            return
        NOTLAR[index]["renk"] = RENKLER[yeni_renk]
        print(F.GREEN + "Notun rengi değiştirildi!")
    except (IndexError, ValueError):
        print(F.RED + "Hatalı numara")

# Kullanıcıya seçenekleri gösteren fonksiyon
def secenekleri_goster():
    print("1 -> Notları Göster")
    print("2 -> Not Ekle")
    print("3 -> Not Sil")
    print("4 -> Renk Değiştir")
    print("5 -> Seçenekleri Göster")
    print("6 -> Dosyaya Kaydet")
    print("7 -> Dosyadan Yükle")
    print("0 -> Çıkış")

# Programın ana döngüsü
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
