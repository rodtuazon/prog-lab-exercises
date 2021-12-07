def bmi(**kwargs):
    weight = kwargs['weight']
    height = kwargs['height']
    return weight/(height/100)**2


if __name__ == "__main__":

    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    bmi_value = bmi(weight=weight, height=height)
    print(f"Your BMI is {bmi_value}")

    if bmi_value < 18.5:
        print("Underweight")
    elif (bmi_value >= 18.5 and bmi_value < 25):
        print("Normal Weight")
    elif (bmi_value >= 25 and bmi_value < 30):
        print("Overweight")
    elif (bmi_value >= 30 and bmi_value < 35):
        print("Obesity Class I")
    elif (bmi_value >= 35 and bmi_value < 40):
        print("Obesity Class II")
    else:
        print("Obesity Class III")
