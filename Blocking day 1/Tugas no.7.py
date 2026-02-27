print("=== Program Perhitungan Gaji ===")

nama = input("Masukkan Nama: ")
gaji_pokok = float(input("Masukkan Gaji Pokok: "))

tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

print("\n=== Hasil Perhitungan ===")
print("Nama         :", nama)
print("Gaji Pokok   : Rp{:,.2f}".format(gaji_pokok))
print("Gaji Bersih  : Rp{:,.2f}".format(gaji_bersih))