#myName computer program guard

myName = input("What is your name? ")
if myName == "Reem":
  print("Hey, Welcome back! I hope you are doing well!")
else: 
  print("Error, you are not allowed to enter this computer system.")

# tea or coffee generator
drink = input("Do you prefer coffee or tea? ")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
# Marvel Movie Character Creator
print("Marvel Movie Character Creator")
print("--")
print()
spiderman = input("Do you like 'hanging around'? ")
theHulk = input("Do you like the color green? ")
superMan = input("Do you like to fly? ")
if spiderman == "yes":
  print("You are Spiderman!")
else:
  print("You are not Spiderman.")
if theHulk == "yes":
  print("You are The Hulk!")
else:
  print("You are not The Hulk.")
if superMan == "yes":
  print("You are Superman!")
else:
  print("You are not Superman.")
if spiderman == "no" and theHulk == "no" and superMan == "no":
  print("You are not a superhero.")
else:
  print("""You have discovered that you are a superhero! Congratulations!""")
