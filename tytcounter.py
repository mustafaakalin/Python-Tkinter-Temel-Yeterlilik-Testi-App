import tkinter as tk
from datetime import datetime, timedelta
import subprocess

# linux autostart
# touch ~/.config/autostart/tytcounter-autostart.desktop
# echo "[Desktop Entry] "\n"Type=Application"\n"Name=tytcounter-autostart"\n"Exec=python /home/$USER/tytcounter.py" > ~/.config/autostart/tytcounter-autostart.desktop

# Sınav Tarihi ve Saati
sinav_tarihi = datetime(2024, 6, 18, 9, 0)

# Güncel Zaman
simdiki_zaman = datetime.now()

# Kalan Süreyi Hesaplama
kalan_sure = sinav_tarihi - simdiki_zaman

# Pencere Oluşturma
pencere = tk.Tk()
pencere.geometry("800x480")
pencere.title("Temel Yeterlilik Testi")

# Arka Plan Rengi
pencere.configure(bg="white")

# Yazı Tipi
yazi_tipi = ("Arial", 36, "bold")

# Kırmızı Renk
kirmizi = "#FF0000"

# Kalan Süre Göstergesi
kalan_sure_str = f"{kalan_sure.days} gün {kalan_sure.seconds//3600} saat {kalan_sure.seconds//60 % 60} dakika KALDI."
kalan_sure_label = tk.Label(text=kalan_sure_str, font=yazi_tipi, fg=kirmizi, bg="white")
kalan_sure_label.pack(padx=20, pady=20)

# # Sistem Başlatıldığında Otomatik Çalıştırma  for windows
# def otomatik_calistirma():
#     subprocess.call(["python", "Temel_Yeterlilik_Testi.py"])

# # Otomatik Çalıştırma Fonksiyonu Çağrısı
# otomatik_calistirma()

# Pencereyi Gösterme
pencere.mainloop()
