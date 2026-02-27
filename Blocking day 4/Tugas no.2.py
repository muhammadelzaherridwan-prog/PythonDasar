import tkinter as tk
from tkinter import messagebox

TARIF = 2000

def hitung_biaya():
    try:
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        lama = keluar - masuk
        if lama < 0:
            messagebox.showerror("Error", "Jam keluar harus lebih besar!")
            return

        biaya = lama * TARIF
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))

    except ValueError:
        messagebox.showerror("Error", "Masukkan jam dalam angka!")

root = tk.Tk()
root.title("Program Parkir")
root.geometry("350x300")

tk.Label(root, text="No Plat Polisi").pack()
entry_plat = tk.Entry(root)
entry_plat.pack()

tk.Label(root, text="Jam Masuk").pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

tk.Label(root, text="Jam Keluar").pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

tk.Label(root, text="Biaya").pack()
entry_biaya = tk.Entry(root)
entry_biaya.pack()

tk.Button(root, text="Hitung Biaya", command=hitung_biaya).pack(pady=10)

root.mainloop()