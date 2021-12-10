print("Welcome to the rollercoaster")
height = int(input("Whats your age in cm? "))

bill = 0
if height > 120:
    print("You can ride roller coaster")
    age = int(input("Whats your age? "))
    if age < 12:
        bill = 5
        print(f"Your ticket is {bill}")
    elif age < 18:
        bill = 7
        print(f"Your ticket is {bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Your ticket is {bill}")
    else:
        bill = 12
        print("Your ticket is $12")
    photo = input("Wanna add photo? Y/N ")
    if photo == "Y":
        bill += 3
    print(f"Total bill is ${bill}")
else:
    print("You cant ride")
