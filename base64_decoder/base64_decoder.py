import base64


def base64_coz(veri):
    try:
        # Veriyi byte tipine çevirip decode ediyoruz
        cozulmus_byte = base64.b64decode(veri)
        # Metni utf-8 formatında stringe dönüştürüyoruz
        return cozulmus_byte.decode('utf-8')
    except Exception as e:
        return f"Hata: Geçersiz Base64 formatı! ({e})"


print("--- Base64 Decoder ---")
print("Programdan çıkmak için istediğiniz zaman 'exit64' yazıp Enter'a basabilirsiniz.\n")

# Sürekli sorması için sonsuz döngü başlatıyoruz
while True:
    girdi = input("Çözmek istediğin Base64 metnini yapıştır: ").strip()

    # Kullanıcı 'exit64' veya 'Exit64' girerse döngüden çık
    if girdi.lower() == 'exit64':
        print("Program kapatılıyor...!")
        break

    # Kullanıcı hiçbir şey yazmadan Enter'a basarsa pas geç, tekrar soracak
    if not girdi:
        continue

    sonuc = base64_coz(girdi)

    print("-" * 20)
    print(f"Sonuç: {sonuc}")
    print("-" * 20 + "\n")  # Her işlemden sonra alt satıra geçmesi için \n ekledim
