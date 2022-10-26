Ödev, PyCharm Pro Edition'da hazırlanmıştır (db bağlantıları da aynı programda yapılmıştır). İlgili çıktılar jpg olarak, kaynak kod dosyaları da ilgili uzantılarda (.py vb.)yüklenmiştir.

	Kullanılan dosyalar :
		modified_or_back.py
		email.py
		analytics.py
		transactions_backend.py
 
 Yeni veri tabanı Db.io yerine PyCharm üzerinden psycopg2 ile oluşturulmuş, Sql'e yüklenmiş ve diagram olarak çıktı alınmıştır. (DB.io sitesini kullanmadım)
 	Fresh DB.py ---  Database dosyası
	New DB Diagram --- Fresh Db.py Diagram



Ödev için belirtilen yönergeler aşağıdaki şekilde listelenmiştir :

	1) adet ürün tablosu oluşturunuz.
	Oluşturuduğunuz tablodan rastgee bir ürün seçimi yapınız. Veri üretme kısmı için

	2)Faker ile kullanıcılar oluşturunuz. Bu kullanıcıları kullanıcı tablosuna ekleyiniz. 

	3) Order tablosu oluşturunuz.

	4)order backendde ürettiğiniz verileri order tablosuna yazınız.

	5)Transaction backend kısmı için customer emailleri customer id üzerinden çekiniz

	6)Bir adet email tablosu oluşturunuz. Mail gönderme kısmına kadar order geldiği anda bu tabloda mail gönderildi kısmı False. 
	Email backendi çalıştıktran sonra order üzerinden bu değeri True olarak güncelleyiniz.

	Tüm tablolar ve bu tablolara ait özellikler sizlerin tarafından oluşturulması gerekiyor.
	
	Kullanıcılar için faker aynı veri ürettiğinden try: except: durumunu konuşmuştuk.
	Tablo column özellikleri ve kısıtlamları sizler tarafından belirlenecektir. Primary key not null foreing key vs.

	Kodlar githuba yüklenirken aynı zamanda db scheması draw io üzerinden çizilip screen shot alınacak. 

	Daha sonrasında pg admin üzerinden tablolara tüm işlemler bittikten sonra count atılarak tablolardaki veri sayıları ilk 10 değer olacak şekilde tablolarında ss leri yüklenmesi gerekmektedir.

	Db yapısını ister SQL Alchemy üzerinden isterseniz GUI üzerinden yapabilirsiniz. 

