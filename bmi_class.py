class bmi:

    def bmi_calculator(**kwargs):
        weight = kwargs['weight']
        height = kwargs['height']
        return weight/(height/100)**2

    def bmi_classification(bmi_value):

        if bmi_value < 18.5:
            return "Underweight"
        elif (bmi_value >= 18.5 and bmi_value < 25):
            return "Normal Weight"
        elif (bmi_value >= 25 and bmi_value < 30):
            return "Overweight"
        elif (bmi_value >= 30 and bmi_value < 35):
            return "Obesity Class I"
        elif (bmi_value >= 35 and bmi_value < 40):
            return "Obesity Class II"
        else:
            return "Obesity Class III"


if __name__ == "__main__":

    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    class1 = bmi
    bmi_value = class1.bmi_calculator(weight=weight, height=height)
    print(f"Your BMI is {bmi_value}")
    class2 = bmi.bmi_classification(bmi_value)
    print(class2)
