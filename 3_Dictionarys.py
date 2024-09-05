# DICTIONARYS {SÖZLÜKLER}**
# key - value pairing / anahtar ve değer eşleşmesi
# Sözlüklerde süslü {} parantez kullanılır.
# İLK yazdığımız her zaman anahtar olur.
my_dictionary = {"key":"value"}
print(my_dictionary["key"])
print(type(my_dictionary))

# index mantığı yok [] köşeli parantez YOK.
my_fitness_dict = {"run":100,"swim":200}
print(my_fitness_dict["swim"])
print(my_fitness_dict["run"])

# anahtarları stringlerlede listelerlede integerlarlada veya bir başka sözlüklerle değer atayabiliriz.
# bir çok veri tipiyle eşleşebilir kısaca.
new_list = {"key1":100, "key2": [1,2,3], "key3":"apple", 20:30, "key4": {"a":5}}
print(new_list[20])
print(new_list["key3"])
print(new_list["key4"]["a"])

# .pop(anahtar) Seçtiğimiz anahtar-değeri sözlükten atar.
print(new_list.pop("key3"))

# .keys sadece anahtarları verir.
print(new_list.keys())

# .values sadece değerleri verir.
print(new_list.values())

# .items hepsini verir.
print(new_list.items())

# sözlükler mutable/değiştirilebilirdir. EKLEMELER yapılabilir.
yeniListem = {"k1":1, "k2":2}
print(yeniListem)
yeniListem["k1"] = 315
print(yeniListem)
yeniListem["k3"] = 7
print(yeniListem)

# anahtarı yazarsan değeri verir ama değeri çağırırsan anahtarı vermez.
# sözlükleri süslü parantezle oluştururuz ama anahtarı normal köşeli
#-parantezle yazarız değeri çağırması için.(index gibi)

# .get KOMUTUNU ARAŞTIR! (HATA ALMAMAK İÇİN KULLANILIR)
print(new_list.get("mert",0)) # mert yoksa 0 döndür gibi.

# BOŞ DICTIONARY OLUŞTURMAK**
# 1.YOL
my_dict = {}
print(type(my_dict))
print(my_dict)
# 2.YOL
my_dict_2 = dict()
my_dict_2["key1"] = 100
my_dict_2["b"] = [1,2,3,4,5] # LİSTE BİLE EKLEYEBİLİRSİN.
my_dict_2["A"] = True
print(type(my_dict_2)) 
print(my_dict_2)
print(my_dict_2["b"] [0]) # Değerdeki listenin içeriğinde indexler geçerlidir.
