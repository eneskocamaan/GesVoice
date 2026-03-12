# GesVoice

**GesVoice**, el hareketleriyle bilgisayarınızı kontrol etmenizi sağlayan bir "Sanal Fare" ve OpenAI (ChatGPT & DALL-E) entegrasyonlu gelişmiş bir "Sesli Asistan" projesidir. Python ve CustomTkinter kullanılarak geliştirilmiş modern bir arayüze sahiptir.

Bu proje, fiziksel bir fareye ihtiyaç duymadan bilgisayar kullanımını mümkün kılarken, sesli komutlarla günlük işlerinizi hızlandırmayı ve yapay zeka araçlarına tek bir noktadan erişmeyi hedefler.

## 🌟 Özellikler

### 1. 🖱️ Sanal Fare (Virtual Mouse)
Bilgisayar kameranızı kullanarak el hareketlerinizi algılar ve fare imlecini yönetir.
*   **İmleç Hareketi:** Sağ el işaret parmağınızla imleci hareket ettirin.
*   **Sol Tık:** Sağ el işaret parmağı ve baş parmağınızı birleştirin.
*   **Sağ Tık:** Sağ el orta parmak, işaret parmağı ve baş parmağınızı birleştirin.
*   **Kaydırma (Scroll):** Sol elinizi yukarı/aşağı hareket ettirerek sayfalarda gezinin.
*   **Otomatik Klavye:** Sanal fare başlatıldığında Windows Ekran Klavyesi otomatik açılır.

### 2. 🎙️ Sesli Asistan
Türkçe sesli komutlarla bilgisayarınızı ve interneti yönetin.
*   **Sistem Kontrolü:** Ses açma/kapatma, masaüstüne dönme, pencere kapatma (Alt+F4), sekmeler arası geçiş (Alt+Tab), bilgisayarı kapatma/yeniden başlatma.
*   **Uygulama Yönetimi:** İstediğiniz uygulamayı sesle açın (Örn: "Spotify aç").
*   **Web İşlemleri:** Google araması yapma, Wikipedia'da konu araştırma, YouTube'da video/müzik açma.
*   **Kişisel Asistan:** Tarih/Saat öğrenme, Not alma/okuma, Hatırlatıcı kurma.
*   **Telefon Entegrasyonu:** Windows "Telefon Bağlantısı" uygulaması üzerinden numara arama ve mesaj gönderme (WhatsApp Web/Desktop üzerinden).
*   **Hava Durumu:** Konumunuza göre anlık hava durumu bilgisi.

### 3. 🤖 Yapay Zeka Entegrasyonu
*   **ChatGPT Modu:** OpenAI GPT-3.5 modeli ile sesli veya yazılı sohbet edin.
*   **DALL-E Modu:** Metin girerek yapay zeka ile resim oluşturun ve indirin (Türkçe yazdığınız promptlar otomatik İngilizceye çevrilir).
*   **Diğer Araçlar:** Blackbox, Copilot, DeepL, LogoAI gibi popüler yapay zeka araçlarına uygulama içi tarayıcıdan hızlı erişim.

---

## 📋 Gereksinimler

Projenin çalışması için aşağıdaki donanım ve yazılımlara ihtiyacınız vardır:

*   **İşletim Sistemi:** Windows 10 veya 11 (Bazı otomasyon özellikleri Windows'a özeldir).
*   **Python:** Sürüm 3.8 veya üzeri.
*   **Kamera:** Sanal fare özelliği için webcam.
*   **Mikrofon:** Sesli asistan için.
*   **OpenAI API Anahtarı:** ChatGPT ve DALL-E özelliklerini kullanmak için.

---

## 🚀 Kurulum

1.  **Projeyi İndirin:**
    Bu projeyi bilgisayarınıza klonlayın veya zip olarak indirip çıkarın.

2.  **Sanal Ortam (Venv) Kurulumu (Önerilen):**
    Python kütüphanelerinin sisteminizdeki diğer projelerle çakışmaması için sanal ortam kullanmanız önerilir.

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    Proje dizininde bir terminal açın ve aşağıdaki komutu çalıştırın:

    ```bash
    pip install -r requirements.txt
    ```

    *Not: `mediapipe` kütüphanesinin sürümü `requirements.txt` dosyasında belirtildiği gibi 0.10.30'dan düşük olmalıdır.*

4.  **Çevre Değişkenlerini Ayarlayın:**
    Proje ana dizininde `.env` adında bir dosya oluşturun ve içine OpenAI API anahtarınızı yapıştırın:

    ```env
    OPENAI_API_KEY=sk-sizin-api-anahtariniz-buraya
    ```

---

## 🎮 Kullanım

### Başlatma
Uygulamayı başlatmak için terminalde şu komutu çalıştırın:

```bash
python GesVoice.py
```

### İlk Kurulum Ekranı
Uygulamayı ilk kez açtığınızda bir kayıt ekranı sizi karşılayacaktır.
*   İsim, Soyisim ve Asistanınıza vermek istediğiniz ismi girin.
*   Bu bilgiler `config.txt` dosyasına kaydedilir ve sonraki açılışlarda sizi otomatik tanır.

### Ana Menü

*   **Sanal Fare'yi Başlat:** Kamerayı açar ve el hareketlerini izlemeye başlar. Çıkmak için sanal fare penceresindeyken `ESC` tuşuna basın.
*   **Asistan Modları (Sağ Panel):**
    *   **Sesli Asistan:** Yerel komutları dinler (Örn: "Asistan ismi + Saat kaç").
    *   **ChatGPT:** Sohbet botu arayüzünü açar.
    *   **Dall-E:** Resim oluşturma arayüzünü açar.
    *   **Diğer:** Yardımcı web araçlarını listeler.

---

## 🗣️ Örnek Sesli Komutlar

Sesli asistanı başlattıktan sonra, belirlediğiniz **Asistan İsmi** ile cümleye başlayarak (veya sadece komutu söyleyerek - *kod akışına göre*) aşağıdaki komutları verebilirsiniz:

| Komut | Açıklama |
| :--- | :--- |
| **"Saat kaç"** | Güncel saati söyler. |
| **"Google'da ara"** | Ardından aramak istediğiniz şeyi söyleyin. |
| **"Uygulama aç"** | Ardından uygulama adını söyleyin (Örn: "Hesap Makinesi"). |
| **"Not et" / "Not al"** | Söylediklerinizi masaüstüne `.txt` olarak kaydeder. |
| **"Not oku"** | Masaüstündeki bir notu sesli okur. |
| **"Müzik aç"** | YouTube üzerinden istenilen şarkıyı açar. |
| **"Hava durumu"** | Bulunduğunuz şehrin hava durumunu söyler. |
| **"Bilgisayarı kapat"** | Süre sorar ve bilgisayarı kapatmaya programlar. |
| **"Ekran görüntüsü al"** | (Eğer kodda tanımlıysa) Ekran görüntüsü alır. |
| **"Numara ara"** | Windows Telefon Bağlantısı ile arama yapar. |
| **"Mesaj at"** | Kayıtlı numaralara WhatsApp mesajı gönderir. |

---

## 🛠️ Sorun Giderme

*   **Kamera Açılmıyor:** Başka bir uygulamanın kamerayı kullanmadığından emin olun.
*   **Ses Algılanmıyor:** Mikrofon ayarlarınızı kontrol edin ve sessiz bir ortamda deneyin.
*   **OpenAI Hataları:** `.env` dosyasındaki API anahtarınızın doğru olduğundan ve krediniz olduğundan emin olun.
*   **Kütüphane Hataları:** `pip install -r requirements.txt` komutunun hatasız tamamlandığından emin olun.

---

## 📂 Proje Yapısı

```
GesVoice/
├── GesVoice.py       # Ana uygulama ve arayüz (GUI) kodu
├── sanalfare.py      # Görüntü işleme ve fare kontrol kodu
├── requirements.txt  # Gerekli kütüphaneler
├── .env              # API anahtarları (Siz oluşturmalısınız)
├── config.txt        # Kullanıcı ayarları (Otomatik oluşturulur)
├── numbers.txt       # Kayıtlı telefon numaraları (Otomatik oluşturulur)
├── background.png    # Arayüz arka plan görseli
├── logo.png          # Uygulama logosu
└── icons/            # Arayüz ikonları (mic.png, info.png vb.)
```

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.

Bu, projeyi özgürce kullanabileceğiniz, değiştirebileceğiniz ve dağıtabileceğiniz anlamına gelir. Detaylar için proje klasöründeki [LICENSE](LICENSE) dosyasına bakabilirsiniz.