Temel Yeterlilik Testi graphical user interface app with tkinter, autostart with
system, font size: 36 , font color red, TYT Sınavına, ... gün ... saat ...
dakika KALDI., # ... gün ... saat ... dakika KALDI. yazısının rengi kırmızı,
arkaplan rengi beyaz olacak şekilde gösterilmelidir. # Bu uygulamayı sistem
başlatıldığında otomatik olarak çalıştırın. # Bu uygulamayı kullanıcıya
gösterin.

# dosyayı kullanıcı dizine çek. /home/kullanıcı/.

# installing

```bash
git clone https://github.com/mustafaakalin/Python-Tkinter-Temel-Yeterlilik-Testi-App.git -b master
```

# linux autostart

```bash
touch ~/.config/autostart/tytcounter-autostart.desktop
echo "[Desktop Entry] "\n"Type=Application"\n"Name=tytcounter-autostart"\n"Exec=python /home/$USER/tytcounter.py" > ~/.config/autostart/tytcounter-autostart.desktop
```
