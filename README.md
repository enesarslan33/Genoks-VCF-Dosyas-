# Genoks-VCF-Dosyas-
VCF dosyasını jsona dönüştürme

vcf ve json kütüphanelerini ekledim.
İlk satırda, 'ornek.vcf' dosyası 'r' (read) modunda açtım ve vcf.Reader() metodu kullanılarak bir vcf_reader nesnesine attım.
Sonrasında, boş bir vcf_data listesi oluşturdum.
Daha sonra, her bir VCF kaydı (record) vcf_reader nesnesinden okunur ve alt_strs değişkeninde alternatif aleller (ALT) bir listeye dönüştürülür.
Her bir VCF kaydının bazı özellikleri, örneğin kromozom (chromosome), pozisyon (position), ID (id), referans (reference) ve alternatif (alternate) alelleri,
kalite (quality), filtre (filter), bilgi (info) ve format (format) özellikleri, ve ayrıca 'NA00001', 'NA00002' ve 'NA00003' adında örnek adlarına sahip örnek verileri,
sözlük (dictionary) biçiminde vcf_data listesine ekledim.
Son olarak, json.dumps() metodu kullanılarak vcf_data listesi bir JSON formatına dönüştürüp ve ekrana yazdırdım.
vcf_data adlı bir sözlük objesinin içeriği json.dump() fonksiyonu kullanılarak example.json adlı bir dosyaya yazılıyor.
with ifadesi, dosyayı açmak ve işlem bittikten sonra otomatik olarak kapatmak için kullanılır.
'example.json' dosyası açılır ve 'w' (yazma) modunda açılır. Bu, dosyanın yazma işlemi için açıldığı anlamına gelir.
json.dump() fonksiyonu, sözlük objesinin içeriğini f adlı dosyaya JSON formatında yazar. indent parametresi,
yazılan JSON verilerinin okunabilirliğini artırmak için kullanılır ve dosyanın içeriğinin girintili bir şekilde yazılmasını sağlar.
Bu sayede, JSON verilerini daha kolay okunabilir hale getirmiş oldum.
with bloğu, dosyanın işlemi tamamlandığında dosyayı otomatik olarak kapatır ve bellek sızıntılarını önler.


![2023-02-27_10-19-46](https://user-images.githubusercontent.com/113882167/221504805-b1f1d82c-53c0-458b-8809-140a8d61166e.png)
