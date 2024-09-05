# FOR LOOP (FOR DÖNGÜSÜ) , FOR (İÇİN) , İN (İÇİNDE / Mİ)**
myList = [10,20,30,40,50]
for num in myList:
    print(num / 2 * 3)
    print("A")
print("Döngü Bitti!")

print(40 in myList) # Listenin içinde 40 var mı ? demektir.
print("a" in "selahaddin")


# WHILE LOOP (ŞU/BU OLDUĞU SÜRECE)**
m = 0
while m < 10:
    print(m)
    m += 1 # m = m + 1


# IF (EĞER/İSE) , ELSE IF (DEĞİLSE) , ELSE (HİÇBİRİYSE)**
# AND (VE) , OR (YA DA) , NOT (DEĞİL)
x = int(input("Number: "))
if x > 20 and x <= 30:
    print("20 < x <= 30")
elif x < 30 and x <= 40:
    print("30 < x <= 40")
else:
    print("KAPSAM DIŞI!")


# BOOL/BOOLEAN , TRUE YA DA FALSE OPERATÖRÜ**
print(3 > 5)
age = int(input("enter age: "))
print(age >= 18)


# Formatted String (Farklı değişkenleri aynı cümlede kullanmak)
age = 35
print(f"my age is : {age}")

