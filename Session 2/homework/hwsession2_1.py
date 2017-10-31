n = int(input("Enter your weight (kg): "))
m = int(input("Enter your height (cm): "))
height = m*0.01
BMI = n / height**2
print("Your BMI is:", BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
