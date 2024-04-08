import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("300x400")

        self.expression = ""

        # Entry widget to display the expression
        self.entry = ttk.Entry(root, font=('Arial', 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("π", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("√", 6, 3),
            ("log", 7, 0), ("exp", 7, 1), ("^", 7, 2), ("∛", 7, 3),
            ("π", 8, 0), ("e", 8, 1), ("abs", 8, 2), ("deg", 8, 3)
        ]

        for (text, row, column) in buttons:
            btn = ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=column, sticky="nsew")

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except Exception as e:
                self.expression = "Error"
        elif value == "C":
            self.expression = ""
        elif value == "π":
            self.expression += str(math.pi)
        elif value == "e":
            self.expression += str(math.e)
        elif value == "sin":
            self.expression += "math.sin("
        elif value == "cos":
            self.expression += "math.cos("
        elif value == "tan":
            self.expression += "math.tan("
        elif value == "log":
            self.expression += "math.log10("
        elif value == "exp":
            self.expression += "math.exp("
        elif value == "abs":
            self.expression += "abs("
        elif value == "deg":
            self.expression += "math.degrees("
        elif value == "√":
            self.expression += "math.sqrt("
        elif value == "∛":
            self.expression += "** (1/3)"
        else:
            self.expression += value

        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
