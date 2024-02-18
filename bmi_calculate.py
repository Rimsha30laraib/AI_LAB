"""
If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to <25, it falls within the healthy weight range.
If your BMI is 25.0 to <30, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obesity range.
weight (kg) / [height (m)]2
"""
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


bmi = calculate_bmi(weight, height)
classification = classify_bmi(bmi)

print("Your BMI is: {}".format(bmi))
print("You are classified as {}".format(classification))


