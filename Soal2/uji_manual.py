from debit import hitung_rata_rata, cari_terendah, cek_status

print("Rata-rata:", hitung_rata_rata([10, 20, 30]))
print("Nilai terendah:", cari_terendah([12.5, 14.0, 11.0]))

debit = float(input("Masukkan nilai debit: "))
print("Status debit:", cek_status(debit))