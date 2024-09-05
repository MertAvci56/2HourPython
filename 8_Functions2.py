# KENDİ FONKSİYONUZUMU OLUŞTURMAK:

def helloPython():
    print("hello")
    print("world")
    print("python")

helloPython()


def helloName(name):
    print(f"hello {name}")

helloName("mert")
helloName("james")


def pythonSum(number1, number2):
    print(number1 + number2)

pythonSum(5, 15)
x = pythonSum(10, 20)
print(type(x))
if x:
    print(x)
else:
    print("X YOK")

# Return ile değer döndürme yaptığımızdan x artık integer olur.
def returnSum(num1, num2, num3):
    print(num1 + num2 + num3)
    return num1 + num2 + num3

x = returnSum(10, 20, 30)
print(x)


def stringCheck(s):
    if s == "atil":
        print("atil")
    else:
        print("not atil")

stringCheck("sdfds")


def defaultValueFunction(name="Atil"):
    print(name)

defaultValueFunction("James")

