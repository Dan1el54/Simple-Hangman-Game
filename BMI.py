
weight = float(input())
height = float(input())

BMI = weight/height**2

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25.0:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 30:
    print("Obesity")