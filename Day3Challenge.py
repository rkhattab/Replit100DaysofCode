#Create The Ultimate Wacky Receipe Maker
#The output needs to be a nice looking Recipe page tht *concatanates* a dish in this format
#cooking food with burned plant on bed of item
print("=== Ultimate Wacky Recipe Maker ===")
print("""let's come up with a recipe generator to build us an amazing dish for today's evening meal 😭""")
print()
food = input("Name a type of food: ")
plant = input("Name a plant: ")
plant2= input("Name another plant: ")
plant3= input("Name a third plant: ")
cookingMethod = input("Name a cooking method: ")
description = input("Give me a word to describe burned food: ")
item = input("Name a household item: ")
item2 = input("Name another household item: ")
item3 = input("Name another household item: ")
print()
print("For starters: ")
print(cookingMethod, food, "with", description, plant2, "on a bed of",item,".")
print()
print("For the main course:")
print(cookingMethod, plant3, "with", description, food, "on a bed of",item2,".")
print()
print("And finally for dessert:")
print(plant, "with", description, food, "whipped cream",item3,".")

print("bon appetit!")
