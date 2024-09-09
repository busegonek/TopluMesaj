# WhatsApp Mesaj Gönderici

Bu proje, kullanıcıların WhatsApp üzerinden toplu mesajlar göndermesine olanak tanıyan bir masaüstü uygulamasıdır. Kullanıcılar, bir mesaj dosyası ve telefon numaraları dosyası yükleyerek, belirledikleri mesajı birden fazla telefon numarasına gönderebilirler.

## Teknolojiler

- **Python**: Uygulamanın ana programlama dili.
- **Tkinter**: Python ile GUI (grafiksel kullanıcı arayüzü) oluşturmak için kullanılan kütüphane.
- **Pillow (PIL)**: Python Imaging Library, resim işleme ve görüntüleme işlemleri için kullanılır.
- **Selenium**: Web otomasyon ve test işlemleri için kullanılan kütüphane. WhatsApp Web üzerinden mesaj gönderme işlemleri bu kütüphane ile gerçekleştirilir.
- **WebDriver Manager**: Selenium WebDriver'ların otomatik olarak indirilmesini ve yönetilmesini sağlar.

## Kurulum ve Kullanım

1. **Gereksinimler**:
   - Python 3.x
   - Pip (Python paket yöneticisi)

2. **Kütüphaneleri Yükleyin**:
   Bu projede kullanılan gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install -r requirements.txt
### Dosyaların Seçilmesi

- "Mesaj Dosyası Seç" butonuna tıklayarak mesajınızı içeren `.txt` dosyasını seçin.
- "Telefon Numaraları Dosyası Seç" butonuna tıklayarak telefon numaralarınızı içeren `.txt` dosyasını seçin.

### Mesaj Gönderme

- Dosyaları seçtikten sonra "Mesaj Gönder" butonuna tıklayarak mesajları belirlediğiniz telefon numaralarına gönderebilirsiniz.
- Uygulama, WhatsApp Web üzerinden mesajları gönderecek ve işlem tamamlandığında bir başarı mesajı gösterecektir.
