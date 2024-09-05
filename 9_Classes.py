# SINIFLAR/METOTLAR**

class Musician():
    
    job = "Musician"
    
    def __init__(self,name,age,instrument):
        self.name = name
        self.age = age
        self.instrument = instrument
        
    def sing(self):
        print("sing sing sing")
    
    def __len__(self):
        return self.age
    
    def __str__(self):
        return self.name

james = Musician("James",50,"Guitar") #instance
james.age
james.job

james.sing()
len(james)
print(james)


# INHERITANCE (KALITIM)**

class Class1():
    
    def __init__(self):
        print("class 1 created")
    
    def method1(self):
        print("method 1")
        
    def method2(self):
        print("method 2")

class1Instance = Class1()
class1Instance.method1()

class Class2(Class1):
    def __init__(self):
        Class1.__init__(self)
        print("class 2 created")

class2Instance = Class2()
class2Instance.method1()


# POLYMORPHISM**

class Apple():
    
    def __init__(self,name):
        self.name = name
    
    def information(self):
        return self.name + " 100 calories"


class Banana():
    
    def __init__(self,name):
        self.name = name
        
    def information(self):
        return self.name + " 200 calories"

banana = Banana("banana")
apple = Apple("apple")
fruitList = [banana,apple]

for fruit in fruitList:
    print(fruit.information())


# SCOPE (KAPSAM)**

number = 10
print(number)

number = 10
def multiply(num1):
    number = 5
    return num1 * number

multiply(10)
print(number)

number = 10
def multiply(num1):
    number = 5
    return num1 * number
print(multiply(20))
print(number)

#legb -> l-> local, e-> enclosing, g-> global, b->built-in
# GLOBAL**

myName = "Atil"

def myFunction():
    #enclosing
    myName = "James"
    
    def myFunction2():
        #local
        myName = "Lars"
        print(myName)
    
    myFunction2()
    
myFunction()


y = 10
def newFunction():
    global y
    y = 5
    print(y)

newFunction()
print(y)

