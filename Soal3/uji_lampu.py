from lampu import Lampu

lampu = Lampu("L1")

print("Awal:", lampu.aktif, lampu.kecerahan)

lampu.nyalakan()
print("Setelah nyalakan:", lampu.aktif, lampu.kecerahan)

for i in range(3):
    nilai = float(input("Masukkan kecerahan: "))
    lampu.atur(nilai)
    print("Kondisi lampu:", lampu.aktif, lampu.kecerahan)

lampu.matikan()
print("Setelah matikan:", lampu.aktif, lampu.kecerahan)