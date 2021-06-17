import math
items = int(input("How many items you got? "))
pbox = int(input("How many per box? "))

boxes = math.ceil(items/pbox)

print(f"You need {boxes}, hoe")