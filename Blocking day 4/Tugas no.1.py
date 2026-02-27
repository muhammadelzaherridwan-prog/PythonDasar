import tkinter as tk
from tkinter import ttk, messagebox

# Membuat window
root = tk.Tk()
root.title("Program Kasir Sederhana")
root.geometry("700x500")

# Variabel total
total_belanja = 0

# ================== FUNGSI ==================
def tambah_item():
    global total_belanja
    
    try:
        nama = entry_nama.get()
        harga = int(entry_harga.get())
        jumlah = int(entry_jumlah.get())
        
        subtotal = harga * jumlah
        total_belanja += subtotal
        
        tree.insert("", tk.END, values=(nama, harga, jumlah, subtotal))
        
        label_total.config(text=f"Total: Rp {total_belanja}")
        
        entry_nama.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Harga dan Jumlah harus angka!")

def hapus_item():
    global total_belanja
    selected = tree.selection()
    if selected:
        item = tree.item(selected)
        subtotal = item['values'][3]
        total_belanja -= subtotal
        tree.delete(selected)
        label_total.config(text=f"Total: Rp {total_belanja}")

def reset_transaksi():
    global total_belanja
    for item in tree.get_children():
        tree.delete(item)
    total_belanja = 0
    label_total.config(text="Total: Rp 0")

# ================== INPUT ==================
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama Barang").grid(row=0, column=0)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

tk.Label(frame_input, text="Harga").grid(row=1, column=0)
entry_harga = tk.Entry(frame_input)
entry_harga.grid(row=1, column=1)

tk.Label(frame_input, text="Jumlah").grid(row=2, column=0)
entry_jumlah = tk.Entry(frame_input)
entry_jumlah.grid(row=2, column=1)

tk.Button(frame_input, text="Tambah", command=tambah_item, bg="green", fg="white").grid(row=3, columnspan=2, pady=5)

# ================== TABEL ==================
columns = ("Nama", "Harga", "Jumlah", "Subtotal")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(pady=10)

for col in columns:
    tree.heading(col, text=col)

# ================== TOTAL ==================
label_total = tk.Label(root, text="Total: Rp 0", font=("Arial", 14, "bold"))
label_total.pack(pady=10)

# ================== TOMBOL ==================
frame_button = tk.Frame(root)
frame_button.pack()

tk.Button(frame_button, text="Hapus Item", command=hapus_item, bg="red", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_button, text="Reset", command=reset_transaksi, bg="orange", fg="white").grid(row=0, column=1, padx=5)

root.mainloop()