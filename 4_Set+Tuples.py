# SET = {1,2,3,4,5} Aynı elemandan 1'den fazla olamaz.
# unique elements / tekil elemanlar / her elemandan bir tane
# unordered / sırası yok / sırası önemli değil
mySet = {1,2,3,4,5}
print(type(mySet))

#Boş Set Oluşturmak:
mySet0 = set()
mySet0.add("a")
mySet0.add("b")
mySet0.add("c")
mySet0.add(1)
print(mySet0)


# TUPLE = LİSTE GİBİ AMA DEĞİŞTİRİLEMEZ, IMMUTABLE!
# AYNI ZAMANDA KÖŞELİ YERİNE NORMAL PARANTEZ KULLANILIR!
myTuple = (1,2,2,2,5,6,7)
print(type(myTuple))
myTuple[0] = 5 # IMMUTABLE

# TUPLE UNPACKING
(x,y) = (5,4)
print(x)
# x ve y değerlerini değiştirmek için:
Temp = x
x = y
y = Temp
print(x)
# SHORTCUT (KISAYOL)
(m,n) = (10,20)
(m,n) = (n,m)
print(m)

