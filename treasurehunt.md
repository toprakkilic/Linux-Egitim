# 🌐 Terminal Treasure Hunt: "The Curl Master" (Final Sürümü)

Bu yarışmada `cd` komutu yasaktır! Her şey `curl` ve terminale gelen çıktılarla çözülecek. 

## 🚩 Başlangıç
Macerayı başlatmak için şu komutu çalıştır:
`curl http://api.col/start`

---

### 1. Görünmez Kapı (Redirects)
- **Görev**: Sunucu seni otomatik olarak bir "Hoş Geldin" sayfasına yönlendiriyor. Bu yönlendirmeyi terminalde otomatik takip et.
- **Komut**: `curl -L http://api.col/start`
- **Sonuç**: Ekranda yeni bir görev adresi belirecek: `/step/02-headers`.

### 2. Satır Aralarını Oku (Headers)
- **Görev**: Sayfa içeriği boş görünebilir. Bilgi, HTTP başlıklarının (Headers) içinde saklıdır.
- **Komut**: `curl -I http://api.col/step/02-headers`
- **İpucu**: `X-Next-Step` başlığındaki `/step/03-download` yolunu not et.

### 3. Paketi İndir (Output)
- **Görev**: Sunucudaki `secret_data.txt` dosyasını kendi bilgisayarına, belirlediğin bir isimle kaydet.
- **Komut**: `curl -o ipucu.txt http://api.col/step/03-download`

### 4. Dosyayı İncele (Cat)
- **Görev**: İndirdiğin `ipucu.txt` dosyasının içeriğini terminale bas.
- **Komut**: `cat ipucu.txt`
- **Sonuç**: İçeride bir arşiv dosya linki ve bir parola ipucu göreceksin.

### 5. Arşivi Çek (Download)
- **Görev**: Belirtilen arşivi (`mission.rar`) URL üzerindeki orijinal ismiyle indir.
- **Komut**: `curl -O http://api.col/step/05-archive/mission.rar`
- **Parola İpucu**: PDF'teki temel felsefe: "Linux'ta her şey bir dosyadır."

### 6. Kelime Avı (Grep)
- **Görev**: Arşivden çıkan devasa `list.txt` dosyası içinde "ACCESS" kelimesini ara.
- **Komut**: `grep "ACCESS" list.txt`
- **Sonuç**: `ACCESS_CODE: linux_kernel_2026`.

### 7. Güvenlik Duvarını Aş (Insecure)
- **Görev**: Sertifikası geçersiz veya hatalı (SSL hatası veren) güvenli bir URL'ye bağlan.
- **Komut**: `curl -k https://api.col/step/07-secure`
- **Mesaj**: "Bağlantı sağlandı. Final aşamasına hazırsın!"

### 8. Büyük Final: Skorbord (POST)
- **Görev**: Bulduğun kodu ve kendi ismini kullanarak sunucuya bir POST isteği (veri paketi) gönder.
- **Komut**: `curl -X POST -d "name=ADINIZ&code=linux_kernel_2026" http://api.col/finish`

---

## 🔍 Katılımcılar İçin İpucu (Hints) Dosyası

Bu rehber, takıldığın yerlerde sana yol gösterecektir:

* **Yönlendirmeler (L)**: Sayfa "taşındı" (Redirect) uyarısı veriyorsa `-L` parametresini ekle.
* **Gizli Başlıklar (I)**: Sayfa içeriği boşsa `-I` ile Header bilgilerini kontrol et.
* **Dosya İndirme (o/O)**: Dosyayı yeni bir isimle kaydetmek için `-o`, orijinal ismiyle kaydetmek için `-O` kullan.
* **Kelime Bulma (Grep)**: Devasa metinler içinde kaybolmamak için `grep` komutuyla arama yap.
* **Sertifika Hatası (k)**: HTTPS bağlantısında hata alıyorsan `-k` ile güvenli olmayan bağlantıya izin ver.
* **Sonuç Gönderme (X/d)**: İsmini listeye eklemek için `-X POST -d` yapısını kullan.
