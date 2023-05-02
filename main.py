def calculate_bmi_metric(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return f"Your BMI is {bmi:.2f}."


def calculate_bmi_imperial(weight, height):
    bmi = (703 * weight) / (height ** 2)
    return f"Your BMI is {bmi:.2f}."


print("Welcome to this BMI Calculator.")

while True:
    unit_choice = input("Please choose Metric or Imperial units.\n")

    if unit_choice != "Metric" and unit_choice != "Imperial":
        continue
    elif unit_choice == 'Metric':
        weight = float(input("Please enter your weight in kg.\n"))
        height = float(input("Please enter your height in cm.\n"))
        print(calculate_bmi_metric(weight, height))
        break

    elif unit_choice == 'Imperial':
        weight = float(input("Please enter your weight in lbs.\n"))
        height = input("Please enter your height in the format [feet]'[inches].\n")
        feet, inches = height.split('\'')
        height_in_inches = 12 * float(feet) + float(inches)
        print(calculate_bmi_imperial(weight, height_in_inches))
        break


