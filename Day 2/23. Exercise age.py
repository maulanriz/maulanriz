age = int(input("your age: "))

max_day = 365 * 90
max_week = 52 * 90
max_month = 12 * 90
max_year = 90

your_day = 365  * age
your_week = 52 * age
your_month = 12 * age
your_year = age

left_day = max_day - your_day
left_week = max_week - your_week
left_month = max_month - your_month
left_age = max_year - your_year

print(f"you have {left_age} years, {left_day} days, {left_week} weeks, and {left_month} months left")