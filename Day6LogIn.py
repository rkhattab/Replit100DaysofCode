#Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting. 

print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
if username == "mark" and password == "password1234":
  print("""Welcome Mark! Today is a new day, and we have to work hard to make some money and achieve our goals.""")
elif username == "suzanne" and password == "su74syee":
  print("""Hey there Suzanne! Another day another dollar... am I right? Well hopefully you are one day closer to retirement and this will all be over soon. Assuming you don't just die randomly like so many other people that never get to reach nor enjoy retirement.""")
elif username == "reem" and password == "reem1234":
  print("""Hey there Reem! Have you thought about investing in Bitcoin, it might help you be able to quit this line of work and live a happy life. I know you can do it!""")
else:
  print("Go away!")


### Fix my Code Activity 

season = input("What is your favorite season? ")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")




