import random
fruitsBox = {}
tuple = ("りんご", "みかん", "バナナ", "トマト", "スイカ")
num = random.randint(1,10)

for fruit in tuple:
    fruitsBox[fruit] = num

print(fruitsBox)
