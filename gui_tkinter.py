import tkinter as tk


def calculate_bmi_metric(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return f"Your BMI is {bmi:.2f}."


def calculate_bmi_imperial(weight, height):
    bmi = (703 * weight) / (height ** 2)
    return f"Your BMI is {bmi:.2f}."


def calculate_bmi():
    unit_choice = unit_var.get()

    if unit_choice == 'Metric':
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        result = calculate_bmi_metric(weight, height)
    elif unit_choice == 'Imperial':
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())
        height_in_inches = 12 * feet + inches
        result = calculate_bmi_imperial(weight, height_in_inches)
    else:
        result = ""

    result_label.config(text=result)


window = tk.Tk()
window.title("BMI Calculator")

unit_var = tk.StringVar(value='Metric')

unit_frame = tk.Frame(window)
unit_frame.pack()

metric_button = tk.Radiobutton(unit_frame, text='Metric', variable=unit_var, value='Metric')
metric_button.pack(side=tk.LEFT)

imperial_button = tk.Radiobutton(unit_frame, text='Imperial', variable=unit_var, value='Imperial')
imperial_button.pack(side=tk.LEFT)

weight_label = tk.Label(window, text='Weight:')
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text='Height:')
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

feet_label = tk.Label(window, text='Feet:')

feet_entry = tk.Entry(window)

inches_label = tk.Label(window, text='Inches:')

inches_entry = tk.Entry(window)

calculate_button = tk.Button(window, text='Calculate', command=calculate_bmi)

result_label = tk.Label(window, text="")


def hide_imperial_fields():
    feet_label.pack_forget()
    feet_entry.pack_forget()
    inches_label.pack_forget()
    inches_entry.pack_forget()
    calculate_button.pack_forget()
    result_label.pack_forget()


def show_imperial_fields():
    feet_label.pack()
    feet_entry.pack()
    inches_label.pack()
    inches_entry.pack()
    weight_label.config(text='Weight (lbs):')
    calculate_button.pack()
    result_label.pack()


def show_metric_fields():
    height_label.pack()
    height_entry.pack()
    height_label.config(text='Height (cm):')
    weight_label.config(text='Weight (kg):')
    calculate_button.pack()
    result_label.pack()


def hide_metric_fields():
    height_entry.pack_forget()
    height_label.pack_forget()
    calculate_button.pack_forget()
    result_label.pack_forget()


def update_fields():
    if unit_var.get() == 'Metric':
        hide_imperial_fields()
        show_metric_fields()
    elif unit_var.get() == 'Imperial':
        hide_metric_fields()
        show_imperial_fields()


update_fields()

unit_var.trace('w', lambda *args: update_fields())

window.mainloop()
