import tkinter as tk
from tkinter import messagebox
def so_buoc_ondinh(candy):
    n = len(candy)
    if n <= 1:
        return 0
    buoc = 0
    while True:
        check = True
        for i in range(n):
            if candy[i] > 1:
                check = False
                break
        if check:
            return buoc
        new_candy = candy.copy()
        for i in range(n):
            if candy[i] > 1:
                new_candy[i] -= 2
                new_candy[(i - 1) % n] += 1
                new_candy[(i + 1) % n] += 1
        candy = new_candy
        buoc += 1
            if buoc > 100000:
          return -1
def tinh_toan():
    text = entry.get().strip()
    if text == "":
        messagebox.showwarning("Lỗi", "Bạn chưa nhập dữ liệu")
        return
    parts = text.split()
    candy = []
    try:
        for i in parts:
            candy.append(int(i))
    except:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số nguyên")
        return
    if sum(candy) > len(candy):
        ket_qua.set("Không ổn định")
    else:
        buoc = so_buoc_ondinh(candy)
        ket_qua.set(str(buoc))
root = tk.Tk()
root.title("Candy Share")
root.geometry("400x200")
label = tk.Label(root, text="Nhập số kẹo (cách nhau bởi dấu cách):")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack()
btn = tk.Button(root, text="Tính", command=tinh_toan)
btn.pack(pady=10)
ket_qua = tk.StringVar()
result_label = tk.Label(root, textvariable=ket_qua, fg="blue")
result_label.pack(pady=10)
root.mainloop()
