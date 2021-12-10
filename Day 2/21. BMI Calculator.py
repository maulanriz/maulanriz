weight = float(input("Input Weight(kg): "))
height = float(input("Input Height(cm): "))


bmi =  int(weight / (height/100)**2)


print(f"your bmi is: {bmi}")