import tkinter as tk
from tkinter import messagebox

def simpan():
    data = f"""
    Nama: {entry_nama.get()}
    Tanggal Lahir: {entry_ttl.get()}
    Asal Sekolah: {entry_sekolah.get()}
    NISN: {entry_nisn.get()}
    Nama Ayah: {entry_ayah.get()}
    Nama Ibu: {entry_ibu.get()}
    No HP: {entry_hp.get()}
    Alamat: {text_alamat.get("1.0", tk.END)}
    """
    messagebox.showinfo("Data Tersimpan", data)

def hapus():
    entry_nama.delete(0, tk.END)
    entry_ttl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Data Siswa Baru")
root.geometry("400x500")

tk.Label(root, text="Nama Lengkap").pack()
entry_nama = tk.Entry(root, width=40)
entry_nama.pack()

tk.Label(root, text="Tanggal Lahir").pack()
entry_ttl = tk.Entry(root, width=40)
entry_ttl.pack()

tk.Label(root, text="Asal Sekolah").pack()
entry_sekolah = tk.Entry(root, width=40)
entry_sekolah.pack()

tk.Label(root, text="NISN").pack()
entry_nisn = tk.Entry(root, width=40)
entry_nisn.pack()

tk.Label(root, text="Nama Ayah").pack()
entry_ayah = tk.Entry(root, width=40)
entry_ayah.pack()

tk.Label(root, text="Nama Ibu").pack()
entry_ibu = tk.Entry(root, width=40)
entry_ibu.pack()

tk.Label(root, text="Nomor Telepon / HP").pack()
entry_hp = tk.Entry(root, width=40)
entry_hp.pack()

tk.Label(root, text="Alamat").pack()
text_alamat = tk.Text(root, width=30, height=5)
text_alamat.pack()

tk.Button(root, text="Simpan", command=simpan).pack(side=tk.LEFT, padx=20, pady=20)
tk.Button(root, text="Hapus", command=hapus).pack(side=tk.RIGHT, padx=20, pady=20)

root.mainloop()