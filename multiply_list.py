try:
    n = list(map(int, input(
        "Enter values you want to multiply [Example: 1x2x3x4x5...]: ").split('x')))

    result = 1
    for x in n:
        result *= x
    print("Total:", result)

except Exception as e:
    print("Error:", e)
