weight = float(input("Input Weight(kg): "))
height = float(input("Input Height(cm): "))


bmi =  round(weight / (height/100)**2)

if bmi < 18.5:
    print(f"your bmi is: {bmi}, underweight")
elif bmi < 24.9:
    print(f"your bmi is: {bmi}, normal")
elif bmi < 29.9:
    print(f"your bmi is: {bmi}, overweight")
else :
    print(f"your bmi is: {bmi}, obsese")

