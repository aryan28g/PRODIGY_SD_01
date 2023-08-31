import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            celsius = temperature
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
        elif unit == "Fahrenheit":
            fahrenheit = temperature
            celsius = (fahrenheit - 32) * 5/9
            kelvin = celsius + 273.15
        elif unit == "Kelvin":
            kelvin = temperature
            celsius = kelvin - 273.15
            fahrenheit = (celsius * 9/5) + 32

        label_result.config(text=f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid temperature value.")


root = tk.Tk()
root.title("Temperature Converter")


label_instruction = tk.Label(root, text="Enter temperature:")
entry_temp = tk.Entry(root)
label_unit = tk.Label(root, text="Select unit:")
combo_unit = tk.StringVar()
combo_unit.set("Celsius")
unit_choices = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown_unit = tk.OptionMenu(root, combo_unit, *unit_choices)
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
label_result = tk.Label(root, text="", justify=tk.LEFT)

label_instruction.pack()
entry_temp.pack()
label_unit.pack()
dropdown_unit.pack()
btn_convert.pack()
label_result.pack()

root.mainloop()



