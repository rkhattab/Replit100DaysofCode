print("---- How many Seconds in a year Python Program----")
print()
seconds = 60
minutes = 60
hours = 24
days = 365
leapYear = input("Is it a leap year? ")
if leapYear == "yes" or leapYear == "Yes":
  days = 366
  print("Okay, that means there are ", seconds * minutes * hours * days, "seconds in a leap year")
elif leapYear == "no" or leapYear == "No": 
  days = 365
  print("Okay, that means there are ", seconds * minutes * hours * days, "seconds in a year")
else: 
  print("Please enter yes or no, we could not understand your input.")
