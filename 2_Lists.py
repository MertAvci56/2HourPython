# LİSTS [LİSTELER]**
# [Köşeli parantezlerle gösterilir.]
# İndeks mantığı vardır elemanlar 0'dan başlar.
# Son elemanı -1 ile çağırabilirsin.

myList = [1,2,3,4,5,6,7] # LİSTE OLUŞTURDUK.
print(type(myList))

otherList = list() # Başka bir liste oluşturma yöntemidir.
otherList.append("a")
otherList.append("b")
otherList.append("c")
otherList.append(1) # FARKLI DEĞİŞKENLERİ BARINDIRABİLİR.
otherList.append(True)
otherList.append(4.8)
print(otherList)

x = otherList[0]
print(type(x))

print(otherList[::2]) # INDEX

# NESTED LİSTS (İç içe geçmiş listeler)**
myNestedList = [1,2,"d",["a","b",98],[10,20,"y"]]
print(myNestedList[3][1]) # 3. indexteki listenin 1. indexteki elemanını gösterir.
print(myNestedList[4])
myNestedList[0] = 100 # Listeler mutable yani değiştirilebilirdir.
print(myNestedList)

