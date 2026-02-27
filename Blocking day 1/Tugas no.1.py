#Persegi
sisi = float(input("Masukkan panjang sisi persegi: "))

keliling = 4 * sisi
luas = sisi * sisi

print("Keliling persegi =", keliling)
print("Luas persegi =", luas)

#PersegiPanjang
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

keliling = 2 * (panjang + lebar)
luas = panjang * lebar

print("Keliling persegi panjang =", keliling)
print("Luas persegi panjang =", luas)

#Trapesium
a = float(input("Masukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
c = float(input("Masukkan sisi miring kiri: "))
d = float(input("Masukkan sisi miring kanan: "))
tinggi = float(input("Masukkan tinggi: "))

keliling = a + b + c + d
luas = 0.5 * (a + b) * tinggi

print("Keliling trapesium =", keliling)
print("Luas trapesium =", luas)