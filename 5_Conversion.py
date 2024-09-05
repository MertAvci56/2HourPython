# DÖNÜŞTÜRME**
myInt = 10
print(str(myInt))
print(type(str(myInt)))

print(int("40"))
print(type(int("40")))

a = int(input("First number: "))
b = int(input("Second number: "))
print(a + b)

myList = [1,2,3,1,2,3,1,2,3]
print(set(myList)) # Listeyi, sete çevirdik. Veya tam tersini yap.


# ERROR HANDLING (HATA ELE ALMA)**
try:
    int("mert")
except:
    print("error")
    
# PROGRAM ÇÖKMESİN DİYE ANA EKRANA HATA MESAJI DÖNDÜRDÜK.
userAge = input("Enter Age: ")
try:
    print(int(userAge) * 2)
except:
    print("Enter Age!!!")

