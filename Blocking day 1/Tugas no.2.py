#VolumeTabung
import math

r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi: "))

volume = math.pi * r * r * t

print("Volume tabung =", volume)

#VolumeBalok
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

volume = panjang * lebar * tinggi

print("Volume balok =", volume)