# 🛠 Linux Treasure Hunt: Geliştirici Teknik Dökümanı

Bu döküman, "The Curl Master" eğitim oyunu için arka planda kurulması gereken API yapısını ve dosya içeriklerini tanımlar.

---

## 📂 1. Sunucu Tarafındaki Dosyalar

### A. ipucu.txt
Bu dosya sunucuda statik olarak barındırılmalıdır.
**İçerik:**
"Tebrikler! İlk engeli aştın. Bir sonraki ipucu kilitli bir arşivin içinde. Arşivi buradan indir: http://api.col/step/05-archive/mission.rar. Parola İpucu: PDF'teki temel felsefeyi hatırla (küçük harflerle, boşluk yerine alt çizgi kullanarak)."

### B. mission.rar
- **Arşiv Şifresi:** `everything_is_a_file`
- **İçerik:** İçerisinde en az 1000 satırlık rastgele metin olan bir `list.txt` dosyası olmalı.
- **Kritik Satır:** `list.txt` dosyasının rastgele bir yerine şu satırı ekle: `ACCESS_CODE: bunu ilk olusturdugumuz dosyanın adı da yapabiliriz siberayvegdgoncampus`.

---

## 🌐 2. API Endpoint Yapılandırması

### 1. GET /start
- **İşlem:** Kullanıcıyı `/step/01-welcome` adresine yönlendir (HTTP 301/302 Redirect).

### 2. GET /step/01-welcome
- **İçerik:** "Hoş geldin! Bir sonraki adım için başlıkları (headers) kontrol et."

### 3. GET /step/02-headers
- **İşlem:** HTTP Yanıt Başlığına (Response Header) şunu ekle: `X-Next-Step: /step/03-download`.
- **Gövde:** "Burada görülecek bir şey yok, sadece başlıklara bak."

### 4. GET /step/03-download
- **İşlem:** `ipucu.txt` dosyasını `Content-Disposition: attachment` ile gönder veya düz metin olarak sun.

### 5. GET /step/05-archive/mission.rar
- **İşlem:** `mission.rar` dosyasını orijinal ismiyle indirmeye zorla.

### 6. GET https://api.col/step/07-secure
- **Önemli:** Bu adres **HTTPS** olmalı ve **geçersiz/self-signed SSL sertifikası** kullanmalıdır.
- **İçerik:** "Güvenli bölgeye ulaştın. Final için verilerini /finish adresine POST et."

### 7. POST /finish
- **Beklenen Veri:** `{ "name": "Kullanıcı Adı", "code": "linux_kernel_2026" }.
- **Mantık:** Eğer kod doğruysa, gelen ismi ve tam geliş vaktini (milisaniye cinsinden) bir log dosyasına kaydet. Bu sayede ilk 3 kişiyi belirleyebiliriz.
- **Yanıt:** "Tebrikler! Kaydın başarıyla alındı."

---

## 💡 Geliştirici Notu
- **SSL Sertifikası:** 7. adımdaki `-k` parametresinin test edilmesi için sertifika hatası verilmesi kritiktir.
- **Sıralama:** `/finish` endpoint'ine gelen istekleri kronolojik sıraya göre dizerek kazananları belirleyeceğiz.
