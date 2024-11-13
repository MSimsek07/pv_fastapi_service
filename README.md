## Fotovoltaik Panel Anomali Tespiti için FastAPI Uygulaması

Bu doküman, fotovoltaik (PV) panel görüntüsündeki anomalileri tespit etmek için geliştirilmiş bir makine öğrenimi modelini dağıtan bir FastAPI uygulamasının kaynak kodunu analiz etmektedir. Uygulama, kullanıcıların bir PV panel görüntüsünü yüklemelerini ve modelin tahmin ettiği anomali türlerinin yüzdesini içeren bir yanıt almalarını sağlar.

### Programlama Dili

Uygulama, web API'leri oluşturmak için modern ve hızlı bir Python web çatısı olan **FastAPI** kullanılarak geliştirilmiştir. Ayrıca, makine öğrenimi modeli eğitimi ve tahmini için **TensorFlow** ve **Keras** kullanır.

### Genel Bakış

Uygulama, yüklenen bir görüntüyü işleyen, önceden eğitilmiş bir TensorFlow modelini kullanarak tahminlerde bulunan ve sonuçları kullanıcı dostu bir JSON formatında döndüren tek bir API uç noktasından oluşur.

### Ana Bileşenler

Uygulama aşağıdaki temel bileşenlerden oluşmaktadır:

1. **`load_model()` Fonksiyonu:** Bu fonksiyon, önceden eğitilmiş makine öğrenimi modelini belirtilen bir yoldan yükler. Model yolu, varsayılan olarak "model_efficientnet.h5" olarak ayarlanmış bir ortam değişkeni (`MODEL_PATH`) kullanılarak yapılandırılabilir.

2. **`process_image()` Fonksiyonu:** Bu fonksiyon, yüklenen görüntüyü alır, bayt dizisinden yükler, modeli tarafından beklenen boyuta (224x224) yeniden boyutlandırır, bir NumPy dizisine dönüştürür ve modelin giriş gereksinimleriyle eşleşmesi için ön işler.

3. **`predict_image()` Fonksiyonu:** Bu fonksiyon, işlenmiş görüntüyü girdi olarak alır ve önceden yüklenmiş modeli kullanarak bir tahmin gerçekleştirir. Tahmin, her bir anomali sınıfı için olasılıkları içeren bir dizi olarak döndürülür.

4. **`get_prediction_percentages()` Fonksiyonu:** Bu fonksiyon, modelin tahminlerini alır ve bunları her bir anomali sınıfı için yüzde olasılıklarına dönüştürür. Daha sonra, sonuçları kullanıcı dostu etiketlerle birlikte bir sözlükte döndürür.

5. **`/predict/` Uç Noktası:** Bu, uygulamanın bir POST isteği kabul ettiği ana API uç noktasıdır. Uç nokta, yüklenen bir görüntü dosyası ("dosya" olarak adlandırılır) bekler. İstek alındığında, görüntü `process_image()` fonksiyonu kullanılarak işlenir, `predict_image()` fonksiyonu kullanılarak tahmin yapılır ve sonuçlar `get_prediction_percentages()` fonksiyonu kullanılarak yüzdelere dönüştürülür. Son olarak, tahmin yüzdelerini içeren bir JSON yanıtı istemciye döndürülür.

### API Uç Noktaları

Uygulama, aşağıda açıklanan tek bir API uç noktası sunar:

**POST /predict/**

* **Amaç:** Yüklenen bir PV panel görüntüsündeki anomalileri tahmin etmek için kullanılır.
* **İstek Gövdesi:** "dosya" adında, yüklenen görüntü dosyasını içeren çok parçalı/form verisi.
* **Yanıt:** Tahmin edilen anomali türleri ve bunlara karşılık gelen yüzde olasılıklarını içeren bir JSON nesnesi.
     ```json
     {
         "percentages": {
             "Cell": 10.5,
             "Cell-Multi": 2.3,
             "Cracking": 0.1,
             "Diode": 5.7,
             "Diode-Multi": 0.8,
             "No-Anomaly": 75.2,
             "Offline-Module": 1.9,
             "Shadowing": 0.5,
             "Soiling": 2.8,
             "Vegetation": 0.2
         }
     }
     ```

### Hata İşleme

Uygulama, temel hata işleme için Python'un `logging` modülünü kullanır. Herhangi bir hata veya istisna durumunda, ayrıntılı hata ayıklama için konsola ve günlük dosyalarına günlük mesajları yazdırılır. 

### Tasarım Desenleri ve İlkeleri

Uygulama, aşağıdaki tasarım desenlerini ve ilkelerini takip eder:

* **Model-View-Controller (MVC):** Uygulama, API uç noktalarını (Controller), iş mantığını (Model) ve kullanıcı arayüzünü (View) açıkça ayırmasa da, kodun organizasyonu MVC deseninden esinlenmiştir.
* **Tekil Sorumluluk İlkesi:** Her fonksiyonun belirli ve tek bir amacı vardır, bu da kodun okunabilirliğini ve bakımını kolaylaştırır.

### Sonuç

Bu FastAPI uygulaması, PV panel anomali tespiti için makine öğrenimi modellerini dağıtmak için basit ve etkili bir yol sunar. Kullanıcı dostu API uç noktası, geliştiricilerin bunu daha büyük sistemlere veya uygulamalara kolayca entegre etmelerini sağlar.
