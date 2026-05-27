import base64

def base64_coz(veri):
    try:
        # Veriyi byte tipine çevirip decode ediyoruz
        cozulmus_byte = base64.b64decode(veri)
        # Metni utf-8 formatında stringe dönüştürüyoruz
        return cozulmus_byte.decode('utf-8')
    except Exception as e:
        return f"Hata: Geçersiz Base64 formatı! ({e})"

# Base64
girdi = input("Çözmek istediğin Base64 metnini yapıştır: ")
sonuc = base64_coz(girdi)

print("-" * 20)
print(f"Sonuç: {sonuc}")