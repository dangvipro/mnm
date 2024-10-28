import numpy as np
import tkinter as tk
from tkinter import messagebox


def solve_equations():
  try:
    n = int(entry_n.get())
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):
      coefficients = entry_coeffs[i].get().strip().split()
      A[i] = list(map(float, coefficients))
      B[i] = float(entry_values[i].get())

    # Kiểm tra định thức
    if np.linalg.det(A) != 0:
      solution = np.linalg.solve(A, B)
      result_text = "Giải của hệ phương trình là:\n"
      for i, val in enumerate(solution):
        result_text += f"x[{i}] = {val:.2f}\n"
      messagebox.showinfo("Kết quả", result_text)
    else:
      # Nếu định thức bằng 0, kiểm tra số nghiệm
      if np.linalg.matrix_rank(A) < np.linalg.matrix_rank(np.column_stack((A, B))):
        messagebox.showerror("Lỗi", "Hệ phương trình vô nghiệm.")
      else:
        messagebox.showinfo("Kết quả", "Hệ phương trình có vô số nghiệm.")

  except np.linalg.LinAlgError:
    messagebox.showerror("Lỗi", "Đã xảy ra lỗi trong việc giải hệ phương trình.")
  except ValueError:
    messagebox.showerror("Lỗi", "Đã xảy ra lỗi trong việc nhập dữ liệu.")


def setup_inputs():
  global entry_coeffs, entry_values
  n = int(entry_n.get())

  for widget in frame_inputs.winfo_children():
    widget.destroy()

  entry_coeffs = []
  entry_values = []

  for i in range(n):
    label_coeffs = tk.Label(frame_inputs, text=f"Hệ số cho phương trình {i + 1}:")
    label_coeffs.grid(row=i, column=0)
    entry_coeff = tk.Entry(frame_inputs)
    entry_coeff.grid(row=i, column=1)
    entry_coeffs.append(entry_coeff)

    label_value = tk.Label(frame_inputs, text="Giá trị:")
    label_value.grid(row=i, column=2)
    entry_value = tk.Entry(frame_inputs)
    entry_value.grid(row=i, column=3)
    entry_values.append(entry_value)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải hệ phương trình")

# Nhập số lượng phương trình
frame_n = tk.Frame(root)
frame_n.pack(pady=10)

label_n = tk.Label(frame_n, text="Nhập số lượng phương trình:")
label_n.pack(side=tk.LEFT)
entry_n = tk.Entry(frame_n)
entry_n.pack(side=tk.LEFT)

btn_setup = tk.Button(frame_n, text="Thiết lập", command=setup_inputs)
btn_setup.pack(side=tk.LEFT)

# Khung nhập các hệ số và giá trị
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Nút giải phương trình
btn_solve = tk.Button(root, text="Giải phương trình", command=solve_equations)
btn_solve.pack(pady=10)

# Chạy giao diện
root.mainloop()
