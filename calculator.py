import tkinter as tk

calculation = ""

#symbol = symbol inputted
def symbol(symbol):
  global calculation
  calculation += str(symbol)
  result.delete(1.0, "end")
  result.insert(1.0, calculation)
#results = text output
def results():
  global calculation
  try:
    calculation = str(eval(calculation))
    result.delete(1.0, "end")
    result.insert(1.0, calculation)
  except:
        reset()
        result.insert(1.0, "Error")

#reset = clear button -- clear inputs/outputs
def reset():
  global calculation
  calculation = ""
  result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

result = tk.Text(root, height=2, width=16, font=("Arial",24))
result.grid(columnspan=5)

button_1 = tk.Button(root, text="1", command=lambda: symbol(1), width=5, font=("Arial", 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(root, text="2", command=lambda: symbol(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(root, text="3", command=lambda: symbol(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", command=lambda: symbol(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(root, text="5", command=lambda: symbol(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(root, text="6", command=lambda: symbol(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", command=lambda: symbol(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(root, text="8", command=lambda: symbol(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(root, text="9", command=lambda: symbol(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: symbol(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=2)

button_plus = tk.Button(root, text="+", command=lambda: symbol("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text="-", command=lambda: symbol("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)

button_multiplication = tk.Button(root, text="*", command=lambda: symbol("*"), width=5, font=("Arial", 14))
button_multiplication.grid(row=4, column=4)

button_division = tk.Button(root, text="/", command=lambda: symbol("/"), width=5, font=("Arial", 14))
button_division.grid(row=5, column=4)

button_open = tk.Button(root, text="(", command=lambda: symbol("("), width=5, font=("Arial", 14))
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=")", command=lambda: symbol(")"), width=5, font=("Arial", 14))
button_close.grid(row=5, column=3)

button_clear = tk.Button(root, text="CLEAR", command=reset, width=11, font=("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2,)

button_equal = tk.Button(root, text="=", command=results, width=11, font=("Arial", 14))
button_equal.grid(row=6, column=3, columnspan=2,)
root.mainloop()

