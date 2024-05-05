print("Fake Fan Finder")
print("---------------")

favAnime = input("What's your favourite Anime? ")
if favAnime == "One piece":
  print("Oh really?! Name me your favorite character?")
  favCharacter = input("What's your favourite character? ")
  if favCharacter == "Nami":
    print("You got that by pure chance. Okay then, what is her job on the ship?")
    job = input("What is her job on the ship?")
    if job == "Navigator":
      print("Hmph! What was her first bounty then?")
      bounty = input("What was her first bounty then?")
      if bounty == "MoneyMan":
        print("That was an excellent episode!")
      elif bounty == "IDK":
        print("seriously?")
      else:
        print("well maybe you should watch the show...")
    else:
      print("See! FAKE One piece fan!")
  else: 
    print("Not familiar with this character")
else: 
  print("Oh sorry to hear you dont like anime")

#This is a fun little program to test and see if someone is truly an anime fan or not!
