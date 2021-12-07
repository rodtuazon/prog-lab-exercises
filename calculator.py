def addition(input1, input2):
    return input1 + input2


def subtraction(input1, input2):
    return input1 - input2


def multiplication(input1, input2):
    return input1 * input2


def division(input1, input2):
    return input1 / input2


print(
    "------------------------------")
print(
    "-C--A--L--C--U--L--A--T--O--R-")

while True:
    print(
        "------------------------------")
    print(
        "Choose an operation\n[1] - Addition\n[2] - Subtraction\n[3] - Multiplication\n[4] - Division")
    print(
        "------------------------------")
    choice = input("Input choice from 1-4: ")

    if choice in ('1', '2', '3', '4'):
        input1 = float(input("Input first number: "))
        input2 = float(input("Input second number: "))

        if choice == '1':
            print(input1, " + ", input2, " = ", addition(input1, input2))
        elif choice == '2':
            print(input1, " - ", input2, " = ",
                  subtraction(input1, input2))
        elif choice == '3':
            print(input1, " * ", input2, " = ",
                  multiplication(input1, input2))
        elif choice == '4':
            print(input1, " / ", input2, " = ", division(input1, input2))

        repeatCalculation = input(
            "Do you want to do another calculation? [yes/no]: ")
        if repeatCalculation == "yes":
            continue
        elif repeatCalculation == "no":
            break

    else:
        print("Invalid input")
