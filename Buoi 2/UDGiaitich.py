import tkinter as tk
import sympy as sym
from tkinter import messagebox

def daoham():
    try:
        ham = ham_input.get()
        if all(char.isdigit() or char == 'x' or char in ['+', '-', '*', '/', '^', '(', ')'] for char in ham):
            x = sym.Symbol('x')
            fx = sym.sympify(ham)
            daoham = sym.diff(fx, x)
            kqua.configure(text=f"Đạo hàm: {daoham}")
        else:
            messagebox.showwarning("Chú ý", "Hãy nhập biểu thức với các chữ số và biến x")
    except ValueError:
        messagebox.showwarning("Chú ý", "Nhập đúng định dạng của biểu thức")

def tichphan():
    try:
        ham = ham_input.get()
        if all(char.isdigit() or char == 'x' or char in ['+', '-', '*', '/', '^', '(', ')'] for char in ham):
            x = sym.Symbol('x')
            fx = sym.sympify(ham)
            tichphan = sym.integrate(fx, x)
            kqua.configure(text=f"Tích phân: {tichphan}")
        else:
            messagebox.showwarning("Chú ý", "Hãy nhập biểu thức với các chữ số và biến x")
    except ValueError:
        messagebox.showwarning("Chú ý", "Nhập đúng định dạng của biểu thức")

def ghan():
    try:
        ham = ham_input.get()
        if all(char.isdigit() or char == 'x' or char in ['+', '-', '*', '/', '^', '(', ')'] for char in ham):
            x = sym.Symbol('x')
            fx = sym.sympify(ham)
            ghan = sym.limit(fx, x, 0)
            kqua.configure(text=f"Giới hạn: {ghan}")
        else:
            messagebox.showwarning("Chú ý", "Hãy nhập biểu thức với các chữ số và biến x")
    except ValueError:
        messagebox.showwarning("Chú ý", "Nhập đúng định dạng của biểu thức")

def tinh_dien_tich(f, x, a, b, n):
    delta_x = (b - a) / n
    x_vals = [a + i * delta_x for i in range(n)]
    area = 0

    for x_val in x_vals:
        height = f.subs(x, x_val)
        rectangle_area = height * delta_x
        area += rectangle_area

    return area

def rutgon():
    try:
        ham = ham_input.get()
        if all(char.isdigit() or char == 'x' or char in ['+', '-', '*', '/', '^', '(', ')'] for char in ham):
            x = sym.Symbol('x')
            fx = sym.sympify(ham)
            rutgon = sym.simplify(fx)
            kqua.configure(text=f"Biểu thức rút gọn: {rutgon}")
        else:
            messagebox.showwarning("Chú ý", "Hãy nhập biểu thức với các chữ số và biến x")
    except ValueError:
        messagebox.showwarning("Chú ý", "Nhập đúng định dạng của biểu thức")
window = tk.Tk()
window.title("Ứng dụng hỗ trợ môn giải tích")
window.geometry('500x200')

ham_frame = tk.Frame(window)
ham_frame.place(x=10, y=10)

ham_label = tk.Label(ham_frame, text="Biểu thức hàm số:")
ham_label.pack(side=tk.LEFT)

ham_input = tk.Entry(ham_frame)
ham_input.pack(side=tk.LEFT)

tdaoham = tk.Button(window, text="Tính đạo hàm", command=daoham)
tdaoham.place(x=10, y=50)

ttichphan = tk.Button(window, text="Tính tích phân", command=tichphan)
ttichphan.place(x=120, y=50)

tghan = tk.Button(window, text="Tính giới hạn", command=ghan)
tghan.place(x=230, y=50)

trutgon = tk.Button(window, text="Rút gọn biểu thức", command=rutgon)
trutgon.place(x=350, y=50)

kqua = tk.Label(window, text="Kết quả:")
kqua.place(x=10, y=90)

window.mainloop()
