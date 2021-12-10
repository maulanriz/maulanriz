bill = 0

print("Welcome to Pizza Deliveries")
size = input("What size pizza you want? S, M, or L? ")
add_pepperoni = input("Do you want add pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill = 2
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your total bill is {bill}")


