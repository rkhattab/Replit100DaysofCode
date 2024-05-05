print("Hello. Welcome to your daily affirmation generator.")

#variables
name = input("What is your name?: ")
weekday = input("What day of the week is it?: ")
fav_food = input("What is your favorite food?: ")
fav_music = input("What is your favorite music?: ")
fav_color = input("What is your favorite color?: ")
fav_animal = input("What is your favorite animal?: ")

#if statements

if weekday == "Monday" or weekday == "monday":
  print("Happy Monday", name, "! You look great today!")
elif weekday == "Tuesday" or weekday == "tuesday":
  print("Happy Tuesday", name, "! Are you going to enjoy your", fav_food, "today?")
  enjoyFood = input("Yes or No?: ")
  if enjoyFood == "Yes" or enjoyFood == "yes"   or enjoyFood == "Yes":
    print("Great! I hope you enjoy your", fav_food, "today!")
  elif enjoyFood == "No" or enjoyFood == "no"   or enjoyFood == "NO":
    print("Aww man, I'm sorry you can't eat your", fav_food, "today.")
elif weekday == "Wednesday" or weekday == "wednesday":
  print("Happy Wednesday", name, "! Enjoy jamming out to your", fav_music, "today, and get that energy up!")
elif weekday == "Thursday" or weekday == "thursday":
  print("Happy Thursday", name, "! It is a glorious occasion be stong like your", fav_animal, "today!")
elif weekday == "Friday" or weekday == "friday":
  print("Happy Friday", name, "! You lookn spiffy today!")
elif weekday == "Saturday" or weekday == "saturday":
  print("Happy Saturday", name, "! It is the weekend and work on your passion projects!")
elif weekday == "Sunday" or weekday == "sunday":
  print("Happy Sunday", name, "! Rest and relaxation are deeply needed. ")
          
else: 
  print("Sorry", name, "I don't know what day that is.")

