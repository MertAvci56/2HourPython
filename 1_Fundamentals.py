# VARIABLES(DEĞİŞKENLER)**
# String = Metinsel değişkenlerdir. 
# Integer = Tam sayı değişkenlerdir.
# Float = Kesirli/reel sayı değişkenlerdir.
# Bool/Boolean = True/False değişkenlerdir.
# Complex = Karmaşık sayı değişkenlerdir. "J" ile yapılır.

print("Hello World")
print(5 + 4)

x = 5 # Değişken tanımladık.
print(type(x)) # Değişkenin türünü verir.

pi = 3.14
print(pi)

x = 4.4
print(type(x)) # Python esnektir, değişkeni direkt değiştirebilirsin.

myBoolean = True
print(myBoolean)


# STRİNG
myStr = "selahaddin mert" 
# Stringler immutabledir. Yani değiştirilemez.
# Indexler 0'dan başlar. Boşluklarda sayılır.
print(myStr[3]) # 3. indexi verir. 
print(len(myStr)) # Len fonksiyonu uzunluğu verir.
print(myStr[-1]) # -1 son indexi verir.
print(myStr[len(myStr)-1]) # Son indexi veren başka bir yoldur.
print(myStr * 2) # String çarpmasıdır. (Yan yana yazar.)
print("mert " + "avci") # String toplamasıdır.


# SLICING (Dilimleme işlemleri) (Index)
print(myStr.capitalize()) # İLK harfi büyük yazar.
print(myStr.count("a")) # İçinde kaç adet "a" olduğunu sayar.

# [Start:Stop:Stepping Size]
print(myStr[3:]) # 3. indexten başla demektir.
print(myStr[:3]) # 0-1 ve 2'yi al 3'te dur demektir.
print(myStr[::2]) # 2'şer atlayarak yazar.
print(myStr[::-1]) # TÜM STRINGI TERSTEN YAZDIRIR.

