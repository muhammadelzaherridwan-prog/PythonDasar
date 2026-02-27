baris = int(input("Masukkan jumlah baris: "))

for i in range(baris):
    print(" " * (baris - i - 1) + "* " * (i + 1))