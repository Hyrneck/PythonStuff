#!/opt/anaconda3/bin/python

print("Welcome to the tip calculator!")
total_bill = float(input("How much was the total bill?"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15"))
number_people = int(input("How many people to split the bill?"))
print(f"Each person should pay: ${round((((total_bill * (tip_percent/ 100)) + total_bill) / number_people),2)}")

