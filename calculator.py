import tkinter as tk

calculation = ""


def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error!")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def backspace():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)




root = tk.Tk()
root.geometry("350x300")
root.configure(bg="slate blue")
text_result = tk.Text(root, height=2, width=19, font=("Arial", 24), bg="dark slate blue", fg="white")
text_result.grid(columnspan=5)

btnac = tk.Button(root, text="AC", bg="deep pink", fg="white", command=clear_field, width=6, font=("arial", 14, "bold"))
btnac.grid(row=2, column=1)

btnde = tk.Button(root, text="<x", command=backspace, width=6, font=("arial", 14, "bold"))
btnde.grid(row=2, column=2)

btndiv = tk.Button(root, text="/", command=lambda: add_calculation("/"), width=6, font=("arial", 14, "bold"))
btndiv.grid(row=2, column=3)

btnmul = tk.Button(root, text="*", command=lambda: add_calculation("*"), width=6, font=("arial", 14, "bold"))
btnmul.grid(row=2, column=4)

btn7 = tk.Button(root, text=7, command=lambda: add_calculation(7), width=6, font=("arial", 14, "bold"))
btn7.grid(row=3, column=1)

btn8 = tk.Button(root, text=8, command=lambda: add_calculation(8), width=6, font=("arial", 14, "bold"))
btn8.grid(row=3, column=2)

btn9 = tk.Button(root, text=9, command=lambda: add_calculation(9), width=6, font=("arial", 14, "bold"))
btn9.grid(row=3, column=3)

btnminus = tk.Button(root, text="-", command=lambda: add_calculation("-"), width=6, font=("arial", 14, "bold"))
btnminus.grid(row=3, column=4)

btn4 = tk.Button(root, text=4, command=lambda: add_calculation(4), width=6, font=("arial", 14, "bold"))
btn4.grid(row=4, column=1)

btn5 = tk.Button(root, text=5, command=lambda: add_calculation(5), width=6, font=("arial", 14, "bold"))
btn5.grid(row=4, column=2)

btn6 = tk.Button(root, text=6, command=lambda: add_calculation(6), width=6, font=("arial", 14, "bold"))
btn6.grid(row=4, column=3)

btnplus = tk.Button(root, text="+", command=lambda: add_calculation("+"), width=6, font=("arial", 14, "bold"))
btnplus.grid(row=4, column=4)

btn1 = tk.Button(root, text=1, command=lambda: add_calculation(1), width=6, font=("arial", 14, "bold"))
btn1.grid(row=5, column=1)

btn2 = tk.Button(root, text=2, command=lambda: add_calculation(2), width=6, font=("arial", 14, "bold"))
btn2.grid(row=5, column=2)

btn3 = tk.Button(root, text=3, command=lambda: add_calculation(3), width=6, font=("arial", 14, "bold"))
btn3.grid(row=5, column=3)

btnper = tk.Button(root, text="%", command=lambda: add_calculation("%"), width=6, font=("arial", 14, "bold"))
btnper.grid(row=5, column=4)

btn0 = tk.Button(root, text=0, command=lambda: add_calculation(0), width=6, font=("arial", 14, "bold"))
btn0.grid(row=6, column=1)

btnopen = tk.Button(root, text="(", command=lambda: add_calculation("("), width=6, font=("arial", 14, "bold"))
btnopen.grid(row=6, column=2)
btnclose = tk.Button(root, text=")", command=lambda: add_calculation(")"), width=6, font=("arial", 14, "bold"))
btnclose.grid(row=6, column=3)

btneq = tk.Button(root, text="=", bg="dodger blue", fg="white", command=evaluate_calculation, width=6,
                  font=("arial", 14, "bold"))
btneq.grid(row=6, column=4)
root.mainloop()
