# 🐧 Linux Temelleri ve Komut Satırı Eğitimi

## 1. Temel Navigasyon (Sistemde İlk Adımlar)
* `pwd`: Şu an hangi dizindeyim? (*Print Working Directory*)
* `cd /`: En kök dizine git.
* `cd ..`: Bir üst dizine çık.
* `cd ~`: Kullanıcı ana dizinine git.
* `cd -`: Bir önceki bulunduğun dizine dön.
* `ls`: Dosyaları listele.

---

## 2. Temel Dosya ve Dizin İşlemleri (Yaratım ve İnceleme)
* `mkdir`: Yeni dizin oluşturur.
* `touch`: Boş dosya oluşturur.
* `cat`: Dosya içeriğini ekrana yazdırır.
* `less`: Büyük dosyaları sayfa sayfa okumanızı sağlar.
* `head` / `tail`: Dosyanın ilk veya son 10 satırını gösterir. (-20 eklenirse ilk/son 20 satir)

---

## 3 Gelişmiş Navigasyon ve Temel Yardımcılar
* `ls -lah`: Detaylı listeleme.
    * `-l`: Detaylı liste.
    * `-a`: Gizli dosyaları göster (Nokta ile başlayanlar).
    * `-h`: Dosya boyutlarını okunabilir yap (KB, MB).
* `man <komut>`: Komutun kullanım kılavuzunu açar.
* `history`: Komut geçmişini listeler.
* `!!`: Bir önceki komutu tekrar çalıştırır.

---

## 4. Dosya Yönetimi (Taşıma ve Silme)
* `cp`: Dosya veya dizin kopyalar.
* `mv`: Dosya taşır veya adını değiştirir.
* `rmdir`: Dizinleri boş ise siler.
* `rm`: Dosya siler. (`rm -rf` dizinleri ve içeriğini zorla siler).

---

## 5. Girdi/Çıktı Yönetimi ve Yönlendirmeler
* `echo`: Ekrana metin yazar.
* `echo > dosya.txt`: Dosyanın içeriğini silip üzerine yazar.
* `echo >> dosya.txt`: Mevcut içeriğin sonuna ekleme yapar.

---

## 6. Arama, Filtreleme ve Borulama (Pipe)
* `grep`: Metin içinde arama yapar.
## 7. Arama, Filtreleme ve Borulama (Pipe)
* `grep`: Metin içinde arama yapar.
* `find`: Dosya sisteminde dosya veya dizin arar.
    * *Kalıp:* `find <nerede_aranacak> -name "aranan_isim"`
    * *Örnek 1:* `find . -name "roman.txt"` (Şu anki dizinde ismi tam olarak 'roman.txt' olanı bulur).
    * *Örnek 2:* `find . -iname "roman.txt"` (Büyük-küçük harf fark etmeksizin arar; 'Roman.txt' veya 'ROMAN.txt' olsa da bulur).
    * *Örnek 3:* `find / -type d -name "bin"` (Tüm sistemde kök dizinden başlayarak ismi 'bin' olan KLASÖRLERİ arar).
* `|` (Pipe): Bir komutun çıktısını diğerine "borulayıp" gönderir.
    * *Örnek:* `history | grep "curl"`
* `alias`: Uzun komutlara kısayol atar (Örn: `alias hersey='ls -lah'`).

* `|` (Pipe): Bir komutun çıktısını diğerine "borulayıp" gönderir.
    * *Örnek:* `history | grep "curl"`
    * *Örnek:* `echo "Linux dunyasina hos geldiniz, bugun gunlerden Cuma." | grep "Cuma"`
* `alias`: Uzun komutlara kısayol atar (Örn: `alias hersey='ls -lah'`).

---

## 7. Web Dünyasına Giriş: HTTP ve Header Mantığı
İnternetteki her web sitesi veya API, tarayıcınız ya da terminaliniz ile **HTTP** protokolü üzerinden haberleşir. Bu iletişim iki ana parçadan oluşur: **İstek (Request)** ve **Yanıt (Response)**.

* **HTTP İsteği:** Bilgisayarınızın sunucuya attığı "Bana şu sayfayı ver" (`GET`) veya "Al bu veriyi kaydet" (`POST`) mesajıdır.
* **HTTP Yanıtı:** Sunucunun size döndüğü cevaptır. Bu cevap kendi içinde ikiye ayrılır:
    1. **Header (Başlık Bilgisi):** Perde arkasındaki teknik detaylardır. İçerik tipi, sunucu bilgisi, sitenin durum kodu (Örn: `200 OK` veya `404 Not Found`) ve gizli yönlendirmeler burada saklanır.
    2. **Body (Gövde / İçerik):** Ekranda gördüğümüz asıl veridir (HTML kodları, yazılar veya indirmek istediğimiz ham dosyalar).

---

## 8. CURL ile Ağ İşlemleri & Dummy API Pratikleri
`curl`, terminal üzerinden dış dünyadaki sunucularla veri transferi yapmanızı sağlar.

### 🛠 Temel Komutlar ve Canlı Örnekler

* **`curl <url>`**: Site içeriğini ekrana basar.
    * *Canlı Pratik:* `curl https://jsonplaceholder.typicode.com/users/1` (Sahte bir kullanıcı verisi çeker).
* **`curl -I`**: Sadece Header (başlık) bilgisini alır.
    * *Canlı Pratik:* `curl -I https://httpbin.org/headers` (Sunucunun teknik etiketini okur).
* **`curl -i`**: Hem Header hem içerik bilgisini aynı anda gösterir.
    * *Canlı Pratik:* `curl -i https://jsonplaceholder.typicode.com/posts/1`
* **`curl -o dosya.html`**: İçeriği bilgisayarınıza belirttiğiniz isimle kaydeder.
    * *Canlı Pratik:* `curl -o test.json https://jsonplaceholder.typicode.com/todos/1`
* **`curl -O`**: Dosyayı URL üzerindeki orijinal ismiyle indirir.
    * *Canlı Pratik:* `curl -O https://www.gutenberg.org/cache/epub/84/pg84.txt` (Frankenstein romanını indirir, `head`/`tail` için harika bir büyük dosyadır).
* **`curl -X POST -d "data"`**: POST isteği gönderir (Sunucuya veri yazar).
    * *Canlı Pratik:* `curl -X POST -d "title=Egitim&body=Linux" https://jsonplaceholder.typicode.com/posts`
* **`curl [1-5].site.com`**: Belirli bir aralıktaki URL'leri tek seferde çeker.
