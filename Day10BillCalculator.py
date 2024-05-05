#a calculator that takes into consideration tips 
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? Please do not use the % sign in your answer, use whole numbers only. "))
bill_with_tip = ((tip / 100) * myBill) + myBill
#Checking the math
#print(bill_with_tip)
#print(.2 * myBill + myBill)
answer = bill_with_tip/ numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
