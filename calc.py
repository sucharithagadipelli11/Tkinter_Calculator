import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="Black")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=20, ipady=15)

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

r = 1
c = 0

for b in buttons:
    cmd = calc if b == '=' else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Segoe UI", 14),
        width=5,
        height=2,
        bg="orange" if b in "+-*/=" else "black",  # 👈 numbers black
        fg="black" if b in "+-*/=" else "orange",  # 👈 numbers orange
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c > 3:
        c = 0
        r += 1

tk.Button(
    root,
    text="C",
    command=clear,
    font=("Segoe UI", 14),
    bg="Red",
    fg="Black",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4, pady=8)

root.mainloop()