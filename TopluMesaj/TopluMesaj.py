import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
import urllib.parse
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class WhatsAppApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Mesaj Gönderici")
        self.root.geometry("500x450")
        self.root.config(bg="#ffffff")

        # Logo
        logo_path = "TopluMesaj/Logo/logo.png"  # Logo dosyasının yolu
        if os.path.isfile(logo_path):
            try:
                # Pencere simgesini ayarla
                image = Image.open(logo_path)
                self.logo_image = ImageTk.PhotoImage(image)
                self.root.iconphoto(False, self.logo_image)
            except Exception as e:
                print(f"Logo yüklenirken bir hata oluştu: {e}")
        else:
            print(f"Logo dosyası bulunamadı: {logo_path}")

        # Başlık etiketi
        self.baslik = tk.Label(root, text="WhatsApp Mesaj Gönderici", font=("Helvetica", 18, "bold"), bg="#4CAF50",
                               fg="#ffffff")
        self.baslik.pack(pady=10, fill=tk.X)

        # Mesaj dosyası seçici
        self.mesaj_dosyasi_etiket = tk.Label(root, text="Mesaj Dosyasının Yolu:", bg="#ffffff", font=("Arial", 12))
        self.mesaj_dosyasi_etiket.pack(pady=(10, 0), anchor="w", padx=20)
        self.mesaj_dosyasi_yolu = tk.Entry(root, width=60, bd=2, relief="solid", font=("Arial", 12))
        self.mesaj_dosyasi_yolu.pack(pady=5, padx=20)
        self.mesaj_dosyasi_buton = tk.Button(root, text="Dosya Seç", command=self.seç_mesaj_dosyası, bg="#4CAF50",
                                             fg="white", relief="flat", font=("Arial", 12))
        self.mesaj_dosyasi_buton.pack(pady=5, padx=20)

        # Telefon numaraları dosyası seçici
        self.telefon_dosyasi_etiket = tk.Label(root, text="Telefon Numara Dosyasının Yolu:", bg="#ffffff",
                                               font=("Arial", 12))
        self.telefon_dosyasi_etiket.pack(pady=(10, 0), anchor="w", padx=20)
        self.telefon_dosyasi_yolu = tk.Entry(root, width=60, bd=2, relief="solid", font=("Arial", 12))
        self.telefon_dosyasi_yolu.pack(pady=5, padx=20)
        self.telefon_dosyasi_buton = tk.Button(root, text="Dosya Seç", command=self.seç_telefon_dosyası, bg="#4CAF50",
                                               fg="white", relief="flat", font=("Arial", 12))
        self.telefon_dosyasi_buton.pack(pady=5, padx=20)

        # Gönder butonu
        self.gonder_buton = tk.Button(root, text="Mesaj Gönder", command=self.gonder, bg="#2196F3", fg="white",
                                      relief="flat", font=("Arial", 14, "bold"))
        self.gonder_buton.pack(pady=20)

    def seç_mesaj_dosyası(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.mesaj_dosyasi_yolu.delete(0, tk.END)
        self.mesaj_dosyasi_yolu.insert(0, dosya_yolu)

    def seç_telefon_dosyası(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.telefon_dosyasi_yolu.delete(0, tk.END)
        self.telefon_dosyasi_yolu.insert(0, dosya_yolu)

    def gonder(self):
        mesaj_dosyasi_yolu = self.mesaj_dosyasi_yolu.get()
        telefon_numaralari_dosyasi_yolu = self.telefon_dosyasi_yolu.get()

        try:
            with open(mesaj_dosyasi_yolu, 'r', encoding='utf-8') as mesaj_dosyasi:
                mesaj = mesaj_dosyasi.read()
            with open(telefon_numaralari_dosyasi_yolu, 'r') as telefon_dosyasi:
                telefon_numaralari = telefon_dosyasi.readlines()

            # WebDriver ayarları
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            service = Service(ChromeDriverManager().install())

            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get("https://web.whatsapp.com/")
            time.sleep(20)  # QR kodunu taramak için bekleyin

            for telefon in telefon_numaralari:
                telefon = telefon.strip()
                if telefon:
                    # Mesajı URL uyumlu hale getir
                    mesaj_url_encoded = urllib.parse.quote(mesaj)
                    url = f"https://web.whatsapp.com/send?phone={telefon}&text={mesaj_url_encoded}"
                    driver.get(url)
                    time.sleep(10)  # Sayfanın yüklenmesini bekleyin

                    try:
                        # Gönder butonuna tıklama
                        send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
                        send_button.click()
                        time.sleep(5)  # Mesajın gönderilmesini bekleyin
                    except Exception as e:
                        self.alert("Hata", f"Mesaj gönderilemedi: {e}")
                        continue

            driver.quit()
            self.alert("Başarı", "Tüm mesajlar gönderildi.")
        except FileNotFoundError:
            self.alert("Dosya Hatası", "Dosya bulunamadı.")
        except Exception as e:
            self.alert("Hata", f"Bir hata oluştu: {e}")

    def alert(self, title, message):
        alert_window = tk.Toplevel(self.root)
        alert_window.title(title)
        alert_window.geometry("300x150")
        alert_window.config(bg="#ffffff")

        label = tk.Label(alert_window, text=message, bg="#ffffff", font=("Arial", 12))
        label.pack(pady=20)

        ok_button = tk.Button(alert_window, text="Tamam", command=alert_window.destroy, bg="#4CAF50", fg="white",
                              font=("Arial", 12))
        ok_button.pack(pady=10)

        alert_window.grab_set()  # Alert penceresinin üstte olmasını sağlar
        alert_window.wait_window()  # Bu, kullanıcı "Tamam" butonuna tıklayana kadar pencereyi engeller

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppApp(root)
    root.mainloop()
