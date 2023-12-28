print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
people = input("How many people to split the bill? ")
bill1 = float(bill)
people1 = float(people)
split = bill1/people1
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage1 = float(percentage)
tip = percentage1/100
total = split*tip + split
final = round(total, 2)
print(f"Each person should pay: ${final}")
