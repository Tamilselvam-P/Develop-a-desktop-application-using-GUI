import tkinter as tk
def calculate():
    number_1 = float(entry_num1.get())
    number_2 = float(entry_num2.get())
    operation = operator.get()
    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        result = number_1 / number_2
    elif operation == "%":
        result = number_1 % number_2
    result_label.config(text="Result: " + str(result))
# Create main window
window = tk.Tk()
window.title("Arithmetic Calculator")
# Create input fields and labels
entry_num1 = tk.Entry(window)
entry_num1.pack()
operator = tk.StringVar(window)
operator.set("+")  # Default operator
operator_menu = tk.OptionMenu(window, operator, "+", "-", "*", "/", "%")
operator_menu.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()
# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()
# Create label to display result
result_label = tk.Label(window, text="Result: ")
result_label.pack()
# Start main loop
window.mainloop()