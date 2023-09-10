import tkinter as tk

# Create a function to handle button clicks
def button_click(number):
    current = display_var.get()
    display_var.set(current + str(number))

# Create a function to handle the "=" button click
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create a function to clear the display
def clear():
    display_var.set("")

# Create the main window
window = tk.Tk()
window.title("Calculator App")

# Create a display area
display_var = tk.StringVar()
display = tk.Entry(window, textvariable=display_var, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(window, text=str(i), command=lambda i=i: button_click(i))
    button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, command=lambda operator=operator: button_click(operator))
    button.grid(row=i + 1, column=3)

# Create "=" and "C" buttons
equals_button = tk.Button(window, text="=", command=calculate)
equals_button.grid(row=4, column=0, columnspan=2)
clear_button = tk.Button(window, text="C", command=clear)
clear_button.grid(row=4, column=2, columnspan=2)

# Run the tkinter main loop
window.mainloop()
