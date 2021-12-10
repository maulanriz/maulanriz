print("Welcome to the tip calculator")

total_bill = float(input("What was total bill? $"))
tip        = float(input("What precentage tip would you like to give? "))
split      = float(input("How many people to split the bill? "))

total_tip = total_bill * (tip/100)
bill_tip = total_bill + total_tip
total_split = bill_tip / split
#result = round(total_split, 2)
result = "{:.2f}".format(total_split)

print(f"Each person should pay: ${result}")
