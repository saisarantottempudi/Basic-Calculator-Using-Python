import tkinter as tk

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and output
display = tk.Entry(root, width=20, font=('Arial', 16))
display.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif button == '0':
        tk.Button(root, text=button, width=12, height=2, command=lambda b=button: button_click(b)).grid(row=row, column=col, columnspan=2)
        col += 1
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='Clear', width=5, height=2, command=clear_display).grid(row=row, column=0, columnspan=2)

# Exit button
tk.Button(root, text='Exit', width=5, height=2, command=root.quit).grid(row=row, column=2, columnspan=2)

root.mainloop()
