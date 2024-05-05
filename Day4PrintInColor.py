#Create your own adventure story that places your user in the role of the main character and we'll 
#even customize the story to suit their interests

print("=== Your Adventure Simulator ===")
print()
print("""You'll be asked a bunch of questions, and we will create your adventure story with you as the star!""")
print()
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your super power: ")
print() 
print("Our story begins as our hero", name, "approaches a foreboding castle...")
print()
print("Suddenly a bolt of lightning striked the ground at the feet of", name,"!")
print()
print("""'Our final battle begins!' shouts the evil", enemy, "clearly missing the fact that", name, "has the super pwer of", superPower, "which means they will win quite easily.""")
print()
print("Uh, oh, you've been given a", "\033[34m", "warning", "\033[35mfor being a bad, bad person.")
