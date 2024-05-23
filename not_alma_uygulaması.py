import colorama  # Basit renk kütüphanesi
import json  # NOTLAR'ı dosyaya yazmak ve dosyadan okumak için

# colorama kütüphanesini başlatır ve otomatik sıfırlama özelliğini etkinleştirir
colorama.init(autoreset=True)

# Her seferinde colorama.Fore yazmak yerine F değerine atıyoruz
F = colorama.Fore

RENKLER = {"cyan": F.CYAN, "red": F.RED,
           "green": F.GREEN, "blue": F.BLUE,
           "yellow": F.YELLOW, "magenta": F.MAGENTA}

# Notları saklayacağımız ana sözlük
VARSAYILAN_KATEGORI = "notlar"

NOTLAR = {
    VARSAYILAN_KATEGORI: {
        "renk": F.BLUE,
        "icerik": []
    }
}


def kategori_ekle():
    kategori = input("Kategori adı girin: ")

    if kategori in NOTLAR:
        print("Bu kategori zaten mevcut.")
        return

    # Mevcut renkleri kullanıcıya gösteriyoruz
    print(f"{F.CYAN}CYAN {F.RED}RED {F.GREEN}GREEN {F.BLUE}BLUE {F.YELLOW}YELLOW {F.MAGENTA}MAGENTA")
    secilen_renk = input("Kategori rengi girin (varsayılan: BLUE): ").lower() or "blue"

    renk = RENKLER.get(secilen_renk)

    if not renk:
        print(f"Geçersiz renk. Varsayılan {F.BLUE}BLUE{F.RESET} seçildi.")
        renk = F.BLUE

    NOTLAR[kategori] = {"renk": renk, "icerik": []}


def notlari_yazdir(numarali_goster=False):
    not_numarasi = 1

    for kategori, veri in NOTLAR.items():
        renk = veri["renk"]
        print(f"{renk}=== {kategori.title()} ===")
        for icerik in veri["icerik"]:
            if numarali_goster:
                print(f"{F.YELLOW}{not_numarasi}- ", end="")
            print(icerik)
            not_numarasi += 1
        print(f"{renk}---------------------")


def not_ekle():
    metin = input(F.YELLOW + "Not girin: ")

    print("Kategoriler:", ", ".join(NOTLAR.keys()))  # join() methodu ile anahtarları virgülle birleştirip yazdırıyoruz
    kategori = input("Kategori girin (varsayılan: " + VARSAYILAN_KATEGORI + "): ") or VARSAYILAN_KATEGORI

    if kategori not in NOTLAR:
        print(f"'{kategori}' bulunamadı! Varsayılan kategoriye ekleniyor...")
        kategori = VARSAYILAN_KATEGORI

    NOTLAR[kategori]["icerik"].append(metin)


def kategori_sil():
    print(", ".join(NOTLAR.keys()))
    kategori = input(F.YELLOW + "Silinecek kategoriyi seçin: ")

    if kategori not in NOTLAR:
        print(F.YELLOW + "Kategori bulunamadı.")
        return

    del NOTLAR[kategori]
    print(F.YELLOW + "Kategori silindi.")


def not_sil():
    notlari_yazdir(numarali_goster=True)

    x = int(input(F.YELLOW + "Hangi not silinsin? (numara girin): "))
    not_numarasi = 1

    for kategori in NOTLAR.keys():
        for not_ in NOTLAR[kategori]["icerik"]:
            if not_numarasi == x:
                NOTLAR[kategori]["icerik"].remove(not_)
                print(F.YELLOW + "Not silindi.")
                return
            not_numarasi += 1


def notlari_import_et():
    with open("notlar.json", "r") as f:
        return json.load(f)


def notlari_export_et():
    with open("notlar.json", "w") as f:
        json.dump(NOTLAR, f, indent=4)


def kategorileri_goster():
    print("0 -> Seçenekleri göster")
    print("1 -> Notlara bak")
    print("2 -> Yeni Kategori")
    print("3 -> Yeni Not ekle")
    print("4 -> Kategori Sil")
    print("5 -> Not Sil")
    print("6 -> Dışarı aktar")
    print("7 -> Içeri aktar")
    print("8 -> Çık")


kategorileri_goster()
while True:
    print()
    secim = input(F.YELLOW + "Seçenek girin: ")

    if secim == "0":
        kategorileri_goster()
    elif secim == "1":
        notlari_yazdir()
    elif secim == "2":
        kategori_ekle()
    elif secim == "3":
        not_ekle()
    elif secim == "4":
        kategori_sil()
    elif secim == "5":
        not_sil()
    elif secim == "6":
        notlari_export_et()
    elif secim == "7":
        NOTLAR.update(notlari_import_et())
    elif secim == "8":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek.")  # Varsayılan durum
