# RANGE
print(list(range(50,60))) # 50'den 60'a kadar. 60 dahil değil.
print(tuple(range(50,60)))
print(set(range(50,60)))

myList0 = ["a","b","c","d","e"]
for letter in range(0,len(myList0)-3):
    print(letter)

print(list(range(0,100,20))) # INDEX GİBİ


# ENUMERATE
myList = list(range(5,15))
index = 0
for number in myList:
    print(f"number: {number} index: {index}")
    index += 1

# SHORTCUT:
for num in enumerate(myList):
    print(num)
# VEYA
for (index, number) in enumerate(myList):
    print(f"number: {number} index: {index}")

newList = []
myStr = "Selahaddin Mert"
for letter in myStr:
    newList.append(letter)
    print(newList)
print(newList)

# SHORTCUT (ONE LİNER):
newList1 = []
myStr1 = "Selahaddin Mert"
newList1 = [letter for letter in myStr1]
print(newList1)

