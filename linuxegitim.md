# Linux Temelleri ve Komut Satırı Eğitimi

## 1. Giriş: Linux Nedir?
Linux bir çekirdektir (kernel). Günlük hayatta kullandıklarımız ise bu çekirdek üzerine inşa edilmiş **Dağıtımlardır** (Ubuntu, Debian, Pop!_OS vb.).

* **Felsefe:** "Linux'ta her şey bir dosyadır." (Donanımlar, süreçler, dizinler...)
* **Ne Değildir?** Sadece bir terminal ekranı değildir, bir Windows alternatifi olmaktan öte bir özgürlük felsefesidir.

## 2. Navigasyon (Dizinlerde Gezinti)
* `pwd`: Şu an hangi dizindeyim? (*Print Working Directory*)
* `cd /`: En kök dizine git.
* `cd ..`: Bir üst dizine çık.
* `cd ~`: Kullanıcı ana dizinine git
* `cd -`: Bir önceki bulunduğun dizine dön.
* `ls -lah`: Dosyaları listele.
    * `-l`: Detaylı liste.
    * `-a`: Gizli dosyaları göster.
    * `-h`: Dosya boyutlarını okunabilir yap (KB, MB).

## 3. Dosya ve Dizin İşlemleri
* `man <komut>`: Komutun kullanım kılavuzunu açar.
* `mkdir`: Yeni dizin oluşturur.
* `touch`: Boş dosya oluşturur.
* `cat`: Dosya içeriğini ekrana yazdırır.
* `less`: Büyük dosyaları sayfa sayfa okumanızı sağlar.
* `head` / `tail`: Dosyanın ilk veya son 10 satırını gösterir.
* `rm`: Dosya siler. (`rm -rf` dizinleri ve içeriğini zorla siler).
* `rmdir`: Dizinleri boş ise siler.
* `cp`: Dosya veya dizin kopyalar.
* `mv`: Dosya taşır veya adını değiştirir.

## 4. Girdi/Çıktı Yönetimi ve Borulama
* `echo`: Ekrana metin yazar.
* `echo > dosya.txt`: Dosyanın içeriğini silip üzerine yazar.
* `echo >> dosya.txt`: Mevcut içeriğin sonuna ekleme yapar.
* `|` (Pipe): Bir komutun çıktısını diğerine "borulayıp" gönderir.
    * Örn: `history | grep "curl"`

## 5. Arama ve Filtreleme
* `grep`: Metin içinde arama yapar.
* `find`: Dosya sisteminde dosya arar.
* `alias`: Uzun komutlara kısayol atar (Örn: `alias gs='git status'`).
* `history`: Komut geçmişini listeler.
* `!!`: Bir önceki komutu tekrar çalıştırır (Örn: `sudo !!`).

## 6. Dosya İzinleri (chmod)
Linux'ta izinler üç grupta incelenir: **Okuma (4), Yazma (2), Çalıştırma (1)**.

* **777 Ne Demek?**
    * İlk 7: Dosya Sahibi (4+2+1) -> Tam yetki.
    * İkinci 7: Grup (4+2+1) -> Tam yetki.
    * Üçüncü 7: Diğerleri (4+2+1) -> Tam yetki.
* `chmod 755`: Sahibi her şeyi yapar, diğerleri sadece okur ve çalıştırır.

## 7. CURL ile Ağ İşlemleri
`curl`, terminal üzerinden veri transferi yapmanızı sağlar.

* `curl <url>`: Site içeriğini (HTML vb.) ekrana basar.
* `curl -I`: Sadece Header (başlık) bilgisini alır.
* `curl -i`: Hem Header hem içerik bilgisini aynı anda gösterir.
* `curl -o dosya.html`: İçeriği bilgisayarınıza belirttiğiniz isimle kaydeder.
* `curl -O`: Dosyayı URL üzerindeki orijinal ismiyle indirir.
* `curl -L`: HTTPS yönlendirmesi (Redirect) varsa otomatik takip eder.
* `curl -v`: Verbose modu. Tüm süreci (TLS handshake, bağlantı adımları) detaylıca gösterir.
* `curl -k`: SSL sertifikası geçersiz olsa bile bağlantıya izin verir (Güvensiz mod).
* `curl -d "data" -X POST`: POST isteği gönderir (Varsayılan olarak form verisi alır).
* `curl [1-5].site.com`: Belirli bir aralıktaki URL'leri tek seferde çeker.
